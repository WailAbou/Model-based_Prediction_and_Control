from random import choice
from typing import List, Tuple
from actions import Action
from maze import Maze
from maze_cell import MazeCell


class Policy:
    def __init__(self, value_function):
        self.value_function = value_function

    def get_actions(self, maze_cells: List[List[MazeCell]]) -> List[Action]:
        get_action = lambda maze_cell: self.get_action(maze_cells, maze_cell)
        actions = [list(map(get_action, maze_row)) for maze_row in maze_cells]
        return actions

    def get_action(self, maze_cells, maze_cell):
        info_pairs = Maze.get_neighbouring_info(maze_cells, maze_cell)
        action = self.value_function(info_pairs)
        return None if maze_cell.finish else action

    @staticmethod
    def greedy(info_pairs: Tuple[MazeCell, Action]) -> Action:
        totals = list(map(lambda info_pair: info_pair[0].total, info_pairs))
        max_value = max(totals)
        chosen = info_pairs[totals.index(max_value)][1] 
        return chosen

    @staticmethod
    def random(neighbours) -> Action:
        return choice(neighbours)[1]
