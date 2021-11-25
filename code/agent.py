from typing import List
from maze_cell import MazeCell
from maze import Maze
from policy import Policy
from visualizer import Visualizer


class Agent:
    def __init__(self, x: int, y: int, maze_cells: List[List[MazeCell]]) -> None:
        self.x, self.y = x, y
        self.maze = Maze(maze_cells)
        self.policy = Policy(Policy.greedy)
        self.visualizer = Visualizer()
        self.discount = 1

    def value_iteration(self) -> float:
        """Excutes value iteration with chosen policy and visualizes it 
        until the difference is smaller then delta.

        Returns
        -------
        new_total
            The last iteration total value of the maze.
        """
        old_total, total, delta = 0, 1, 0.01
        while abs(total - old_total) > delta:
            old_total, total = total, self.maze.update(self.discount)
        self.visualizer.visualize_all(self.maze, self.policy)
        return total
