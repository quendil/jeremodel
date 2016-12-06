import random as rand
import numpy as np

###### Initialisation
n = 10
O = 1.
c = 0
c1 = 0
print(rand.random())
population = [[rand.choice([0,1]) for i in range(n)] for j in range(n)]
phenotypic_pool = [[]for j in range(n)]

print(population)

#Generation of an innocent population
for line in range(len(population)):
	for cell in range(len(population[line])):
		if population[line][cell] == 1:
			c += 1
			phenotypic_pool[line].append(1)
		else:
			phenotypic_pool[line].append(0)
print(c)
print("phenotypic_pool :", phenotypic_pool)
 ######

 ###### Start the Dynamics

 	#Probabilistic Growth and Death of the different cells
def Growing_population(y):
	for p in range(len(y)):
		for q in range(len(y)):
			if y[p][q] == 1:
			#First, check the survival of the cell
				survival = 0.9
				hazard = rand.random()
				if phenotypic_pool[p][q] * hazard >= survival :
					y[p][q] = 0
				# If survived, the cell can divide but its rate of division depends on its phenotype
					growth_probability = 0.5
					hazard = rand.random()
					if phenotypic_pool[p][q] * hazard > growth_probability :
					#Binary fission
						move = rand.sample([1, 2, 3, 4], 1)
						if move == 1:
							y[p][q+1] = 1
						elif move == 2:
							y[p][q-1] = 1
						elif move == 3:
							y[p+1][q] = 1
						elif move == 4:
							y[p-1][q] = 1
				

			else: 
				continue

	return y;

population = Growing_population(population)
print(population)

for line in range(len(population)):
	for cell in range(len(population[line])):
		if population[line][cell] == 1:
			c1 += 1
print(c1)