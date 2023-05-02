import numpy as np
import math
from activations import activation
import random

class Individual:
    def __init__(self):
        self.layers = []
        self.activations = []

    def inference(self, input_layer):
        for act_index, layer in enumerate(self.layers):
            weights = layer[0]
            biases = layer[1]

            # matrix multiply the input layer by the weights and add biases to get output
            neurons = np.add(
                np.matmul(input_layer, weights),
                biases
            )

            # apply activation function
            for i in range(len(neurons)):
                neurons[i] = activation(neurons[i], self.activations[act_index])

            input_layer = neurons

        return input_layer

    def generate_layers(self, structure = [10,30,1]):
        # 0 = sigmoid, 1 = tanh, 2 = ReLU, 3 = Leaky ReLU, 4 = Softmax, 5 = linear
        self.activations = [1 for x in range(len(structure)-1)]
        layers = []
        for index,layer_num in enumerate(structure[1:]):
            weights = []

            # generate weight layers
            for i in range(structure[index]):
                weights.append([1 - 2 * random.random() for a in range(layer_num)])


            # generate bias layers
            biases = []
            for i in range(layer_num):
                biases.append(1 - 2 * random.random())

            layers.append([weights,biases])

        self.layers = layers

    def get_layers(self):
        return self.layers
    
    def set_layers(self, new_layers):
        self.layers = new_layers
"""
a = Individual(1)
a.generate_layers([3,5,1])
print(a.inference([.1,-.4,.2]))
"""