# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as anim
import random as rand

n_loop = 10         # length of simulation
n_cell = 1           # initial number of cells
divTime = 1          # growth rate cells
gridSize = 24       # size of grid side, square root of possible number of cells
grid = [0 for i in range(gridSize**2)]
cell = []

# position of all cells on the grid
for i in range(n_cell):
    x = round(rand.random() * gridSize)
    y = round(rand.random() * gridSize)
    pos = (y * gridSize) + x
    if grid[pos] == 0:
        grid[pos] = 1
        cell.append([x, y])
    else:
        i -= 1
        continue


def cellGrowth():

    for i in range(len(cell)):
        x1 = cell[i][0]
        x2 = cell[i][0] + 1
        x3 = cell[i][0] - 1
        y1 = cell[i][1]
        y2 = cell[i][1] + 1
        y3 = cell[i][1] - 1
        pos1 = x1 + (y2 * gridSize)
        pos2 = x1 + (y3 * gridSize)
        pos3 = x2 + (y1 * gridSize)
        pos4 = x2 + (y2 * gridSize)
        pos5 = x2 + (y3 * gridSize)
        pos6 = x3 + (y1 * gridSize)
        pos7 = x3 + (y2 * gridSize)
        pos8 = x3 + (y3 * gridSize)
        # grid1 = 
        # grid2
        # grid3
        # grid4
        # grid5
        # grid6
        # grid7
        # grid8

        if grid[pos1] != 0 and grid[pos2] != 0 and grid[pos3] != 0 and grid[pos4] != 0 and\
           grid[pos5] != 0 and grid[pos6] != 0 and grid[pos7] != 0 and grid[pos8] != 0:
            continue
        else:
            x = rand.choice([x1, x2, x3])
            y = rand.choice([y1, y2, y3])
            pos = (y * gridSize) + x
            if grid[pos] == 0:
                grid[pos] = 1
                # n_cell += 1
                cell.append([x, y])
            else:
                i -= 1
                continue
        # except IndexError:
        #     continue


for n in range(n_loop):
    cellGrowth()
print(grid)
print(cell)


# def update(data):
#     mat.set_data(data)
#     return mat


# def data_gen():
#     for n in range(n_loop):
#         yield cellGrowth()


# fig, ax = plt.subplots()
# mat = ax.matshow(cellGrowth())
# ani = animation.FuncAnimation(fig, update, data_gen, interval=500, save_count=50)
# plt.show()
