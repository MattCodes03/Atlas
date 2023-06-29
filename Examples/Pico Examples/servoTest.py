from machine import Pin, PWM
import time


class Servo:
    __servo_pwm_frequency = 750
    __min_u16_duty = 750
    __max_u16_duty = 1023
    min_angle = 0
    max_angle = 180
    current_angle = 0.001

    def __init__(self, pin):
        self.__setup(pin)

    def move(self, angle):
        angle = round(angle, 2)

        # If servo is already rotated to the angle then we don't need to rotate it anymore
        if (angle == self.current_angle):
            return

        self.current_angle = angle

        # Calculate new duty cycle and move the servo
        duty_u16 = self.__angle_to_u16_duty(angle)
        self.__motor.duty_u16(duty_u16)

    def stop(self):
        self.__motor.duty_u16(0)

    # Will Calculate a duty cycle value based on an angle
    def __angle_to_u16_duty(self, angle):
        return int((angle - self.min_angle) * self.__angle_conversion_factor) + self.__min_u16_duty

    def __setup(self, pin):
        self.current_angle = -0.001
        self.__angle_conversion_factor = (
            self.__max_u16_duty - self.__min_u16_duty) / (self.max_angle - self.min_angle)

        self.__motor = PWM(Pin(pin, Pin.OUT))
        self.__motor.freq(self.__servo_pwm_frequency)


servo = Servo(22)

while True:
    print("Turn left ...")
    for i in range(0, 180, 10):
        servo.move(i)
        time.sleep(0.05)
    print("Turn right ...")
    for i in range(180, 0, -10):
        servo.move(i)
        time.sleep(0.05)

    servo.stop()
