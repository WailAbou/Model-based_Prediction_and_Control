from typing import List
from actions import Action
from maze_cell import MazeCell


class Maze:
    def __init__(self, maze_cells: List[List[MazeCell]]) -> None:
        self.maze_cells = maze_cells

    def update(self, discount: float):
        calculate_values = lambda maze_cell: self.calculate_values(maze_cell, discount)
        new_values = [list(map(calculate_values, row_cells)) for row_cells in self.maze_cells]
        self.update_values(new_values)
        return sum(map(sum, new_values))

    def calculate_values(self, maze_cell: MazeCell, discount: float):
        neighbours = [neighbour[0] for neighbour in self.get_neighbouring_cells(self.maze_cells, maze_cell)]
        new_value = maze_cell.calculate_values(neighbours, discount)
        return new_value

    def update_values(self, new_values: List[float]):
        for row, maze_row in enumerate(self.maze_cells):
            for col, maze_cell in enumerate(maze_row):
                maze_cell.update(new_values[row][col])

    @staticmethod
    def get_neighbouring_cells(maze_cells, maze_cell: MazeCell):
        neighbours = [
            (Maze.get_cell(maze_cells, maze_cell, 0, -1), Action.UP),
            (Maze.get_cell(maze_cells, maze_cell, 1, 0), Action.RIGHT),
            (Maze.get_cell(maze_cells, maze_cell, 0, 1), Action.DOWN),
            (Maze.get_cell(maze_cells, maze_cell, -1, 0), Action.LEFT)
        ]
        return neighbours
    
    @staticmethod
    def get_cell(maze_cells, maze_cell: MazeCell, x: int, y: int):
        nx, ny = maze_cell.x + x, maze_cell.y + y
        return maze_cells[ny][nx] if -1 < ny < 4 and -1 < nx < 4 else maze_cell 
