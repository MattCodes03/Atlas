# NOTE: When passing multiple arguments e.g Speed and Direction of a DC Motor, sperate the values with a comma

from typing import Any


class Command:
    def __init__(self, signal: str, args: str):
        self.__setup(signal, args)

    def __call__(self) -> Any:
        return self.command

    def __setup(self, signal, args):
        self.command = {'command': signal, 'args': args}
