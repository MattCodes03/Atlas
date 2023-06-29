from machine import Pin, PWM
import time  # importing time for delay


class Motor:
    __pwm_frequency = 2000
    __min_u16_duty = 750
    __max_u16_duty = 1023

    def __init__(self, in1, in2, en):
        self.__setup(in1, in2, en)

    def move_forward(self, speed):
        print("Forward...")
        self.input1.high()
        self.input2.low()
        self.enable_pin.duty_u16(self.__calculate_u16_duty(speed))

    def move_backward(self, speed):
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

    def __calculate_u16_duty(self, speed):
        if (speed <= 0 or speed > 100):
            return 0

        return int(self.__min_u16_duty + (self.__max_u16_duty - self.__min_u16_duty)*(speed/100*65536))

    def __setup(self, in1, in2, en):
        self.input1 = Pin(in1, Pin.OUT)
        self.input2 = Pin(in2, Pin.OUT)

        self.enable_pin = PWM(Pin(en, Pin.OUT))
        self.enable_pin.freq(self.__pwm_frequency)

        self.__reset()


motor1 = Motor(0, 1, 7)
motor2 = Motor(2, 3, 6)


motor1.stop()
motor2.stop()

# while True:
#     motor1.move_forward(50)
#     motor2.move_forward(50)

#     time.sleep(2)

#     motor1.stop()
#     motor2.stop()

#     time.sleep(2)

#     motor1.move_backward(50)
#     motor2.move_backward(50)

#     time.sleep(2)

#     motor1.stop()
#     motor2.stop()
