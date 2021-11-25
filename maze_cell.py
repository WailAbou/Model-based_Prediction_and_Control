from dataclasses import dataclass
from typing import List


@dataclass
class MazeCell:
    x: int = -1
    y: int = -1
    reward: int = 0
    value: int = 0
    finish: bool = False

    @property
    def total(self):
        return self.reward + self.value

    def update(self, new_value):
        self.value = new_value

    def calculate_values(self, neighbours: List['MazeCell'], discount: float):
        new_values = [self.bellman_equation(neighbour, discount) for neighbour in neighbours]
        return self.value if self.finish else max(new_values)

    def bellman_equation(self, neighbour: 'MazeCell', discount: float):
        return neighbour.reward + (discount * neighbour.value)

    def __str__(self) -> str:
        return f"R:{self.reward:.2f} & V:{self.value:.2f}"
