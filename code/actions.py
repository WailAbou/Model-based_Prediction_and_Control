from enum import Enum

class Action(Enum):
    UP = '↑'
    RIGHT = '→'
    DOWN = '↓'
    LEFT = '←'

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.value