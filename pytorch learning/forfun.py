import numpy as np
import torch
import torch.nn as nn
x = torch.randn(10, 3, requires_grad = True)
# w = torch.randn(12, 10, requires_grad = True)
b = torch.randn(10, 10)

data = np.random.uniform(0, 3, (100, 10, 10))
# print(data)
y = torch.from_numpy(data).float()
print(x)
print(y.type(), b.size())
# y = torch.mm(w, x) + b
# prsint(y)

# model 
model = nn.Linear(3, 10)

# optimizer
optimizer = torch.optim.SGD(model.parameters(), lr = 1e-3)

# loss
loss = nn.MSELoss()

def forward(x):
    return model(x) + b

pred_y = forward(x)

pred_loss = loss(pred_y, y)

epoch = 10
batch_size = 10

for i in range(10):
    optimizer.step()
    pred_y = forward(x)
    pred_loss = loss(pred_y, y)
    pred_loss.backward()
    print(f'loss after {i} optim is: {pred_loss}')
