<!--
---
name: weather:bit
type: sensor
manufacturer: SparkFun
description: Turn the micro:bit into a weather station
pxt: https://github.com/sparkfun/pxt-weather-bit
buy: https://shop.pimoroni.com/products/sparkfun-weather-bit
image: 'sparkfun-weatherbit.jpg'
pin:
  P20:
    mode: I2C
  P19:
    mode: I2C
  P0:
    mode: analog
    name: Soil Moisture
  P1:
    name: Wind Direction
  P2:
    name: Rain Inches
  P8:
    name: Wind Speed
  P12:
    name: Temperature
  P14:
    mode: UART
    name: RX
  P15:
    mode: UART
    name: TX
  P16:
    mode: digital
    name: Soil Moisture Power
i2c:
  '0x59':
    name: Temperature, Pressure, Humidity sensor
    device: BME280
-->
The SparkFun weather:bit is a fully loaded “carrier” board for the micro:bit that, when combined with the micro:bit, provides you with a fully functional weather station. With the weather:bit you will have access to barometric pressure, relative humidity and temperature readings. There are also connections on this carrier board to optional sensors such as wind speed, direction, rain gauge and soil readings! The micro:bit has a lot of features and a lot of potential for weather data collection.