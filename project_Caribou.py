import matplotlib.animation as animation
import random

# size of the plate
grille = 100
time = 0


grid = []
for ligne in range(grille):
    lignes = []
    for colonne in range(grille):
        cellule = {}
        if random.random() > 0.999:
            cellule["value"] = 10
            cellule["ligne"] = ligne
            cellule["colonne"] = colonne
            cellule["divide"] = 0
            cellule["name"] = int(ligne) + int(colonne)
        else:
            cellule["value"] = 0
            cellule["ligne"] = ligne
            cellule["colonne"] = colonne
            cellule["divide"] = 0
        grid.append(cellule)


def tri(data):
    output = []
    for ligne in range(grille):
        lignes = []
        for colonne in range(grille):
            for cell in data:
                if cell["ligne"] == ligne and cell["colonne"] == colonne:
                    lignes.append(cell["value"])
                    cell["divide"] = 0
                    break
        output.append(lignes)
    return output


def generation_of_data():
    for cell in grid:
        if cell["value"] == 0:
            for cell_next in grid:
                if cell_next["value"] > 0 and cell_next["divide"] == 0:
                    if cell_next["ligne"] == cell["ligne"]:
                        if cell_next["colonne"] - 1 == cell["colonne"]\
                           or cell_next["colonne"] + 1 == cell["colonne"]\
                           or cell_next["colonne"] == cell["colonne"]:
                            if random.random() < 0.9:
                                cell_next["divide"] = 0
                                cell["value"] = 1
                                cell["divide"] = 1
                            else:
                                cell["value"] = 0
                    if cell_next["colonne"] == cell["colonne"]:
                        if cell_next["ligne"] - 1 == cell["ligne"]\
                           or cell_next["ligne"] + 1 == cell["ligne"]\
                           or cell_next["ligne"] == cell["ligne"]:
                            if random.random() < 0.9:
                                cell_next["divide"] = 0
                                cell["value"] = 1
                                cell["divide"] = 1
                            else:
                                cell["value"] = 0
                    if random.random() < 0.5:
                        if cell_next["colonne"] - 1 == cell["colonne"]\
                           or cell_next["colonne"] + 1 == cell["colonne"]\
                           or cell_next["colonne"] == cell["colonne"]:
                            if cell_next["ligne"] - 1 == cell["ligne"]\
                               or cell_next["ligne"] + 1 == cell["ligne"]\
                               or cell_next["ligne"] == cell["ligne"]:
                                if random.random() < 0.9:
                                    cell_next["divide"] = 0
                                    cell["value"] = 1
                                    cell["divide"] = 1
                                else:
                                    cell["value"] = 0
        else:
            cell["value"] = cell["value"] + 1
    output = tri(grid)
    for cell in grid:
        cell["divide"] = 0
    print(output)
    print("--")
    return output


def update(data):
    mat.set_data(data)
    return mat


def data_gen():
    while True:
        yield generation_of_data()


fig, ax = plt.subplots()
mat = ax.matshow(generation_of_data())
ani = animation.FuncAnimation(fig, update, data_gen, interval=500,
                              save_count=50)
plt.show()
