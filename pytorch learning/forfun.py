import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
# estimate y = x^2
x = np.linspace(0, 10, 50)
y = np.array([i ** 2 for i in x])
print(y)

x_ = torch.from_numpy(x)
y_ = torch.from_numpy(y)

# model
# model = nn.Linear()
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.layer1 = nn.Linear(1, 1)
        self.layer2 = nn.Linear(1, 1)
        self.layer3 = nn.Linear(1, 1)
    def forward(self, x_, k):
        out = F.relu(self.layer1(x_[k]))
        out = F.relu(self.layer2(x_[k]))
        out = F.relu(self.layer3(x_[k]))
        return out

model = Model()
pred_y = model.forward(x_)

# loss
loss_fn = nn.MSELoss()
loss = loss_fn(y_, pred_y)
loss.backward()

# optimizer
optimizer = nn.optim.SGD(model.parameters(), lr = 0.01)

epoch =  10
i = 0
while(i <= epoch):
    for iters in range(x_.size()):
        optimizer.step()
        pred_y = model.forward(x_, iter)
        loss = loss_fn(y_[iters], pred_y)
        print(f'loss in {i}_epoch {iters}_iter: {loss}')
        i += 1
    