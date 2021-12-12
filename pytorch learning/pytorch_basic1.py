import torch
import torchvision
import torch.nn as nn
import numpy as np
import torchvision.transforms as transforms

# basic autograd 1 =========================================
x = torch.tensor(1., requires_grad = True)
w = torch.tensor(2., requires_grad = True)
b = torch.tensor(3., requires_grad = True)
""" In pytorch, tensor() is different from Tensor()
    the former is a function and the latter is a class
    there are many methods in Tensor we can use, for example Tensor.new_tensor
 """

# build a computational graph
y = w * x + b

# compute gradients
y.backward()

# print out the gradients
print(f'x: {x.grad}, w: {w.grad}, b: {b.grad}')

# basic autograd 2 ==========================================
x = torch.randn(10, 3)
y = torch.randn(10, 2)

# build a fully connected layer
linear = nn.Linear(3, 2)
print(f'weight:{linear.weight}, bias: {linear.bias}')

# build a loss function and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(linear.parameters(), lr = 0.01)

# forward pass
pred = linear(x)
# print(f'pred: {pred}')

# compute loss
loss = criterion(pred, y)
print(f'loss: {loss.item()}')

# backward pass
loss.backward()

# print out the gradients
print(f'dl/dw: {linear.weight.grad}, dl/db: {linear.bias.grad}')

# i-step gradient descent
for i in range(100):
    optimizer.step()
    # print out the results after 1-step gradient descent
    pred = linear(x)
    loss = criterion(pred, y)
    print(f'loss after {i} step optimization: {loss.item()}')


# loading data from numpy==============================================
x = np.array([[1, 2], [3, 4]])
print(np.shape(x))

# conver numpy to tensor
y = torch.from_numpy(x)

# convert torch tensor to a numpy array
z = y.numpy()

# input pipeline=====================================================

# download dataset CIFAR-10, it is included in the torchvision.datasets
# the detailed information of this dataset is https://www.cs.toronto.edu/~kriz/cifar.html
train_dataset = torchvision.datasets.CIFAR10(root = '/data', train = True, transform = transforms.ToTensor(), download = True)

# fetch one data pair
image, label = train_dataset[0]
print(image.size())
print(label)

# dataloader (provide queues and threads in a simple way)
train_loader = torch.utils.data.DataLoader(dataset = train_dataset, batch_size = 64, shuffle = True)

# when iteration starts, queue and thread start to laod data from files
data_iter = iter(train_loader)

# mini-batch images and labels
images, labels = data_iter.next()

# actual usage of the dataloader
for images, labels in train_loader:
    # training here TODO
    pass

