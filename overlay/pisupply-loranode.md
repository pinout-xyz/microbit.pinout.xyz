<!--
---
name: IoT micro:bit LoRa Node
type: radio
manufacturer: Pi Supply
description: Our IoT micro:bit LoRa Node allows you to create an inexpensive LoRa node.
pxt: https://github.com/PiSupply/pxt-iot-lora-node/
buy: https://uk.pi-supply.com/products/iot-micro-bit-lora-node
image: 'pisupply-loranode.jpg'
pin:
  P14:
    name: TX
    mode: UART
  P15:
    name: RX
    mode: UART
  P16:
    name: Reset
    mode: digital
  P20:
    mode: I2C
  P19:
    mode: I2C
  i2c:
    '0x42':
      name: Pi Supply I2C GPS Module
      device: GPS
-->
Our IoT micro:bit LoRa Node allows you to create an inexpensive LoRa node, compatible with The Things Network, in conjunction with a BBC micro:bit or other single board computers.

This board allows quicker prototyping as it has the LoRa stack on the chip. Add sensors, buttons and more to complete your LoRa network!

The IoT micro:bit LoRa Node uses the RAKWireless RAK811 LoRa node module which is based on Semtech SX1276 LoRa technology.

Compatible with the upcoming GPS Module.
