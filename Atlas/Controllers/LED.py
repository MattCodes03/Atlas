from machine import Pin


class LED:
    __led_state = 0

    def __init__(self, pin='LED'):
        self.__setup(pin)

    def on(self):
        self.led.value(1)

    def off(self):
        self.led.value(0)

    def toggle(self):
        self.led.value(self.__led_state)
        self.__led_state = not self.__led_state

    def __setup(self, pin):
        self.led = Pin(pin, Pin.OUT)
        self.off()
