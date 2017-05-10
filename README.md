# jeremodel
Model for antibioresistance in an heterogenous population of microbes.

Dependencies (for GNU/Linux, haven't tried on other OS) :
- ffmpeg
- python3
- python3-matplotlib
- python3-numpy
- python3-tk

Python modules used :
- matplotlib (any version should after 1.5 should do)
- numpy
- os


cellgrowth.py simulate the growth of cells on a square plate. Each cell is assigned a random phenotype in a form of a number. Phenotypes are heritable and can mutate between generations. The cells grow at the rate of one division per iteration for each cell that is not already surrounded. A higher phenotype value can lead to a slower reproduction, as many mutations comes with a cost ; here, having a lower phenotype value helps the cells reproduce faster. Grid can be showed dynamically or saved as mp4 (all plots are saved in "plots" folder). Graphs with number of cells, average phenotype and all final phenotypes are generated. Visually, different phenotypes are shown as a gradation of color.

antibioresistance.py is based on cellgrowth.py. It uses the phenotype as antibioresistance. Antibiotics kill all the weakest cells, leaving only the most antibioresistant, which can then strive.

This model comes with no guarantee and does not model antibioresistance or cell growth exhaustively nor in a perfectly realistic way. It only uses some simple biological rules to show the emergence of an antibioresistance among a virtual microbial population.
All the code is distributed under license GPL-3.0.