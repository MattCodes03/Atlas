# This is a receiever class for the UART serial communication protocol
# NOTE: This will only work with Micropython as it makes use of the UART class of the machine library
# https://docs.micropython.org/en/latest/library/machine.UART.html

from machine import UART


class Receiver:
    def __init__(self, id: int, baudrate: int, encoding='utf-8'):
        self.__setup(id, baudrate)
        self.encoding = encoding

    def __str__(self) -> str:
        val = self.uart.read()
        if val:
            return val.decode(self.encoding).strip()

        return ""

    def __setup(self, id, baudrate):
        self.uart = UART(id, baudrate)
