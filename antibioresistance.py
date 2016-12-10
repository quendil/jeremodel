# coding = UTF-8
# written by Nikola Zarevski (Klaklok) and Samuel Churlaud (quendil1)
# distributed under license GPL-3.0
# cells growing on a plate with mutation of the value describing them (here antibioresistance)
# adds antiobiotics after given time
# for JereModel on github.com/quendil1/jeremodel
# antibioresistance version 1.2.3
# based on cellgrowth 3.2.2 for JereModel


# import modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os.path


# plate
N = 200                         # size of grid side (100 - 400)
n_loop = 100                    # number of iterations (~1.5 times N)
emptyValue = -200               # value for empty case (> -100, must be > 0)
state = [1, emptyValue]         # possible starting state for any position ([1, emptyValue])
prob = 0.001                    # probability for a position to be a cell (0.01 - 0.00001)

# genetics
mutationRate = 30               # mutation rate (1 - 3)
counterpart = 0.9               # how much is cell growth slowed down because of antibioresistance (must be between 0 and 1)
diversity = 50                  # genetic diversity of the population, the bigger the more diverse (arbitrary unit) (10 - 100)
averageRes = 300                # average resistance (must be between 0 and 1000)
maxRes = 1000                   # maximum resistance for a cell (whatever)

# antibiotics
n_antibio = 0                   # number of time antibiotics is put on the system (depends incrDeadliness)
deadliness = 300                # efficiency of antiobiotics at beginning (~< averageRes)
incrDeadliness = 100            # how much is antibiotic deadliness increased (100 - 300)
firstAntibio = 30               # number of generations (iteration) before antibiotic is first used (~< 10)
stepAntibio = 20                # number of generations between each increase in antibiotic deadliness (5 - 30, depends mutationRate)

# code
counter = []                    # progress counter
population = []                 # list with number of cells at each iteration
mediumRes = []                  # list with average resistance at each iteration


# generate gif name
gifNumber = 1
while os.path.exists('animation' + str(N) + '_' + str(n_loop) + '_' + str(gifNumber) + '.gif') is True:
    gifNumber += 1

# generate png name
pngNumber = 1
while os.path.exists('graph' + str(N) + '_' + str(n_loop) + '_' + str(pngNumber) + '.png') is True:
    pngNumber += 1


# function for cells growing on the plate, with mutation and hereditary transmission of antibioresistance
def cellgrowth(grid):
    # generate growth of cells on the plate, with mutation
    newGrid = grid    # copy grid

    for i in range(N - 2):
        i += 1
        for j in range(N - 2):
            j += 1

            # if case empty or surrounded, skip, else try to fill one the empty surrounding cases
            if (grid[i, j] < 0) or ((grid[i, j - 1] >= 0) and (grid[i, j + 1] >= 0) and (grid[i - 1, j] >= 0) and
               (grid[i + 1, j] >= 0) and (grid[i - 1, j - 1] >= 0) and (grid[i - 1, j + 1] >= 0) and
               (grid[i + 1, j - 1] >= 0) and (grid[i + 1, j + 1] >= 0)):
                continue
            else:
                # the bigger the counterpart and resistance, the less likely to divide
                if np.random.random() > ((grid[i, j] / 1000) * counterpart):
                    # generate position of daughter cell compared to mother cell
                    x = np.random.choice([-1, 0, 1])
                    y = np.random.choice([-1, 0, 1])
                    # check if case not already full
                    if grid[i + x, j + y] >= 0:
                        j -= 1
                        continue
                    else:
                        # generate resistance of daughter cell (taking into account mutations)
                        a = grid[i, j] + np.random.normal(0, mutationRate)
                        # if generated resistance higher than max or lower than min, attribute max or min, else proceed normally
                        if a < 0:
                            newGrid[i + x, j + y] = 0
                        if a > maxRes:
                            newGrid[i + x, j + y] = maxRes
                        else:
                            newGrid[i + x, j + y] = a
                        continue
                else:
                    continue

    # return plottable data for animation
    mat.set_data(newGrid)
    return [mat]


# function for antibiotic effect on the plate
def antibiotic(grid):
    for i in range(N):
        for j in range(N):
            if grid[i, j] < deadliness:
                grid[i, j] = emptyValue
    return grid


# iteration function
def update(data):

    # update counter
    if (len(counter) % 10) == 0:
        print("progress %.0f%%" % (100. * float(len(counter)) / float(n_loop)))
    else:
        pass
    counter.append(0)

    # append average resistance to mediumRes and number of cells to population
    n = 0
    res = 0
    for i in range(N):
        for j in range(N):
            if grid[i, j] >= 0:
                n += 1
                res += grid[i, j]
    population.append(n)
    a = (res / n)
    mediumRes.append(a)

    # increase antibiotics every stepAntibio
    global deadliness
    if ((len(counter) - firstAntibio) % stepAntibio) == 0 and ((len(counter) - firstAntibio) / stepAntibio) < n_antibio:
        deadliness += incrDeadliness
    # call antibiotic function if necessary, else don't
    if len(counter) > firstAntibio and n_antibio != 0:
        return cellgrowth(antibiotic(grid))
    else:
        return cellgrowth(grid)


# generate grid and populate it
grid = np.random.choice(state, N * N, p=[prob, 1 - prob]).reshape(N, N)


# randomize resistance value for each cell
for i in range(N):
    for j in range(N):
        if grid[i, j] == 1:
            a = abs(np.random.normal(averageRes, diversity))
            if (a > maxRes) or (a < 0):
                j -= 1
            else:
                grid[i, j] = a


# set up animation
fig, ax = plt.subplots()
mat = ax.matshow(grid)
cbar = fig.colorbar(mat, boundaries=list(range(emptyValue, maxRes + 1, 100)))
cbar.set_clim([emptyValue, maxRes])
ani = animation.FuncAnimation(fig, update, frames=n_loop, interval=1, save_count=50, blit=True)
# save animation as gif
# ani.save('animation' + str(N) + '_' + str(n_loop) + '_' + str(gifNumber) + '.gif', writer='imagemagick', fps=10)
# or show animation
plt.show()


# generate lists with all the final resistances
allRes = []         # list with all resistance value at the end
allCell = []        # list with number of cells for each resistance value

for i in range(N):
    for j in range(N):
        if grid[i, j] >= 0:
            if grid[i, j] in allRes:
                number = allRes.index(grid[i, j])
                allCell[number] += 1
            else:
                allRes.append(grid[i, j])
                allRes = sorted(allRes)
                number = allRes.index(grid[i, j])
                allCell.append(1)
        else:
            pass

# plot both average res and population at each iteration
fig = plt.figure()
ax = fig.add_subplot(211)
ax.plot(mediumRes, label='average resistance', linestyle='solid', linewidth='2', color='red')
plt.ylabel('arbitrary unit')
plt.legend(loc=2, framealpha=0.5)
ax2 = ax.twinx()
ax2.plot(population, label='population', linestyle='solid', linewidth='2', color='blue')
plt.ylabel('n° of cells')
plt.legend(loc=1, framealpha=0.5)
plt.xlabel('iterations')


# plot with all resistances at the end
plt.subplot(212)
plt.plot(allRes, allCell, label='resistances at the end', linestyle='solid', linewidth='0.5', color='green')
plt.ylabel('n° of individuals')
plt.legend(loc=1, framealpha=0.5)
plt.xlabel('resistance')
plt.axis([0, maxRes, 0, max(allCell)])
# save graphs
# plt.savefig('graph' + str(N) + '_' + str(n_loop) + '_' + str(pngNumber) + '.png')
# or display them
plt.show()
