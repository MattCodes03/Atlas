import json
from Atlas import Serial, Command, FORWARD, BACKWARD


serial = Serial('/dev/serial0')

while True:
    speed = input("What Speed: ")
    direction = input("What Direction: ")

    if direction == 'f':
        direction = FORWARD
    else:
        direction = BACKWARD

    command = Command('MOTOR', f'{speed},{direction}')

    serial.send(json.dumps(command()))
