from typing import Callable


def choose(effects: list[Callable]):
    choice = int(input())
    return effects[choice]()
