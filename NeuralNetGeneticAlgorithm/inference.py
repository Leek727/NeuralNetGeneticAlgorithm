import numpy as np

# layer format = [
# [
#   [n1w1, n2w1],
#   [n1w2, n2w2],
# ]
# [b1,b2,b3]
# ]

# activation functions


def activation(x, func):
    """A ton of activation functions"""
    if func == 0:
        return 1/(1 + np.exp(-x))

    elif func == 1:
        return (np.exp(x) - np.exp(-x))/(np.exp(x) + np.exp(-x))

    elif func == 2:
        return x * (x > 0)

    elif func == 3:
        return max(.05*x, x)

    elif func == 4:
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum()

    else:
        print("Not a activation function!")


# activations per layer
# 0 = sigmoid, 1 = tanh, 2 = ReLU, 3 = Leaky ReLU, 4 = Softmax
activations = [1, 0]

# inference
"""layers = [
    [
        [
            [-2.1157231, 2.727366, 2.17497],
            [2.9331796, -1.4264885, 2.3271747]
        ],
        [0.87192124, 0.2856308, -0.4019518]
    ], 
    [
        [
            [-3.405584], [-3.4246705], [2.8490212]
        ], 
        [0.74746406]
    ]
]"""
layers = []
with open("fmtweight.txt", "r") as f:
    layers = eval(f.read())


input_layer = [1, 0]
for act_index, layer in enumerate(layers):
    weights = layer[0]
    biases = layer[1]

    # matrix multiply the input layer by the weights and add biases to get output
    neurons = np.add(
        np.matmul(input_layer, weights),
        biases
    )

    # apply activation function
    for i in range(len(neurons)):
        neurons[i] = activation(neurons[i], activations[act_index])

    input_layer = neurons


print(input_layer)
