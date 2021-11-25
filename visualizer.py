from typing import List, Union
from actions import Action
from maze import Maze
from maze_cell import MazeCell
from policy import Policy


class Visualizer:
    def visualize_all(self, maze: Maze, policy: Policy):
        self.visualize(maze.maze_cells)
        actions = policy.get_actions(maze.maze_cells) 
        self.visualize(actions)

    def visualize(self, targets: Union[List[MazeCell], Action]):
        print(' ', ''.join([f" | {' ':10s}{str(i):10s} |" for i in range(4)]))
        for row in range(len(targets)):
            print('-' * 100)
            print(row, ''.join([f" | {str(targets[row][col]):20s} |" for col in range(4)]))
            print('_' * 100)
        print('\n')
