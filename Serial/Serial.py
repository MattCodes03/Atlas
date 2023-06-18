import serial


class Serial:
    __terminator = '/r'.encode('utf-8')

    def __init__(self, serial_line, baudrate=115200, timeout=100):
        self.serial = serial.Serial(
            serial_line, baudrate, serial.EIGHTBITS, timeout=timeout)

    def send(self, signal):
        line = '%s\r\f' % signal
        self.serial.write(line.encode('utf-8'))

    def receive(self):
        line = self.serial.read_until(self.__terminator)

        return line.decode('utf-8').strip()

    def close(self):
        self.serial.close()
