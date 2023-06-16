from machine import Pin, PWM


class Motor:
    def __init__(self, in1, in2, en):
        self.in1 = in1
        self.in2 = in2
        self.en = en

        self.input1 = Pin(self.in1, Pin.OUT)
        self.input2 = Pin(self.in2, Pin.OUT)

        self.speed = PWM(Pin(self.en, Pin.OUT), frequency=1000, duty_u16=8129)

    def move_forward(self):
        self.input1.value(1)
        self.input2.value(0)

    def move_backward(self):
        self.input1.value(0)
        self.input2.value(1)
