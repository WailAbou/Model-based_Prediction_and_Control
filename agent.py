from maze_cell import MazeCell
from typing import List
from maze import Maze
from policy import Policy
from visualizer import Visualizer


class Agent:
    def __init__(self, x, y, maze_cells: List[List[MazeCell]]) -> None:
        self.x, self.y = x, y
        self.maze = Maze(maze_cells)
        self.policy = Policy(Policy.greedy)
        self.visualizer = Visualizer()
        self.discount = 1

    def value_iteration(self):
        old_total, new_total, delta = 0, 1, 0.01
        while abs(new_total - old_total) > delta:
            old_total, new_total = new_total, self.maze.update(self.discount)
        self.visualizer.visualize_all(self.maze, self.policy)
