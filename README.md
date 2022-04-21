# DFW Pythoneers Talk on LoRa & LoRaWAN

## *Project Architecture:*

LoRa  & LoRaWAN Topology

![](./lorwan_topology.png)

    source: https://www.techplayon.com/lora-technology-benefits-application/

<hr>

## Eric Livesay

*Data Engineer*
https://www.linkedin.com/in/ericlivesay

    Hardware: 
        1. Gowoops SX1276 LoRa Radio Wireless 915Mhz UART Serial Module
        2. Raspberry Pi Pico

    Project setup:

    The idea is to Setup Serial (UART) communications between two e32-915TDO lora modules. The example here is using Arduino,
    I plan on using two Raspberry Pi Pico's:
    
    https://osoyoo.com/2018/07/26/osoyoo-lora-tutorial-how-to-use-the-uart-lora-module-with-arduino/

<hr>

## Jack Camier 

*Full Stack Software Engineer, IoT Enthusiast*
https://www.linkedin.com/in/jacques-camier/

    Hardware: SX1262 LoRa HAT Covers 915MHz Frequency Band with Spread Spectrum Modulation

    * https://www.amazon.com/gp/product/B07VS47RQZ/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1

![](./SX1268_LoRa_HAT.jpeg)

    Project setup: 

        1. Enable Serial Console (UART) on Raspberry Pi

            https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/enabling-serial-console
            
            you can run `check_serial.py` found in repo to confirm it is enabled
            
            or

            dmesg | grep tty

            (dmesg - print or control the kernel ring buffer)

            The kernel ring buffer is a data structure that records messages related to the operation of the kernel.
            A ring buffer is a special kind of buffer that is always a constant size, removing the oldest messages when
            new messages are received.
        

        Resources for project:

            https://www.waveshare.com/wiki/SX1262_915M_LoRa_HAT

            https://learn.adafruit.com/lora-and-lorawan-radio-for-raspberry-pi/rfm9x-raspberry-pi-setup

<hr>

## General Resources:

What is LoRa and LoRaWAN Fundamentals (60+ minutes):

https://www.youtube.com/watch?v=ZsVhYiX4_6o

What are Hexadecimals (i.e. 0xC0): 

https://en.wikipedia.org/wiki/Hexadecimal


        
