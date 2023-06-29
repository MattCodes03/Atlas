from machine import Pin, UART, PWM
from time import sleep
import json


from machine import Pin, PWM


class DCMotor:
    __pwm_frequency: int = 2000
    __min_u16_duty: int = 750
    __max_u16_duty: int = 1023

    # Directions
    FORWARD = 0
    BACKWARD = 1

    def __init__(self, in1: int, in2: int, en: int):
        self.__setup(in1, in2, en)

    def move(self, speed, direction):
        if direction == self.FORWARD:
            print("Forward...")
            self.input1.high()
            self.input2.low()
            self.enable_pin.duty_u16(self.__calculate_u16_duty(speed))

        elif direction == self.BACKWARD:
            print("Backward...")
            self.input1.low()
            self.input2.high()
            self.enable_pin.duty_u16(self.__calculate_u16_duty(speed))

    def stop(self):
        print("Stopped...")
        self.__reset()

    def __reset(self):
        self.input1.low()
        self.input2.low()
        self.enable_pin.duty_u16(0)

    def __calculate_u16_duty(self, speed) -> int:
        if (speed <= 0 or speed > 100):
            return 0

        return int(self.__min_u16_duty + (self.__max_u16_duty - self.__min_u16_duty)*(speed/100*65536))

    def __setup(self, in1, in2, en):
        self.input1 = Pin(in1, Pin.OUT)
        self.input2 = Pin(in2, Pin.OUT)

        self.enable_pin = PWM(Pin(en, Pin.OUT))
        self.enable_pin.freq(self.__pwm_frequency)

        self.__reset()


class Receiver:
    def __init__(self, id: int, baudrate: int, encoding: str):
        self.__setup(id, baudrate)
        self.encoding = encoding

    def __str__(self) -> str:
        val = self.uart.read()
        if val:
            return val.decode(self.encoding).strip()

        return ""

    def __setup(self, id, baudrate):
        self.uart = UART(id, baudrate)


rec = Receiver(1, 9600, 'utf-8')
motor = DCMotor(0, 1, 7)

while True:
    command = str(rec)
    if command:
        command = json.loads(command)
        speed, direction = command['args'].split(',')

        if command['command'] == 'MOTOR':
            if direction == 'b':
                motor.move(int(speed), direction)
            elif direction == 'f':
                motor.move(int(speed), direction)
            elif direction == 's':
                motor.stop()
