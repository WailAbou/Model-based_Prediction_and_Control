from typing import List, Tuple
from actions import Action
from maze_cell import MazeCell


class Maze:
    def __init__(self, maze_cells: List[List[MazeCell]]) -> None:
        self.maze_cells = maze_cells

    def update(self, discount: float) -> float:
        """Updates the state of the maze by updating all the maze cells.

        Parameters
        ----------
        discount
            A discount value for the bellman_equation.

        Returns
        -------
        float
            The total sum of all the maze cells value.
        """
        calculate_values = lambda maze_cell: self.calculate_values(maze_cell, discount)
        new_values = [list(map(calculate_values, row_cells)) for row_cells in self.maze_cells]
        self.update_values(new_values)
        return sum(map(sum, new_values))

    def calculate_values(self, maze_cell: MazeCell, discount: float) -> float:
        """Calculates the new value of the given maze cell.

        Parameters
        ----------
        maze_cell
            The current maze cell to calculate the values of
        discount
            A discount value for the bellman_equation.

        Returns
        -------
        float
            The new calculated value.
        """
        neighbours = [neighbour[0] for neighbour in self.get_neighbouring_info(self.maze_cells, maze_cell)]
        new_value = maze_cell.calculate_values(neighbours, discount)
        return new_value

    def update_values(self, new_values: List[float]) -> None:
        for row, maze_row in enumerate(self.maze_cells):
            for col, maze_cell in enumerate(maze_row):
                maze_cell.update(new_values[row][col])

    @staticmethod
    def get_neighbouring_info(maze_cells: List[List[MazeCell]], maze_cell: MazeCell) -> Tuple[MazeCell, Action]:
        info = [
            (Maze.get_cell(maze_cells, maze_cell, 0, -1), Action.UP),
            (Maze.get_cell(maze_cells, maze_cell, 1, 0), Action.RIGHT),
            (Maze.get_cell(maze_cells, maze_cell, 0, 1), Action.DOWN),
            (Maze.get_cell(maze_cells, maze_cell, -1, 0), Action.LEFT)
        ]
        return info
    
    @staticmethod
    def get_cell(maze_cells: List[List[MazeCell]], maze_cell: MazeCell, x_offset: int, y_offset: int) -> MazeCell:
        """Gets a cell given a list of all cells the current cell and the x and y offsets.

        Parameters
        ----------
        maze_cell
            The current maze cell to calculate the values of
        discount
            A discount value for the bellman_equation.

        Returns
        -------
        MazeCell
            The found maze cell (the given maze cell if it is not found).
        """
        nx, ny = maze_cell.x + x_offset, maze_cell.y + y_offset
        return maze_cells[ny][nx] if -1 < ny < 4 and -1 < nx < 4 else maze_cell 
