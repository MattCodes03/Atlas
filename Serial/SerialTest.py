from Serial import Serial

serial = Serial('/dev/ttyS0', 9600)
serial.send('on')
serial.close()
