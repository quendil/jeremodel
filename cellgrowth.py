import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 100            # size of grid side
n_loop = 200       # number of iterations
state = [1, 0]     # possible starting states for any position
prob = 0.001       # probability of having one cell in one position
counter = []
prog = 0


# populate grid with random on/off - more off than on
grid = np.random.choice(state, N * N, p=[prob, 1 - prob]).reshape(N, N)


def update(data):
    global grid
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line
    newGrid = grid.copy()

    for i in range(N - 1):
        # if not first line normal, if first line don't take into account the i-1 (first line minus one)
        if i != 0:
            for j in range(N - 1):
                # if not first line normal, if first line don't take into account the j-1 (first line minus one)
                if j != 0:
                    # compute 8-neighbor sum and divide by 255 to know how many are full
                    surr = (grid[i, j - 1] + grid[i, j + 1] +
                            grid[i - 1, j] + grid[i + 1, j] +
                            grid[i - 1, j - 1] + grid[i - 1, j + 1] +
                            grid[i + 1, j - 1] + grid[i + 1, j + 1]) / 255

                    # apply Conway's rules
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
                            newGrid[i + x, j + y] = 2
                            continue

                # exception for first j line
                else:
                    surr = (grid[i, j + 1] + grid[i - 1, j] + grid[i + 1, j] +
                            grid[i - 1, j + 1] + grid[i + 1, j + 1]) / 255

                    if (grid[i, j] == 0) or (surr == 5):
                        continue
                    else:
                        x = np.random.choice([-1, 0, 1])
                        y = np.random.choice([0, 1])
                        if grid[i + x, j + y] == 1:
                            j -= 1
                            continue
                        else:
                            newGrid[i + x, j + y] = 1

            # exception for last j line
            j = N - 1
            surr = (grid[i, j - 1] + grid[i - 1, j] + grid[i + 1, j] +
                    grid[i - 1, j - 1] + grid[i + 1, j - 1]) / 255
            if (grid[i, j] == 0) or (surr == 5):
                continue
            else:
                x = np.random.choice([-1, 0, 1])
                y = np.random.choice([-1, 0])
                if grid[i + x, j + y] == 1:
                    j -= 1
                    continue
                else:
                    newGrid[i + x, j + y] = 1
                    continue

        # exception for first i line
        else:
            for j in range(N - 1):
                # if not first line normal, if first line don't take into account the j-1 (first line minus one)
                if j != 0:
                    # compute 8-neighbor sum and divide by 255 to know how many are full
                    surr = (grid[i, j - 1] + grid[i, j + 1] + grid[i + 1, j] +
                            grid[i + 1, j - 1] + grid[i + 1, j + 1]) / 255

                    # apply Conway's rules
                    # if case not empty and not surrounded, try to fill on of surrounding, else skip
                    if (grid[i, j] == 0) or (surr == 5):
                        continue
                    else:
                        x = np.random.choice([0, 1])
                        y = np.random.choice([-1, 0, 1])
                        if grid[i + x, j + y] == 1:
                            j -= 1
                            continue
                        else:
                            newGrid[i + x, j + y] = 1
                            continue

                # exception for first j line
                else:
                    surr = (grid[i, j + 1] + grid[i + 1, j] +
                            grid[i + 1, j + 1]) / 255

                    if (grid[i, j] == 0) or (surr == 3):
                        continue
                    else:
                        x = np.random.choice([0, 1])
                        y = np.random.choice([0, 1])
                        if grid[i + x, j + y] == 1:
                            j -= 1
                            continue
                        else:
                            newGrid[i + x, j + y] = 1

            # exception for last j line
            j = N - 1
            surr = (grid[i, j - 1] + grid[i + 1, j] +
                    grid[i + 1, j - 1]) / 255

            if (grid[i, j] == 0) or (surr == 3):
                continue
            else:
                x = np.random.choice([0, 1])
                y = np.random.choice([-1, 0])
                if grid[i + x, j + y] == 1:
                    j -= 1
                    continue
                else:
                    newGrid[i + x, j + y] = 1
                    continue

        # exception for last i line
        for j in range(N - 1):
            # if not first line normal, if first line don't take into account the j-1 (first line minus one)
            if j != 0:
                # compute 8-neighbor sum and divide by 255 to know how many are full
                surr = (grid[i, j - 1] + grid[i, j + 1] + grid[i - 1, j] +
                        grid[i - 1, j - 1] + grid[i - 1, j + 1]) / 255

                # apply Conway's rules
                # if case not empty and not surrounded, try to fill on of surrounding, else skip
                if (grid[i, j] == 0) or (surr == 5):
                    continue
                else:
                    x = np.random.choice([-1, 0])
                    y = np.random.choice([-1, 0, 1])
                    if grid[i + x, j + y] == 1:
                        j -= 1
                        continue
                    else:
                        newGrid[i + x, j + y] = 1
                        continue

            # exception for first j line
            else:
                surr = (grid[i, j + 1] + grid[i - 1, j] +
                        grid[i - 1, j + 1]) / 255

                if (grid[i, j] == 0) or (surr == 3):
                        continue
                else:
                    x = np.random.choice([-1, 0])
                    y = np.random.choice([0, 1])
                    if grid[i + x, j + y] == 1:
                        j -= 1
                        continue
                    else:
                        newGrid[i + x, j + y] = 1

        # exception for last j line
        j = N - 1
        surr = (grid[i, j - 1] + grid[i - 1, j] +
                grid[i - 1, j - 1]) / 255

        if (grid[i, j] == 0) or (surr == 3):
            continue
        else:
            x = np.random.choice([-1, 0])
            y = np.random.choice([-1, 0])
            if grid[i + x, j + y] == 1:
                j -= 1
                continue
            else:
                newGrid[i + x, j + y] = 1
                continue

    # update data
    mat.set_data(newGrid)
    grid = newGrid
    if (len(counter) % 10) == 0:
        print("avancement %.0f%%" % (100. * float(len(counter)) / float(n_loop)))
    else:
        pass
    counter.append(1)
    return [mat]


# set up animation
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, frames=n_loop, interval=100, blit=True)
ani.save('animation.gif', writer='imagemagick', fps=10)
# plt.show()
ani.event_source.stop()
