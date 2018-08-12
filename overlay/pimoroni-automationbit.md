<!--
---
name: automation:bit
type: sensor
manufacturer: Pimoroni
description: 24V tolerant IO, analog inputs and a relay
pxt: https://github.com/pimoroni/pxt-automationbit
python: https://github.com/pimoroni/micropython-automationbit
buy: https://shop.pimoroni.com/products/automation-bit
image: 'pimoroni-automationbit.jpg'
pin:
  P14:
    name: Output One
    mode: digital
  P15:
    name: Output Two
    mode: digital
  P16:
    name: Relay
    mode: digital
  P8:
    name: Input One
    mode: digital
  P13:
    name: Input Two
    mode: digital
  P2:
    name: Analog One
    mode: analog
  P1:
    name: Analog Two
    mode: analog
  P0:
    name: Analog Three
    mode: analog
-->
# Pimoroni enviro:bit

The Pimoroni automation:bit provides 24V-tolerant digital inputs and outputs, 24V-tolerant analog channels and a relay for interfacing your low-voltage micro:bit with high-voltage electronics such as central heating controlers.

* Three digital outputs (sinking) via a darlington driver array
* Three digital inputs, protected with inline resistors and diodes
* Three analog inputs, protected with voltage dividers and diodes
* One relay