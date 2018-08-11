# -*- coding: utf8 -*-
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

import os
import yaml
import markjaml

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

FILE_PINOUT = 'common/pinout.yaml'

master_template = open(os.path.join(BASE_DIR,'common/layout.html')).read()

pinout_path = os.path.join(BASE_DIR, FILE_PINOUT)

pinout = yaml.load(open(pinout_path).read())

html_pins = []
pin_pages = {}

def render_html(template, **kwargs):
    for key in kwargs:
        value = kwargs.get(key)
        if type(value) == dict:
            template = render_html(template, **value)
        elif type(value) in [str, unicode]:
            template = template.replace('{{' + key + '}}', value)

    return template

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

navigation = "\n".join(html_pins)

index_content = markjaml.load(os.path.join(BASE_DIR, 'common', 'index.md'))

html = render_html(master_template,
    navigation = navigation,
    content = index_content['html']
)

with open(os.path.join(BASE_DIR, 'build', 'index.html'), 'w') as output:
    output.write(html)

for pin_page_id in pin_pages:
    pin_page_url = pin_pages[pin_page_id]
    pin_page_content = markjaml.load(os.path.join(BASE_DIR, 'pin', '{}.md'.format(pin_page_id)))
    html = render_html(master_template,
        navigation = navigation,
        content = pin_page_content['html']
    )
    with open(os.path.join(BASE_DIR, 'build', pin_page_url), 'w') as output:
        output.write(html)
