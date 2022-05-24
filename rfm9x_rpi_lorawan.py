# GitHub repo: https://github.com/adafruit/Adafruit_CircuitPython_RFM9x
# Author: Jacques Camier

import os
import sys
import logging
import json
import csv
import random
from datetime import datetime

import board
import busio
import digitalio
import adafruit_rfm9x
import paho.mqtt.client as mqtt


# Procedure to get the USER, PASSWORD, PUBLIC_TLS_ADDRESS and PUBLIC_TLS_ADDRESS_PORT:
# 1. Login to The Things Stack Community Edition console
#    https://console.cloud.thethings.network/
# 2. Select Go to applications
# 3. Select your application
# 4. On the left hand side menu, select Integrations | MQTT
# 5. See Connection credentials
# 6. For the password press button: Generate new API key
#    Each time you press this button a new password is generated!
#    The password looks like:
#    NNSXS.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#
USER = "XXXXXXXXXX@ttn"
PASSWORD = "NNSXS.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
PUBLIC_TLS_ADDRESS = "nam1.cloud.thethings.network"
PUBLIC_TLS_ADDRESS_PORT = 8883
DEVICE_ID = "eui-XXXXXXXXXXXXXX"
ALL_DEVICES = True

# Define radio parameters.
RADIO_FREQ_MHZ = 915.0  # Frequency of the radio in Mhz. Must match your country

# Define pins connected to the chip:
CS = digitalio.DigitalInOut(board.CE1)
RESET = digitalio.DigitalInOut(board.D25)

# Initialize SPI bus.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialize RFM radio
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)


# You can adjust the transmit power (in dB).  The default is 13 dB but
rfm9x.tx_power = 23

# Send a packet.  Note you can only send a packet up to 252 bytes in length.
# This is a limitation of the radio packet size, so if you need to send larger
# amounts of data you will need to break it into smaller send calls.  Each send
# call will wait for the previous one to finish before continuing.
rfm9x.send(bytes("Hello world!\r\n", "utf-8"))
print("Sent Hello World message!")


