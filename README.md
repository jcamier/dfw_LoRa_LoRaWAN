# DFW Pythoneers Talk on LoRa & LoRaWAN
![](./lora_logo.png) 

GitHub LoRa repo:

https://github.com/Lora-net

![](./lorawan_logo.png)  

https://lora-alliance.org/about-lorawan/

* Please not this material is for learning purposes only and no warranty is provided. Some of the code has MIT licensing 
  which requires disclosure and it's implications
  
## Technical Terms:

* **RPi** - shorthand for Raspberry Pi


* **SBC** - Single Board Computer, like a Raspberry Pi


* **UART** - is a computer hardware device for asynchronous serial communication in which the data format and
  transmission speeds are configurable


* **I2C** - Synchronous Multi-controller/Multi-target Serial Communication Bus
  * The I2C protocol is used to establish communication between two or more IC's (Integrated Circuits)


* **SPI** - Serial Peripheral Interface
  * is a synchronous serial communication or protocol normally found on RPi for two devices to send and receive data
  * I2C on the other hand share a single data wire
  
  Source: https://learn.adafruit.com/circuitpython-basics-i2c-and-spi/spi-devices?gclid=CjwKCAjwsJ6TBhAIEiwAfl4TWIzVniDvAVgEOLEkvDarvc1BUPUY0CubcazydnU9LvjP4zbjciRJyhoCjtkQAvD_BwE


* **Hardware Register** are used in the interface between software and peripherals. Software writes to them to send
  information to the device, and reads them to get information from the device with hardware-related functions. Some
  hardware devices also include registers that are not visible to software, for their internal use.
  
  It involves accessing its memory-mapped I/O address or port-mapped I/O address with a "load" or "store" instruction,
  issued by the processor.
  
  Looking at the datasheets of a chip, you can assign attributes in a class normally as hexadecimal value and have
  methods that use these addresses to perform different actions on your end node device.
  
    Source: https://en.wikipedia.org/wiki/Hardware_register


* **GPIO.BCM** Broadcom chip-specific pin numbers. These pin numbers follow the lower-level numbering system defined by
  the Raspberry Pi's Broadcom-chip brain.
  * If you want to refer to the pins with the numbers represented in circles (i.e 1, 2, 3, …) then you would be referring
    them with the GPIO.BOARD method.

  * But, if you want to refer the pins with the numbers represented in the rectangles around the pins (i.e GPIO 21,
    GPIO 25, …) then in that case you would be referring to GPIO.BCM method


* **CRC** Cyclic redundancy check. Is an error-detecting code commonly used in digital networks and storage devices. 
  Often you will see this in LoRa code to ensure the data was transmitted properly as data loss is not uncommon.
  
  Source: https://en.wikipedia.org/wiki/Cyclic_redundancy_check   


* **RSSI** Received Signal Strength Indicator

  Source: https://www.metageek.com/training/resources/understanding-rssi/  

Example:
![](./gpio_pins_example.png)  

* **Transceiver** - combination of a transmitter/receiver in a single device. Most
  LoRa end nodes and gateways are transceivers i.e. able to both transmit and receive data


* **Modulation** - how analog or digital information is encoded onto a carrier signal
  * Analog:  
    * Amplitude Modulation (AM)
    * Frequency Modulation (FM)
    * Phase Modulation (PM)
  * Digital:
    * Amplitude Shift Keying (ASK)
    * Frequency Shift Keying (FSK)
    * Phase Shift Keying (PSK)
      
![](./digital_modulation.png)  


  Source: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Microwave_and_RF_Design_I_-_Radio_Systems_(Steer)/02%3A_Modulation/2.05%3A_Digital_Modulation
 
    
* The **baud rate** is the rate at which information is transferred in a communication channel. It is commonly used
  when discussing electronics that use serial communication. In the serial port context, "9600 baud" means that the
  serial port is capable of transferring a maximum of *9600 bits per second*.
  
  

  
## What is LoRa?
* LoRa technology is used as wide area network wireless technology. 


* It is a great technology for IoT devices since its architecture is designed for very little power consumption
  (some devices last 10 years on a single battery) and for long ranges several miles.
  
  - Transmission in general of as far as 15 km (9 mi) with clear line of sight or in urban areas is 2 to 3 km (~1+ mi)
   
  - Bluetooth is only good for 30 feet (10 meters) in comparison  



* There are different frequency bands:
  
    - US: (902 to 928 MHz)
    - EU: (863 to 870 MHz)
    - China: (779 to 787 MHz)
    - India 3 channels: (865.0625 MHz, 865.4025 MHz, 865.9850 MHz)
    - Australia: (915 to 928 MHz)
    - Other Asian countries: (920 to 923 MHz or 923 to 925 MHz)
  
    Source: https://devopedia.org/lora


* LoRa is based on Chirp Spread Spectrum (CSS) technology, where chirps (also known as symbols) are the carrier of data.
  The LoRa spread spectrum modulation technique is patented by [Semtech](https://www.semtech.com/)
  

  Source: https://www.thethingsnetwork.org/docs/lorawan/spreading-factors/#:~:text=LoRa%20is%20based%20on%20Chirp,the%20speed%20of%20data%20transmission.
  

* Spreading Factors and Frequencies
![](./lora_data_specs.png)
  Source: Semtech Corporation 2020

* More details on how it is modulated and encoded: 

  https://myriadrf.org/news/lora-modem-limesdr/


* The transmission from end device to gateway is referred as "uplink." 
    

* Transmission from gateway to end device is referred as "downlink"


### Device Classes
* **Class A:** devices sleep most of the time. They listen for downlink messages (from gateway to device) only for a short period after transmitting. If a cloud-hosted application sends a command to this device, a significant delay may take place until the messages is received by the device. Because of that, class A devices are typically battery-powered sensors, having a battery time of up to 10 years.
  

* **Class B:** devices can receive downlink messages in scheduled downlink slots. These devices are typically battery-powered actuators.
  

* **Class C:** almost never sleep and continuously listen for the incoming messages. If a cloud-hosted application sends a command to this device, the message will reach the devices with a low delay. Because of that, these devices are typically mains-powered actuators.


### Hardware Specs:

Datasheets  [Semtech SX1276/77/78/79](https://semtech.my.salesforce.com/sfc/p/#E0000000JelG/a/2R0000001Rc1/QnUuV9TviODKUgt_rpBlPz.EZA_PNK7Rpi8HA5..Sbo)

Datasheets  [Semtech SX1261/2](https://semtech.my.salesforce.com/sfc/p/#E0000000JelG/a/2R000000Un7F/yT.fKdAr9ZAo3cJLc4F2cBdUsMftpT2vsOICP7NmvMo)


## What is LoRaWAN ?

LoRa  & LoRaWAN Topology

![](./lorwan_topology.png)


There are two protocols:



* **OTAA** Over-The-Air-Activation
  - The most secure and recommended activation method for end devices. Devices perform a join procedure with the network, during which a dynamic device address is assigned and security keys are negotiated with the device.


* **ABP** Activation By Personalization
  - It requires hardcoding the device address as well as the security keys in the device. ABP is less secure than OTAA and also has the downside that devices can not switch network providers without manually changing keys in the device.


### OTAA message flow in LoRaWAN 1.0
![](./otaa-1.0.png)

Source: https://www.thethingsnetwork.org/docs/lorawan/end-device-activation/


AppEUI - 8 bytes

DevEUI - 8 bytes

DevNonce - 2 bytes

### LoRaWAN network layers
![](./lorawan_network_layers.png)
source: https://docs.arduino.cc/learn/communication/lorawan-101

### Finding a LoRaWAN Gateway near you:
https://www.thethingsnetwork.org/map

### Adding devices to The Things Network (TTN)


1. First create a community account with TTN, it's free


2. Go to the Applications section and create some generic name
   - TTN will let you know if it is already used
  

3. Click on the `+ Add end device button` to get **DevEUI, AppEUI and AppKey**
   - You can try to find From The LoRaWAN Device Repository, I did not find raspberry pi in the device repository,
    here is how you do it manually:
   - Click on `Manually`
   - Frequency plan: United States 902-928 MHz, FSB2
   - LoRaWAN Specifications 1.0.1
   - DevEUI (click on Generate, let TTN to create this for you)
   - AppEUI (click fill with zeros)
   - AppKey (click on Generate, let TTN to create this for you)
   - End device ID (will be created by TTN, leave blank)
   - `Register end device`
    

Not yet completed (4)...to be updated
4. Send an Uplink Payload, special thanks to mobilefish.com - **Robert Lei**:
    
    - Inspiration: 
      
        - https://www.youtube.com/watch?v=k5-1o8WifQM
      
        - https://www.mobilefish.com/download/lora/lora_part58.pdf
    
    - Use a text to hexadecimal translator:

        https://www.rapidtables.com/convert/number/ascii-to-hex.html

  
![](./the_things_lorawan_manual_end_device.png)

## *Project Architecture:*


    source: https://www.techplayon.com/lora-technology-benefits-application/

<hr>

## Eric Livesay

*Data Engineer*
https://www.linkedin.com/in/ericlivesay

    Hardware: 
        1. Gowoops SX1276 LoRa Radio Wireless 915Mhz UART Serial Module
        2. Raspberry Pi Pico

    Project setup:

    The idea is to Setup Serial (UART) communications between two lora modules. The example here is using Arduino,
    I plan on using two Raspberry Pi Pico's:
    
    https://osoyoo.com/2018/07/26/osoyoo-lora-tutorial-how-to-use-the-uart-lora-module-with-arduino/

## Project Setup:
This board uses the SX1276 chipset, but instead of requiring you to use the SPI bus, they take care of that all for you and you simply need to use uart.write() and uart.read() once you are on the right frequency. It has a set of commands you can give it through the uart bus.

![](ebyte_e32.png))

I wanted to run my experiment of connecting to another Lora module using a Raspberry Pi. However, the Pis are all sold out in most countries! There is a huge backlog. So I settled for a a Pi Pico. The Raspberry Pi Pico is a microcontroller board that has many IO pins and supports the same buses and connections as a Raspberry Pi, except it is only a microcontroller, not a computer. However, it has enough resources to run Micropython, so that is what I used for this: ![](pi_pico.png)

After I got my Pi and my module I connected it up.

Here is the diagram for how to connect it:

![](pico_ebyte_pinout.png)

This is image taken from another similar board, which behaves almost exactly the same which is made by that manufacturer, it just works on a different frequency. Here is the write up on how to connect it: [https://www.iottrends.tech/blog/how-to-interface-lora-sensor-e32-433t20dt-with-pico/](https://www.iottrends.tech/blog/how-to-interface-lora-sensor-e32-433t20dt-with-pico/)

The connection is really simple- Connect the RX on the Uart ports on the Pi Pico to the TX on the E32 board, and vice versa for the TX port (connect to the RX on the e32 board).

Once I had it connected I wanted to try it out. Here is where I realized that I had an issue :) I only had one board! I was thinking that I would try connecting my board to one of Javques Lora modules. However, in reality, when you are testing things out, and its you aren&#39;t close by, that was a silly mistake. So what I did was try to get it to work and then tried to use my RTLSDR32 usb software defined radio dongle and CuvbeSDR software to see if I could pick up the signal. Unfortunately I wasn&#39;t able to find the signal as there is a lot involved in demodulating it and there is a lot of use on the frequency it sends at. By default, this device uses 868 MHz. I tried it on the default frequency first.

Since I had never used a Pi Pico, I tried to use the easiest thing I could to program it and debug it. I found Thonny to be very easy to use to hook up a Pi Pico and put the firmware on it. RTLSDR32 usb software defined radio dongle and CuvbeSDR software to see if I could pick up the signal. Unfortunately I wasn&#39;t able to find the signal as there is a lot involved in demodulating it and there is a lot of use on the frequency it sends at. By default, this device uses 868 MHz. I tried it on the default frequency first.

Since I had never used a Pi Pico, I tried to use the easiest thing I could to program it and debug it. I found Thonny to be very easy to use to hook up a Pi Pico and put the firmware on it.

[https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/2](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/2)

![](thonny.png)

You plug in the Raspberry PI to your computer via the micro usb cable with Thonny open and you might need to hold down the boot select button on the PI Pico.

Then you are prompted to put the firmware on it and it installs MicroPython. When you save programs, you can choose to save to the Pi Pico.

Here is one of my programs I tested with, that got the device sending (as far as I can tell because I monitored the AUX pin, and that showed the change in values prior to and during transmission (and after) the the manufacturer said indicated sending.

	from machine import UART
	from machine import Pin, Timer
	led = Pin(25, Pin.OUT)
	aux = Pin(22, Pin.IN)
	m0 = Pin(20, Pin.OUT)
	m1 = Pin(21, Pin.OUT)
	import micropython
	import time
	import sys
	micropython.alloc_emergency_exception_buf(100)

	uart = UART(0, 9600) # init with given baudrate

	led.value(1)
	m0.value(1)
	m1.value(1)

        def aux_pin_change(p):
            led.toggle()
            print(aux.value())

        aux.irq(trigger=Pin.IRQ\_RISING | Pin.IRQ\_FALLING, handler=aux\_pin\_change)

	a = 1

	while a == 1:
	    print(aux.value())
	    uart.write(&#39;hello there from eric test\0&#39;)
	    time.sleep(.04)

The result showed that the AUX pin would change as expected right when I sent the data. My led blinked and the value shown toggled. So I was able to tell with pretty good certainty that it was sending. I have not been able to get the other module to check if I can receive yet. Hopefully in the next week or two.

After realizing that I only had one device, I still wanted to try to communicate with Jacques LoraWan gateway that he had set up. Jacque did some research and found out how he can hook up his gateway to a things network MQTT broker. So he got that hoked up. The next step was for me to add an ESP-01 wifi module onto my device. I was working on making it work but did not have enough time to get it up and running yet. So how it would work would be:

1. A Lora module in the field somewhere would communicate with this other Lora module that also has wifi
2. The module with wifi would send the message and receive the messages from the MQTT broker
3. The MQTT broker sends and receives from the gateway
<hr>

## Jack Camier 

*Full Stack Software Engineer, IoT Enthusiast*
https://www.linkedin.com/in/jacques-camier/


## Project setup: 
### Adafruit LoRa Radio Bonnet for Raspberry Pi

    Hardware: Adafruit LoRa Radio Bonnet with OLED - RFM95W @ 915MHz - RadioFruit

    * https://www.adafruit.com/product/4074

![](./adafruit_lora_rfm95w_bonnet.jpeg)

1. Configure I2C
  

`sudo apt-get install -y python-smbus`

`sudo apt-get install -y i2c-tools`

* sudo raspi-config
    * Interfacing Options or Advanced (Older versions)
    * then I2C and enable it
  

`sudo reboot`

`sudo ls /dev/i2c*`


2. Configure SPI


* sudo raspi-config
    * Interfacing Options or Advanced (Older versions)
    * then SPI and enable it
  

`sudo reboot`

`ls -l /dev/spidev*`

You should see two devices listed for each SPI bus

Now run this command:

`ls /dev/i2c* /dev/spi*`

You should see a response like this:

`/dev/i2c-1 /dev/spidev0.0 /dev/spidev0.1`

3. Install CircuitPython on RPi (requires Python 3.7 or later)

Source: https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi
   

`sudo apt-get update`

`sudo apt-get upgrade`

`sudo apt-get install python3-pip`

`sudo pip3 install --upgrade setuptools`
  * setuptools is a package used by many other packages to handle their installation from source code. It is 
    used extensively for non-pure-Python packages, which need some compilation/installation step before being usable
    (like packages containing extensions written in C)

`cd ~`

`sudo pip3 install --upgrade adafruit-python-shell`

`wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py`

`sudo python3 raspi-blinka.py`
  * This will update your Raspberry OS to use Python3 as default
  * You really should as Python2 is now deprecated
  :smirk:

Yes to proceed, and yes to reboot

`sudo nano blinkatest.py`
  * copy over file blinkatest.py from repo

`python3 blinkatest.py`

You should see the following output if all things are working:

```
Hello blinka!
Digital IO ok!
I2C ok!
SPI ok!
done!
```

### Getting the Adafruit LoRa Radio Bonnet to work with RPi

Source: https://learn.adafruit.com/lora-and-lorawan-radio-for-raspberry-pi?view=all

`sudo pip3 install adafruit-circuitpython-ssd1306`

`sudo pip3 install adafruit-circuitpython-framebuf`

`sudo pip3 install adafruit-circuitpython-rfm9x`

You'll also want to download the font file, font5x8.bin

`wget https://github.com/adafruit/Adafruit_CircuitPython_framebuf/raw/main/examples/font5x8.bin`

`sudo nano rfm9x_check.py`
* copy over file rfm9x_check.py from repo

`python3 rfm9x_check.py`

If the RFM9x/RFM69 is detected, the OLED will display Detected!!!
:crossed_fingers:


* You can now press the buttons!!!
:star_struck:

### Have Two Adafruit LoRa Radio Bonnets talk to each other with RPi - (This requires 2 Adafruit bonnets and RPis!!!)

`sudo nano radio_rfm9x.py`
* copy over file radio_rfm9x.py from repo

`python3 radio_rfm9x.py`
  
* You can now press the buttons on one LoRa device and the second one will display which one was pressed

### Have One Adafruit LoRa Radio Bonnets send Hello World to the other one - (This requires 2 Adafruit bonnets and RPis)

`sudo nano rfm9x_rpi_simpletest.py`
* copy over file rfm9x_rpi_simpletest.py from repo

Run `python3 rfm9x_rpi_simpletest.py` on each of the RPis at the same time. One of them will send Hello World to the 
other using LoRa!

* more cool samples scripts can be found at:
https://github.com/adafruit/Adafruit_CircuitPython_RFM9x/tree/main/examples

(To be continued...not yet completed...)
### LoRa part II

    Hardware: SX1262 LoRa HAT Covers 915MHz Frequency Band with Spread Spectrum Modulation

    * https://www.amazon.com/gp/product/B07VS47RQZ/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1

![](./SX1268_LoRa_HAT.jpeg)

Enable Serial Console (UART) on Raspberry Pi

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

Arduino Guide to LoRa and LoRaWAN

https://docs.arduino.cc/learn/communication/lorawan-101

What is LoRa and LoRaWAN Fundamentals (60+ minutes):

https://www.youtube.com/watch?v=ZsVhYiX4_6o

The Things Network - collaborative IoT ecosystem

https://www.thethingsnetwork.org/

https://github.com/TheThingsNetwork

Notable Python Lora Projects:

https://github.com/chandrawi/LoRaRF-Python

https://github.com/rpsreal/pySX127x

https://github.com/wdomski/LoRa-RaspberryPi

https://gist.github.com/garystafford/bd5e781c8a1097dbac8a447abe18d0cd#file-rasppi_lora_receiver-py

https://github.com/pycom/pycom-libraries/blob/f24b3fbbbfeb3a681cb92e049db9e25db2a6e7c6/examples/lorawan-regional-examples/main_US915.py


What are Hexadecimals (i.e. 0xC0): 

https://en.wikipedia.org/wiki/Hexadecimal


        
