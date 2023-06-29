from Serial.UART import UART
from Serial.Command import Command
import Controllers.DCMotor as dcm
import json

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
