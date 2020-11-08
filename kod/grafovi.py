import matplotlib.pyplot as plt
import numpy as np
import math


def sigmoid(linspace):
    brojevi = list()
    for x in linspace:
        brojevi.append(1 / (1 + math.exp(-x)))
    return brojevi


def tanh(linspace):
    brojevi = list()
    for x in linspace:
        brojevi.append(math.tanh(x))
    return brojevi


def relu(linspace, alpha=None):
    brojevi = list()
    for x in linspace:
        if alpha is not None:
            if x <= 0:
                brojevi.append(alpha*x)
            else:
                brojevi.append(x)
        else:
            brojevi.append(max(0, x))
    return brojevi


plt.style.use('seaborn-whitegrid')
linspa = np.arange(-10., 10., 0.1)
x = [-10, 0,  10]
y = [0, 0, 1]
#fun = relu(linspa)
fun = sigmoid(linspa)
plt.figure()
#plt.plot(linspa, fun, linewidth=2)
plt.xlabel('x', size=12)
plt.ylabel('f(x)', size=12)
#plt.step(x, y)
plt.plot(linspa, linspa)
plt.axhline(color='black', linewidth=0.5)
plt.axvline(color='black', linewidth=0.5)
plt.ylim(-1.25, 1.25)
plt.xlim(-10, 10)
plt.show()
