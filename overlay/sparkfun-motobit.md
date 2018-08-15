<!--
---
name: moto:bit
type: motor
manufacturer: SparkFun
description: turn the micro:bit into a robot
pxt: https://github.com/sparkfun/pxt-moto-bit
buy: https://shop.pimoroni.com/products/sparkfun-moto-bit
image: 'sparkfun-motobit.jpg'
pin:
  P20:
    mode: I2C
  P19:
    mode: I2C
  P15:
    mode: digital
    name: Servo Motor
  P16:
    mode: digital
    name: Servo Motor
i2c:
  '0x59':
    name: Motor Driver
    device: DRV8835
-->
The SparkFun moto:bit is a fully loaded “carrier” board for the micro:bit that, when combined with the micro:bit, provides you with a fully functional robotics platform. The moto:bit offers a simple, beginner-friendly robotics controller capable of operating a basic robotics chassis. Onboard each moto:bit are multiple I/O pins capable of hooking up servos, sensors and other circuits. At the flip of the switch you can get your micro:bit moving!