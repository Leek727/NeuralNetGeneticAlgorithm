import neat
from naturalenvironment import find_fitness

def eval_genomes(genomes, config):
    nets = []
    for genome_id, genome in genomes:
        #genome.fitness = 4.0
        nets.append(neat.nn.FeedForwardNetwork.create(genome, config))

    fitness_values = find_fitness(nets)
    for index,(genome_id, genome) in enumerate(genomes):
        genome.fitness = fitness_values[index]
    """
        for xi, xo in zip(xor_inputs, xor_outputs):
            output = net.activate(xi)
            genome.fitness -= (output[0] - xo[0]) ** 2
    """


# Load configuration.
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation,
                     'config-feedforward')

# Create the population, which is the top-level object for a NEAT run.
p = neat.Population(config)

# Add a stdout reporter to show progress in the terminal.
p.add_reporter(neat.StdOutReporter(False))

# Run until a solution is found.
winner = p.run(eval_genomes)

# Display the winning genome.
print('\nBest genome:\n{!s}'.format(winner))

# Show output of the most fit genome against training data.
#print('\nOutput:')
#winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
#for xi, xo in zip(xor_inputs, xor_outputs):
#    output = winner_net.activate(xi)
#    print("  input {!r}, expected output {!r}, got {!r}".format(xi, xo, output))