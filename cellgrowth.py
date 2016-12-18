# coding = UTF-8
# written by Samuel Churlaud - quendil1
# distributed under license GPL-3.0
# cells growing on a plate with different phenotypes represented by a value
# for JereModel on github.com/quendil1/jeremodel
# version 3.2.3


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os.path


N = 200                # size of grid side
n_loop = 200           # number of iterations
state = [1, -30]       # possible starting state for any position
prob = 0.001           # probability for a position to be a cell
counter = []           # progress counter

diversity = 5          # genetic diversity of the population, the bigger the more diverse (arbitrary unit)
averageValue = 50      # average value
savePlot = True        # save mp4 and graphs or show grid then graphs, boolean


gifNumber = 1
while os.path.exists('animation' + str(N) + '_' + str(n_loop) + '_' + str(gifNumber) + '.gif') is True:
    gifNumber += 1


def cellgrowth(grid):
    newGrid = grid
    for i in range(N - 2):
        i += 1
        for j in range(N - 2):
            j += 1

            # if case not empty and not surrounded, try to fill one of the surrounding case, else skip
            if (grid[i, j] < 0) or ((grid[i, j - 1] >= 0) and (grid[i, j + 1] >= 0) and (grid[i - 1, j] >= 0) and
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
                    newGrid[i + x, j + y] = grid[i, j]
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

# randomize value for each cell
for i in range(N):
    for j in range(N):
        if grid[i, j] == 1:
            a = abs(np.random.normal(averageValue, diversity))
            if (a > 100) or (a < 0):
                j -= 1
            else:
                grid[i, j] = a


def update(data):
    return cellgrowth(grid)


# set up animation
fig, ax = plt.subplots()
mat = ax.matshow(grid)
plt.colorbar(mat)
ani = animation.FuncAnimation(fig, update, frames=n_loop, interval=1, save_count=50, blit=True)
if savePlot is True:
    ani.save('animation' + str(N) + '_' + str(n_loop) + '_' + str(gifNumber) + '.gif', writer='imagemagick', fps=10)
else:
    plt.show()
