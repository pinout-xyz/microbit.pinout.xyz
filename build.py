# -*- coding: utf8 -*-
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

import os
import yaml
import markjaml
import glob
import re

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

def src_file(dir, file):
    return os.path.join(BASE_DIR, dir, file)

def save_file(dir, file, content):
    path = src_file(dir, file)
    print("Saving: {}".format(path))
    with open(path, 'w') as output:
        output.write(content)

pinout = yaml.load(open(src_file('common', 'pinout.yaml')).read())

overlays = glob.glob(src_file('overlay/', '*.md'))

pin_pages = {}

def render_template(_template, **kwargs):
    _html = open(src_file('common', '{}.html'.format(_template))).read()
    return render_html(_html, '', **kwargs)


def render_html(_html, _parent='', **kwargs):
    for key in kwargs:
        value = kwargs.get(key)
        if type(value) == dict:
            if _parent != '':
                _html = _html.replace('{{count(' + _parent + ':' + key + ')}}', str(len(value)))
                _html = render_html(_html, _parent + ':' + key, **value)
            else:
                _html = _html.replace('{{count(' + key + ')}}', str(len(value)))
                _html = render_html(_html, key, **value)
        elif type(value) in [str, unicode]:
            if _parent != '':
                _html = _html.replace('{{' + _parent + ':' + key + '}}', value)
            else:
                _html = _html.replace('{{' + key + '}}', value)

    return _html


def get_pin_index_from_id(pin_id):
    for pin_index in pinout['pins']:
        if pinout['pins'][pin_index]['id'].lower() == pin_id.lower():
            return pin_index
    return None

# Generate left-hand navigation

def build_navigation(overlay=None):
    html_pins = []
    for pin_index in pinout['pins']:

        css_class = []

        pin_data = pinout['pins'][pin_index]
        pin_id = pin_data.get('id', None)
        pin_name = pin_data.get('name', None)
        pin_type = pin_data.get('type', None)
        pin_info = pin_data.get('info', None)
        if pin_type is not None:
            pin_type = pin_type.split("/")

        text_name = ''

        if 'Power' in pin_type:
            text_name = 'Power'
        elif 'Ground' in pin_type:
            text_name = 'Ground'
        else:
            text_name = pin_id

        text_desc = ''
        text_info = ''

        if pin_info is not None:
            text_info = "<small>{}</small>".format(pin_info)

        if pin_name != text_name and pin_name is not None:
            text_desc = pin_name

        if text_desc != '':
            text_desc = "<strong>{}</strong>".format(text_desc)

        if overlay is not None:
            if 'data' in overlay:
                if 'pin' in overlay['data']:
                    if pin_id.upper() in overlay['data']['pin']:
                        pin_data = overlay['data']['pin'][pin_id.upper()]
                        
                        if 'name' in pin_data:
                            pin_info = pin_data['name']
                        elif 'mode' in pin_data:
                            pin_info = pin_data['mode']

                        text_desc = "<strong>{}</strong>".format(pin_info)
                        css_class += ['active']

        for t in pinout.get('types'):
            if t in pin_type:
                css_class += ["type-{}".format(t.lower())]

        css_class = " ".join(css_class)

        pin_slug = markjaml.slugify(pin_name or pin_info)

        pin_slug = 'power' if pin_slug == '3v' else pin_slug
        pin_slug = 'ground' if pin_slug == '0v' else pin_slug

        pin_url = "pin-{pin_id}-{pin_slug}.html".format(
            pin_id=pin_id.lower(),
            pin_slug=pin_slug
        )

        html_pins += ["<li id=\"pin-{index}\" class=\"{css_class}\"><a href=\"{url}\"><span>{name}</span>{desc}{info}</a></li>".format(
            index=pin_index,
            id=pin_id,
            url=pin_url,
            name=text_name,
            desc=text_desc,
            info=text_info,
            css_class=css_class
        )]

        if pin_id.lower() not in pin_pages.keys():
            pin_pages[pin_id.lower()] = pin_url

    return "\n".join(html_pins)

navigation = build_navigation()

# Generate various pin pages

for pin_page_id in pin_pages:
    pin_page_url = pin_pages[pin_page_id]
    pin_page_content = markjaml.load(src_file('pin', '{}.md'.format(pin_page_id)))
    back_button = '<a href="index.html" class="button">Back</a>'

    pin_navigation = navigation

    if pin_page_id == '3v':
        pin_navigation = pin_navigation.replace(
            'type-power',
            'active type-power'
        )
    elif pin_page_id == '0v':
        pin_navigation = pin_navigation.replace(
            'type-ground',
            'active type-ground'
        )
    else:
        index = get_pin_index_from_id(pin_page_id)
        pin_navigation = pin_navigation.replace(
            '"pin-{}" class="'.format(index),
            '"pin-{}" class="active '.format(index)
        )

    html = render_template(
        'layout',
        navigation = pin_navigation,
        content = back_button + pin_page_content['html']
    )

    save_file('build', pin_page_url, html)

# Generate overlay/add-on pages

overlay_info = {}
addonsmain = ''

for overlay in overlays:
    overlay_content = markjaml.load(overlay)

    content = render_template(
        'overlay.part',
        **overlay_content
    )

    overlay_navigation = build_navigation(overlay_content)

    html = render_template(
        'layout',
        navigation = overlay_navigation,
        content = content
    )

    filename = os.path.basename(overlay_content['data']['src'])
    filename = filename.replace('.md', '')
    filename = markjaml.slugify(filename)
    filename = filename + ".html"

    save_file('build', filename, html)

    product_name = os.path.basename(overlay_content['data']['src'])
    product_name = product_name.replace('.md', '')
    product_name = markjaml.slugify(product_name)

    overlay_name = overlay_content['data']['manufacturer'] + ' ' + overlay_content['data']['name']


    addonsmain += '''
    <div class="card" catname="apples" style="visibility: visible; display: block;">
        <a style="text-decoration: none; color: black !important;" href="{filename}">
            <div style="padding:5px;cursor:pointer;">
                <div>
                    <img class="card-logo" src="{image}" alt="apples">
                </div>
                <h3 class="name">{name}</h3>
            </div>
        </a>
    </div>
    '''.format(
        filename=filename,
        name=overlay_name,
        image="resources/" + product_name + ".jpg"
    )


# Generate index.html

index_content = markjaml.load(src_file('common', 'index.md'))

html = render_template(
    'layout',
    navigation = navigation,
    content = render_template(
        'index.part',
        content = index_content['html'],
        addons = addonsmain
    )
)

save_file('build', 'index.html', html)