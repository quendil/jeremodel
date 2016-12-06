import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 100
ON = 255
OFF = 0
vals = [ON, OFF]

# populate grid with random on/off - more off than on
grid = np.random.choice(vals, N * N, p=[0.05, 0.95]).reshape(N, N)


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
                    if (grid[i, j] == ON) or (surr == 8):
                        continue
                    else:
                        x = np.random.choice([-1, 0, 1])
                        y = np.random.choice([-1, 0, 1])
                        if grid[i + x, j + y] == ON:
                            j -= 1
                            continue
                        else:
                            newGrid[i + x, j + y] = ON
                            continue
                # exception if first j line
                else:
                    surr = (grid[i, j + 1] + grid[i - 1, j] + grid[i + 1, j] +
                            grid[i - 1, j + 1] + grid[i + 1, j + 1]) / 255

                    if grid[i, j] == OFF:
                        if (surr == 5):
                            continue
                        else:
                            x = np.random.choice([-1, 0, 1])
                            y = np.random.choice([0, 1])
                            if grid[i + x, j + y] == ON:
                                j -= 1
                                continue
                            else:
                                newGrid[i + x, j + y] = ON
                    else:
                        continue
            # exception if last j line
            j = N
            surr = (grid[i, j - 1] + grid[i - 1, j] + grid[i + 1, j] +
                    grid[i - 1, j - 1] + grid[i + 1, j - 1]) / 255
            if (grid[i, j] == ON) or (surr == 5):
                continue
            else:
                x = np.random.choice([-1, 0])
                y = np.random.choice([-1, 0])
                if grid[i + x, j + y] == ON:
                    j -= 1
                    continue
                else:
                    newGrid[i + x, j + y] = ON
                    continue

        # exception for first i line
        else:
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
                    if (grid[i, j] == ON) or (surr == 8):
                        continue
                    else:
                        x = np.random.choice([-1, 0, 1])
                        y = np.random.choice([-1, 0, 1])
                        if grid[i + x, j + y] == ON:
                            j -= 1
                            continue
                        else:
                            newGrid[i + x, j + y] = ON
                            continue
                # exception if first j line
                else:
                    surr = (grid[i, j + 1] + grid[i - 1, j] + grid[i + 1, j] +
                            grid[i - 1, j + 1] + grid[i + 1, j + 1]) / 255

                    if grid[i, j] == OFF:
                        if (surr == 5):
                            continue
                        else:
                            x = np.random.choice([-1, 0, 1])
                            y = np.random.choice([0, 1])
                            if grid[i + x, j + y] == ON:
                                j -= 1
                                continue
                            else:
                                newGrid[i + x, j + y] = ON
                    else:
                        continue
            # exception if last j line
            j = N
            surr = (grid[i, j - 1] + grid[i - 1, j] + grid[i + 1, j] +
                    grid[i - 1, j - 1] + grid[i + 1, j - 1]) / 255
            if (grid[i, j] == ON) or (surr == 5):
                continue
            else:
                x = np.random.choice([-1, 0])
                y = np.random.choice([-1, 0])
                if grid[i + x, j + y] == ON:
                    j -= 1
                    continue
                else:
                    newGrid[i + x, j + y] = ON
                    continue



    # update data
    mat.set_data(newGrid)
    grid = newGrid
    return [mat]


# set up animation
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, interval=50,
                              save_count=50, blit=True)
plt.show()
# ani.save(filename='anim.mp4', fps=1)
