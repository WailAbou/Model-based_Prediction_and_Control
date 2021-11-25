from random import choice
from typing import List

from actions import Action
from maze import Maze
from maze_cell import MazeCell


class Policy:
    def __init__(self, value_function):
        self.value_function = value_function

    def get_actions(self, maze_cells: List[List[MazeCell]]) -> List[Action]:
        actions = [[], [], [], []]
        for row, maze_row in enumerate(maze_cells):
            for maze_cell in maze_row:
                neighbours = Maze.get_neighbouring_cells(maze_cells, maze_cell)
                action = self.value_function(neighbours)
                actions[row].append(None if maze_cell.finish else action)
        return actions

    @staticmethod
    def greedy(neighbours) -> Action:
        max_value, chosen = 0, None
        for neighbour, action in neighbours:
            if neighbour.total > max_value:
                max_value = neighbour.total
                chosen = action
        return chosen

    @staticmethod
    def random(neighbours) -> Action:
        return choice(neighbours)[1]
