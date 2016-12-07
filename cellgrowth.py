# coding = UTF-8
# written by Samuel Churlaud - quendil1
# version 3.0


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os.path


N = 100              # size of grid side
n_loop = 200         # number of iterations
state = [1, 0]       # possible starting state for any position
prob = 0.001         # probability for a position to be a cell
counter = []         # progress counter

fileNumber = 1
while os.path.exists('animation' + str(N) + '_' + str(n_loop) + '_' + str(fileNumber) + '.gif') is True:
    fileNumber += 1

grid = np.random.choice(state, N * N, p=[prob, 1 - prob]).reshape(N, N)  # generate grid and populate it


def update(data):

    for i in range(N - 2):
        i += 1
        for j in range(N - 2):
            j += 1
            # compute 8-neighbour sum to know how many are full
            surr = (grid[i, j - 1] + grid[i, j + 1] +
                    grid[i - 1, j] + grid[i + 1, j] +
                    grid[i - 1, j - 1] + grid[i - 1, j + 1] +
                    grid[i + 1, j - 1] + grid[i + 1, j + 1])

            # if case not empty and not surrounded, try to fill on of surrounding, else skip
            if (grid[i, j] == 0) or (surr == 8):
                continue
            else:
                x = np.random.choice([-1, 0, 1])
                y = np.random.choice([-1, 0, 1])
                if grid[i + x, j + y] == 1:
                    j -= 1
                    continue
                else:
                    grid[i + x, j + y] = 1
                    continue

    # update counter
    if (len(counter) % 10) == 0:
        print("progress %.0f%%" % (100. * float(len(counter)) / float(n_loop)))
    else:
        pass
    counter.append(0)

    # update data
    mat.set_data(grid)
    return [mat]


# set up animation
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, frames=n_loop, interval=1, save_count=50, blit=True)
ani.save('animation' + str(N) + '_' + str(n_loop) + '_' + str(fileNumber) + '.gif', writer='imagemagick', fps=10)
# plt.show()
