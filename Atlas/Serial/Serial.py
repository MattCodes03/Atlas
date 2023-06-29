import serial


class Serial:
    __terminator = '\n'.encode('utf-8')

    def __init__(self, serial_line: str, baudrate=9600, timeout=5, encoding='utf-8'):
        self.serial = serial.Serial(
            serial_line, baudrate, timeout=timeout)
        self.encoding = encoding

    def send(self, signal):
        print(f'Sending Signal: {signal}')
        signal = signal + '\n'
        self.serial.write(bytes(signal, self.encoding))

    def receive(self) -> str:
        line = self.serial.read_until(self.__terminator)

        return line.decode(self.encoding).strip()

    def close(self):
        self.serial.close()
