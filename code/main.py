from maze_cell import MazeCell
from agent import Agent


rewards = [[-1, -1, -1 ,  40], 
           [-1, -1, -10, -10], 
           [-1, -1, -1 , -1 ], 
           [10, -2, -1 , -1 ]]
maze_cells = [[MazeCell(col, row, rewards[row][col]) for col in range(4)] for row in range(4)]
maze_cells[0][3].finish, maze_cells[3][0].finish = True, True
agent = Agent(2, 3, maze_cells)

agent.value_iteration()