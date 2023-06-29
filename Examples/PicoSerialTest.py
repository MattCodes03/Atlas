# This is MicroPython Code designed to run on the Raspberry PI Pico
# It was used to test the serial connection between the Pico Microcontroller and a Raspberry Pi 3

from machine import Pin, UART
from time import sleep
import json
from Receiver import Receiver
from Controllers.DCMotor import DCMotor

rec = Receiver(1, 9600, 'utf-8')
motor = DCMotor(0, 1, 7)

while True:
    command = str(rec)
    if command:
        command = json.loads(command)
        speed, direction = command['args'].split(',')

        if command['command'] == 'MOTOR':
            if direction == 'b':
                motor.move_backward(int(speed))
            elif direction == 'f':
                motor.move_forward(int(speed))
            elif direction == 's':
                motor.stop()
