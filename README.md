# jeremodel
Model for antibioresistance in an heterogenous population of microbes.

Dependencies :
- ffmpeg
- python3
- python3-tk

Python modules :
- matplotlib
- numpy
- os


cellgrowth.py simulate the growth of cells on a square plate. Each cell is assigned a random phenotype in a form of a number. Phenotypes are heritable. The cells grow at the rate of one division per iteration for each cell that is not already surrounded. Grid can be showed dynamically or saved as mp4. Visually, different phenotypes are shown as a gradation of color.

antibioresistance.py is based on cellgrowth.py. It adds random mutation and use this phenotype as antibioresistance. Antibiotics kill all the weakest cells, leaving only the most antibioresistant, which can then strive. Graphs with number of cells, average resistance and all final resistances are generated.

This model comes with no guarantee and does not model antibioresistance exhaustively nor in a perfectly realistic way. It only uses some simple biological rules to show the emergence of an antibioresistance among a virtual microbial population.
All the code is distributed under license GPL-3.0.