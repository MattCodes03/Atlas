from Serial import Serial

serial = Serial('/dev/serial0', 9600)

while True:
    sig = input("Signal: ")
    serial.send(sig)
