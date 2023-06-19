import serial


class Serial:
    __terminator = '\n'.encode('utf-8')

    def __init__(self, serial_line, baudrate=19600, timeout=5):
        self.serial = serial.Serial(
            serial_line, baudrate, timeout=timeout)

    def send(self, signal):
        print(f'Sending Signal: {signal}')
        signal = signal + '\n'
        self.serial.write(bytes(signal, 'utf-8'))

    def receive(self):
        line = self.serial.read_until(self.__terminator)

        return line.decode('utf-8').strip()

    def close(self):
        self.serial.close()
