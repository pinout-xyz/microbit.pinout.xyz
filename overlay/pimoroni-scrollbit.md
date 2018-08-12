<!--
---
name: scroll:bit
type: led
manufacturer: Pimoroni
description: 17x7 pixel LED display
pxt: https://github.com/pimoroni/pxt-scrollbit
python: https://github.com/pimoroni/micropython-scrollbit
buy: https://shop.pimoroni.com/products/scroll-bit
image: 'pimoroni-scrollbit.jpg'
pin:
  P20:
    mode: I2C
  P19:
    mode: I2C
i2c:
  '0x74':
    name: Matrix LED driver
    device: IS31FL3731
-->
The Pimoroni scroll:bit, 17x7 pixels of single-colour, brightness-controlled, message scrolling goodness!