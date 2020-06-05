# micro:bit pinout

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a>

# About this project

micro:bit pinout is a detailed, interactive guide to the GPIO pins on your BBC micro:bit, and the pins that various micro:bit add-ons use.

Find out if two add-ons will work together, or what pins you have available when using a particular add-on.

# Contributing

## Boards/Add-ons

If you've got a micro:bit add-on you want to see listed on microbit.pinout.xyz then please raise an issue with details of your board and a link to an appropriate photo.

You may also raise a pull request, contributing your board directly to `overlay/manufacturer-boardname.md` and image to `resources/manufacturer-boardname.jpg`. Use an existing board as a template and don't forget to test that it builds.

## Translations

Based on what we learned with Pinout.xyz, I'll be handling translations as forks or branches and would appreciate some input from anyone fluent in English and the three most popular non-English lanauges from Pinout.xyz:

* Spanish
* German
* French

# Building

## Linux/OSX/Linux-On-Windows

microbit.pinout.xyz includes a Makefile to help you set up a build environment and generate the .html files. For most build processes you should prepare the Python virtual environment with:

```
make venv
source venv/bin/activate
```

Then you can build the HTML files with:

```
make pinout
```

# Support this project

micro:bit pinout is a passion project put together in my free time, leverging my first-hand knowledge of designing, manufacturing and supporting micro:bit add-ons at Pimoroni.

If you'd like to keep me fed, fuelled and beered while I slog away and contribute to hosting and domain costs please head on over to my Patreon and throw a dollar my way - https://www.patreon.com/gadgetoid - thank you!

# With thanks to

Micro:bit Educational Foundation for inspiration with the web design from their micro:bit classroom tool.
