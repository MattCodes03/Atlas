# NOTE: When passing multiple arguments e.g Speed and Direction of a DC Motor, sperate the values with a comma

class Command:
    def __init__(self, signal: str, args: str):
        self.__setup(signal, args)

    def __setup(self, signal, args):
        self.signal = signal
        self.args = args
