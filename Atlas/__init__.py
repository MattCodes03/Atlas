# NOTE: When running locally use pip install -e .


from sys import platform
if platform == "linux" or platform == "linux2" or platform == "win32":
    from Atlas.Serial.Command import Command
    from Atlas.Serial.SerialConnection import Serial
    from Atlas.Controllers.DCMotor import FORWARD, BACKWARD
else:
    from Atlas.Controllers.Servo import Servo
    from Atlas.Controllers.LED import LED
    from Atlas.Controllers.DCMotor import DCMotor, FORWARD, BACKWARD
    from Atlas.Serial.Receiver import Receiver


__all__ = ["Serial", "Command", "Receiver", "DCMotor",
           "LED", "Servo", "FORWARD", "BACKWARD"]
