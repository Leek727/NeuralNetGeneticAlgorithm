from individual import Individual
import random
import math
import numpy as np
import copy
import matplotlib.pyplot as plt

POPULATIONSIZE = 200
CROSSOVERRATE = 2  # num neurons to change
MUTATIONRATE = .2  # x percent mutation chance per weight or bias
STRUCTURE = [1, 16,16, 1]

best = Individual()
best.generate_layers(STRUCTURE)
population = []
for individuals in range(POPULATIONSIZE):
    indiv = Individual()
    indiv.generate_layers(STRUCTURE)
    population.append(indiv)


def find_fitness(individual):
    # try to estimate sine
    fitness = 0
    for i in range(100):
        test = random.random()*2*math.pi
        fitness += abs(math.sin(test) - individual.inference([test]))[0]

    return fitness


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
for i in range(10):
    fitness_values = []

    # FITNESS AND SELECTION
    for indiv in population:
        fitness_values.append(find_fitness(indiv))

    fittest = [x for _, x in sorted(zip(fitness_values, population))]
    best0 = fittest[0]
    best1 = fittest[1]

    # CROSSOVER
    new_layers = best0.get_layers()
    randstart = len(new_layers)-CROSSOVERRATE
    for cross in range(round(random.random() * randstart), CROSSOVERRATE):
        rweight_index = random.randint(0, len(new_layers[cross][0][0]) - 1)
        # get the weights layer of the layer with index cross and swap with the other
        #print(f"crossing layer: {cross}")
        new_layers[cross][0][0][rweight_index] = best1.get_layers()[
            cross][0][0][rweight_index]

    best.set_layers(new_layers)
    # print(best0.get_layers())
    # MUTATION AND GENERATE OFFSPRING
    for indiv in population:
        indiv.set_layers(mutate(copy.deepcopy(new_layers)))

    print(sorted(fitness_values)[0])

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
plt.show()