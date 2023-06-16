from machine import Pin, PWM


class Motor:
    __min_u16_duty = 750
    __max_u16_duty = 1023

    def __init__(self, in1, in2, en):
        self.__setup(in1, in2, en)

    def move_forward(self, speed):
        self.enable_pin.duty_u16(self.__calculate_u16_duty(speed))
        self.input1.value(1)
        self.input2.value(0)

    def move_backward(self, speed):
        self.enable_pin.duty_u16(self.__calculate_u16_duty(speed))
        self.input1.value(0)
        self.input2.value(1)

    def __reset(self):
        self.input1.value(0)
        self.input2.value(0)
        self.enable_pin.duty_u16(0)

    def __calculate_u16_duty(self, speed):
        if (speed <= 0 or speed > 100):
            return 0

        return int(self.__min_u16_duty + (self.__max_u16_duty - self.__min_u16_duty)*(speed-1)/(100-1))

    def __setup(self, in1, in2, en):
        self.input1 = Pin(self.in1, Pin.OUT)
        self.input2 = Pin(self.in2, Pin.OUT)
        self.enable_pin = Pin(self.en, Pin.OUT)

        self.__reset()
