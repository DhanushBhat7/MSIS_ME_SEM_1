import numpy as np

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.01):

    return np.where(x > 0, x, alpha * x)

def gelu(x):
    return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) *(x + 0.044715 * x**3)))

def softmax(x):
    x = np.asarray(x, dtype=np.float64)
    exp_values = np.exp(x - np.max(x))
    return exp_values / np.sum(exp_values)


def one_hot(labels, num_classes):
    output = np.zeros((len(labels), num_classes),dtype=np.float64)
    output[np.arange(len(labels)), labels] = 1
    return output

def l2_normalize(x, eps=1e-12):
    magnitude = np.sqrt(np.sum(x**2))
    return x / max(magnitude, eps)