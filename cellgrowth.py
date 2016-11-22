import numpy as np
import matplotlib.animation as anim
import random as rand

n_loop = 100         # length of simulation
n_cell = 1           # initial number of cells
divTime = 1          # growth rate cells
gridSize = 100       # size of grid side, square root of possible number of cells

# position of all cells on the grid
cell = [np.array([round(rand.random() * gridSize) for i in range(2)]) for i in range(n_cell)]


for n in range(n_loop):
    n_cell *= 2
    for i in range(len(cell)):
        a = cell[i][0] + rand.choice([-1, 1])
        b = cell[i][1] + rand.choice([-1, 1])
        ab = np.array([a, b])

        np.append(cell, ab)










