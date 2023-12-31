import json
from Atlas import *

serial = Serial('/dev/serial0')

while True:
    speed = input("What Speed: ")
    direction = input("What Direction: ")

    command = Command('MOTOR', f'{speed},{direction}')

    serial.send(json.dumps(command()))
