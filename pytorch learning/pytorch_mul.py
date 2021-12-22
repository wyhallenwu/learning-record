import numpy as np
import torch
""" 
How pytorch do multiply 
1. *, @
2. torch.dot(), torch.mul(), torch.mm(), torch.bmm()
3. torch.matmul()
"""
# vector mul
x = torch.randn(3, 1)
y = torch.randn(1, 3)

# dot multiply
z_dot1  = x * y  # support matrix mul
print(z_dot1)
z_dot2 = torch.mm(x, y)
z_dot3 = x @ y
print(z_dot1 == z_dot2)
print(z_dot3.size())

# element-wise mul which is different from numpy
x1 = torch.randn(3, 2)
y1 = torch.randn(3, 2)
z_ele1 = x1 * y1 # here is element-wise, notice line-13
z_ele2 = torch.mul(x1, y1)
print(z_ele1 == z_ele2)
print(z_ele1.size())

# torch.dot() : different from numpy.dot(), only support 1-d vector
x3 = torch.randn(2)
print(x3)
y3 = torch.randn(2)
z3 = torch.dot(x3, y3)
print(z3)

# torch.bmm(): support vec1=B*n*m and vec2=B*m*k where B is usually batch-size
# B must be the same
x4 = torch.randn(12, 1).reshape(2, 2, 3)
y4 = torch.randn(12, 1).reshape(2, 3, 2)
z4 = torch.bmm(x4, y4)
print(z4)

# torch.matmul(): support broadcast
x5 = torch.randn(3, 3)
y5 = torch.randn(3, 4)
z5 = torch.matmul(x5, y5)
print(z5, z5.size())