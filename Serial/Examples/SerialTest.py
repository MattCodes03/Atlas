from Serial import Serial
from Command import Command
import json

serial = Serial('/dev/serial0')

while True:
    speed = input("What Speed: ")
    direction = input("What Direction: ")

    command = Command('MOTOR', f'{speed},{direction}')

    serial.send(str(json.dumps(command.command)))
