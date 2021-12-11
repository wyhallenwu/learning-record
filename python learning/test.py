
# list comprehension
import os
import torch 
import torch.nn as nn
print([d for d in os.listdir('.')])
L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() if isinstance(s, str) else s for s in L])

'''
generator
1. () with list comprehension
2. generator function using yield
'''
g = (x * x for x in range(10))
for n in g:
    print(n)
#next(g) record the next, so if continue next(g), here will raise stopiteration error

#fibonacci using generator
def fib(max):
    n, a, b = 0, 0 ,1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'
f = fib(6)
for i in f:
    print(i)

def pascal_triangle(rows):
    L = [1]
    count = 0
    while(count < rows):
        yield(L)
        for n in range(len(L)):
            if n == 0:
                test_L = [1]
            else:
                test_L.append(L[n] + L[n-1])
        test_L.append(1)
        count = count + 1
        L = test_L
    return 'done'

for i in pascal_triangle(5):
    print(i)


#decorator
def deco(func):
    def deco_(*args, **kwargs):
        print("hello")
        print("test")
        return func(*args, **kwargs)
    return deco_

@deco
def test(data):
    print("hello world")
    print(data)

test(10)

def info(value):
    def deco(func):
        def wrapper(*args, **kwargs):
            print(value)
            return func(*args, **kwargs)
        return wrapper
    return deco

@info('123')
def test2():
    print("hello")

test2()

list = [i + (9 - 5) // 2 for i in range(5)]
list.reverse()
print(list)

for i in range(5, -1, -1):
    print(i)

print(torch.Tensor([0.485, 0.456, 0.406]).view(1, 3, 1, 1))

m = nn.LeakyReLU(0.1)
input = torch.randn(2)
print(isinstance(m(input),torch.Tensor))

ten1 = torch.zeros(5, 3)
ten2 = None
ten2 = torch.zeros_like(ten1)
print(ten2.size())
