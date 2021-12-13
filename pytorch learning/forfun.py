import numpy as np
import torch
import torch.nn as nn
x = torch.randn(10, 3, requires_grad = True)
w = torch.randn(12, 10, requires_grad = True)
b = torch.randn(12, 3,requires_grad = True)
print(x)
print(x.size(), w.size(), b.size())
y = torch.mm(w, x) + b
print(y)


