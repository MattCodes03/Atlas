import json
import Controllers.DCMotor as dcm
from Serial.Command import Command
from Serial.UART import UART


serial = UART('/dev/serial0')

while True:
    speed = input("What Speed: ")
    direction = input("What Direction: ")

    if direction == 'f':
        direction = dcm.FORWARD
    else:
        direction = dcm.BACKWARD

    command = Command('MOTOR', f'{speed},{direction}')

    serial.send(json.dumps(command()))
