import numpy as np
import math

# activation functions
def activation(x, func):
    """A ton of activation functions"""
    if func == 0:
        return 1/(1 + np.exp(-x))

    elif func == 1:
        return math.tanh(x)

    elif func == 2:
        return x * (x > 0)

    elif func == 3:
        return max(.05*x, x)

    elif func == 4:
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum()

    elif func == 5:
        return x

    else:
        print("Not a activation function!")