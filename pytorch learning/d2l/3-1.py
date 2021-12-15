import numpy as np
import torch
import math
import matplotlib.pyplot as plt
""" 
    linear regression basic
 """

def normal(x, mu, sigma):
    p = 1 / math.sqrt(2 * math.pi * sigma**2)
    return p * np.exp(-1 * (x - mu)**2 / (2 * sigma**2))

# x axis 
x = np.arange(-7, 7, 0.01)

# parameters of normal distribution
param = [(0, 1), (0, 2), (3, 1)]

# normal distribution
plt.plot(x, normal(x, param[0][0], param[0][1]))
plt.plot(x, normal(x, param[1][0], param[1][1]))
plt.plot(x, normal(x, param[2][0], param[2][1]))
plt.xlabel('x')
plt.ylabel('p(x)')
plt.legend([f'mean:{mu}, sigam:{sigma}' for mu, sigma in param])
plt.show()
