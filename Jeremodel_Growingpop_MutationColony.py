import random as rand
import numpy as np

###### Initialisation ######
time = 20
n = 10
O = 1.
c = 0
c1 = 0
print(rand.random())
population = [[rand.choice([0,1]) for i in range(n)] for j in range(n)]
phenotypic_pool = [[]for j in range(n)]

#print("population:",population)

	#Generation of an innocent population
for line in range(len(population)):
	for cell in range(len(population[line])):
		if population[line][cell] == 1:
			c += 1
			phenotypic_pool[line].append(rand.random())
		else:
			phenotypic_pool[line].append(0)
print(c)
#print("phenotypic_pool :", phenotypic_pool)
######______________________________________



###### Start the Dynamics ######

 	#Probabilistic Growth and Death of the different cells
def Growing_population(x, y):
	for p in range(len(y)):
		for q in range(len(y)):
			if y[p][q] == 1:
			#First, check the survival of the cell
				survival = 0.5
				hazard = rand.random()
				if x[p][q] * hazard >= survival :
					y[p][q] = 0
				# If survived, the cell can divide but its rate of division depends on its phenotype
				else:
					growth_probability = 0
					mutation_rate = 0.001
					hazard = rand.random()
					if x[p][q] * hazard <= growth_probability:
					#Binary fission
						move = rand.sample([1, 2, 3, 4], 1)
						if move == [1] and q < n-1:
							y[p][q+1] = 1
							x[p][q+1] = x[p][q] + rand.random() * mutation_rate
						elif move == [2]:
							y[p][q-1] = 1
							x[p][q-1] = x[p][q] + rand.random() * mutation_rate
						elif move == [3] and p < n-1:
							y[p+1][q] = 1
							x[p+1][q] = x[p][q] + rand.random() * mutation_rate
						elif move == [4]:
							y[p-1][q] = 1
							x[p-1][q] = x[p][q] + rand.random() * mutation_rate
				

			else: 
				continue

	return x, y;

	#Probability of mutation
def Mutation(y,x):
	mutation_probability = 0.001
	for p in range(len(y)):
		for q in range(len(y)):
			if y[p][q] == 1:
				hazard = rand.random()
				if hazard < mutation_probability:
					x[p][q] = rand.choice(0, 1)

	return y, x;

for t in range(0,time):
	phenotypic_pool, population = Growing_population(phenotypic_pool, population)
	population, phenotypic_pool = Mutation(population, phenotypic_pool)
#print("population:",population)
	for line in range(len(population)):
		for cell in range(len(population[line])):
			if population[line][cell] == 1:
				c1 += 1
	print(c1)

#print("phenotypic_pool:",phenotypic_pool)
