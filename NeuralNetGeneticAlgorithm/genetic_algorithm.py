from individual import Individual
import random
import math
import numpy as np
import copy
import matplotlib.pyplot as plt
from naturalenvironment import find_fitness

POPULATIONSIZE = 1000
CROSSOVERRATE = 2  # num neurons to change
MUTATIONCHANCE = .8
MUTATIONRATE = .8 # x percent mutation chance per weight or bias+POPULATIONSIZE*2
STRUCTURE = [4, 10, 10, 2]

best = Individual()
best.generate_layers(STRUCTURE)
population = []
for individuals in range(POPULATIONSIZE):
    indiv = Individual()
    indiv.generate_layers(STRUCTURE)
    population.append(indiv)


def afind_fitness(individual):
    # FITNESS AND SELECTION
    fitness_values =[]
    for indiv in population:
        # try to estimate sine
        fitness = 0
        for i in range(100):
            test = random.random()*2*math.pi
            fitness += abs(math.sin(test) - indiv.inference([test]))[0]
        fitness_values.append(fitness)

    return fitness_values


def mutate(new_layers):
    for cross in range(len(new_layers)):
        if random.random() < MUTATIONRATE:
            rweight_index = random.randint(0, len(new_layers[cross][0][0]) - 1)
            # get the weights layer of the layer with index cross and swap with the other
            #print(f"mutating weight in layer: {cross}")
            new_layers[cross][0][0][rweight_index] = random.random()

    return new_layers


# generation loop
gen = 0
best0 = Individual()
best0.generate_layers(STRUCTURE)

best1 = Individual()
best1.generate_layers(STRUCTURE)

best0_score = float("inf")
best1_score = float("inf")
for i in range(100000):

    fitness_values = find_fitness(population)
    for i, score in enumerate(fitness_values):
        if score < best0_score:
            best0.set_layers(population[i].get_layers())
            best0_score = score

        elif score < best1_score:
            best1.set_layers(population[i].get_layers())
            best1_score = score

    
    # CROSSOVER
    new_layers = best0.get_layers()
    randstart = len(new_layers)-CROSSOVERRATE
    for cross in range(round(random.random() * randstart), CROSSOVERRATE):
        rweight_index = random.randint(0, len(new_layers[cross][0][0]) - 1)
        # get the weights layer of the layer with index cross and swap with the other
        #print(f"crossing layer: {cross}")
        new_layers[cross][0][0][rweight_index] = best1.get_layers()[
            cross][0][0][rweight_index]

    for player in population:
        player.set_layers(new_layers)
    # print(best0.get_layers())
    # MUTATION AND GENERATE OFFSPRING
    for ind, indiv in enumerate(population):
        if random.random() < MUTATIONCHANCE and ind != 0:
            indiv.set_layers(mutate(copy.deepcopy(new_layers)))
        else:
            indiv.set_layers(copy.deepcopy(new_layers))

    print(sorted(fitness_values)[0])

print(best.get_layers())
"""
x0 = []
y0 = []
y1 = []
for i in range(int(2*math.pi*100)):
    x0.append(i/100)
    y0.append(best.inference([i/100])[0])
    y1.append(math.sin(i/100))

plt.plot(x0, y0, 'r')
plt.plot(x0, y1, 'b')
plt.axis('scaled')
#plt.ylim([0, 30])
plt.show()"""