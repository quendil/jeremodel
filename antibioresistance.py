# coding = UTF-8
# written by Nikola Zarevski and Samuel Churlaud
# distributed under license GPL-3.0
# cells growing on a plate with mutation of the value describing them (here antibioresistance)
# for JereModel on github.com/quendil1/jeremodel
# version 1.0


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os.path


N = 200                          # size of grid side
n_loop = 100                     # number of iterations
emptyValue = -20                 # value for empty case
deathValue = -10                 # value for case with dead cell in it
state = [1, emptyValue]          # possible starting state for any position
prob = 0.001                     # probability for a position to be a cell
mutationRate = 3                 # mutation rate
counter = []                     # progress counter
diversity = 5                    # genetic diversity of the population, the bigger the more diverse (arbitrary unit)
averageRes = 50                  # average resistance
maxRes = 100                     # maximum resistance for a cell

# for gif generation, generate file name
fileNumber = 1
while os.path.exists('animation' + str(N) + '_' + str(n_loop) + '_' + str(fileNumber) + '.gif') is True:
    fileNumber += 1


def cellgrowth(grid):
    # generate growth of cells on the plate, with mutation
    newGrid = grid    # copy grid

    for i in range(N - 2):
        i += 1
        for j in range(N - 2):
            j += 1

            # if case not empty and not surrounded, try to fill one of the surrounding case, else skip
            if (grid[i, j] < 0) or ((grid[i, j - 1] >= 0) and (grid[i, j - 1] >= 0) and (grid[i - 1, j] >= 0) and
               (grid[i + 1, j] >= 0) and (grid[i - 1, j - 1] >= 0) and (grid[i - 1, j + 1] >= 0) and
               (grid[i + 1, j - 1] >= 0) and (grid[i + 1, j + 1] >= 0)):
                continue
            else:
                x = np.random.choice([-1, 0, 1])
                y = np.random.choice([-1, 0, 1])
                if grid[i + x, j + y] >= 0:
                    j -= 1
                    continue
                else:
                    a = grid[i, j] + np.random.normal(0, mutationRate)     # change resistance value because of mutations
                    if a < 0:
                        newGrid[i + x, j + y] = 0
                    if a > maxRes:
                        newGrid[i + x, j + y] = maxRes
                    else:
                        newGrid[i + x, j + y] = a
                    continue

    # update counter
    if (len(counter) % 10) == 0:
        print("progress %.0f%%" % (100. * float(len(counter)) / float(n_loop)))
    else:
        pass
    counter.append(0)

    # update data
    mat.set_data(newGrid)
    return [mat]


grid = np.random.choice(state, N * N, p=[prob, 1 - prob]).reshape(N, N)  # generate grid and populate it

# randomize resistance value for each cell
for i in range(N):
    for j in range(N):
        if grid[i, j] == 1:
            a = abs(np.random.normal(averageRes, diversity))
            if (a > maxRes) or (a < 0):
                j -= 1
            else:
                grid[i, j] = a


def update(data):
    return cellgrowth(grid)


# set up animation
fig, ax = plt.subplots()
mat = ax.matshow(grid)
cbar = fig.colorbar(mat, boundaries=[-20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
cbar.set_clim([-20, 100])
ani = animation.FuncAnimation(fig, update, frames=n_loop, interval=1, save_count=50, blit=True)
# ani.save('animation' + str(N) + '_' + str(n_loop) + '_' + str(fileNumber) + '.gif', writer='imagemagick', fps=10)
plt.show()
