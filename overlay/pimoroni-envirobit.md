<!--
---
name: enviro:bit
type: sensor
manufacturer: Pimoroni
description: Temperature, Pressure, Humidity, Sound and Light Sensors
pxt: https://github.com/pimoroni/pxt-envirobit
python: https://github.com/pimoroni/micropython-envirobit
buy: https://shop.pimoroni.com/products/enviro-bit
image: 'pimoroni-envirobit.jpg'
pin:
  P20:
    mode: I2C
  P19:
    mode: I2C
  P2:
    name: Microphone
    mode: analog
  P8:
    name: Lights
    mode: digital
    active: high
i2c:
  '0x29':
    name: Light/Colour Sensor
    device: TCS3472
  '0x76':
    name: Temp/Pressure/Humidity Sensor
    device: BME280
-->
The Pimoroni enviro:bit combines a BME280, capable of reading the Temperature, Pressure and Humidity with a MEMS Microphone for sound level and clap sensing and a TCS3472 with onboard light source to measure ambient light level and object colour.

Monitor your environment, respond to sharp sounds, detect the colour of objects and more.