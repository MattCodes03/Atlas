# This is MicroPython Code designed to run on the Raspberry PI Pico
# It was used to test the serial connection between the Pico Microcontroller and a Raspberry Pi 3

from machine import Pin, UART
from time import sleep

led = Pin("LED", Pin.OUT)

# Turn the LED on


def on():
    led.value(1)

# Turn the LED off


def off():
    led.value(0)


uart = UART(1, 9600)


while True:
    val = uart.read()
    if val:
        val = val.decode('utf-8').strip()
        print(val)

    if (val == 'on'):
        on()
    elif (val == 'off'):
        off()

    sleep(1)
