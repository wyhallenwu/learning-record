# decorator testing. Date: 2021-12-11
# two aspects:
# 1. decorator for function
# 2. decorator for class
# or you can use "from functools import wraps"

#for function
print("for function:==========================")
# without parameter
print("without parameter:")
def decorator1(func):
    def wrapper():  
        print("call from decorator1.")
        func()
    return wrapper
    

@decorator1
def decoed1():
    print("call from decoed1")
decoed1()
# we try naive way to do it
print("\nnaive way to explain how we decorate")
def decoed1_naive():
    print("call from decoed1")

decoed1_naive = decorator1(decoed1_naive)
decoed1_naive() # we can find the results of decoed1 and decoed1_naive are the same 

#with parameters
print("\nwith parameters: ")
def decorator2(func):
    def wrapper(*args, **kwargs): # using two parts to receive parameters
        print("call from decorator2")
        func(*args, **kwargs) # the parameter should choose from args
    return wrapper
@decorator2
def decoed2(data):
    print(f"data is: {data}")

decoed2(10)
print("\n")

def decorator3(data):
    print("*")
    def wrapper(func): # this can be only used in the first decorator
        print(f'wrapper layer data is: {data}')
        def inner_wrapper(*args, **kwargs):
            print(f'inner wrapper data is: {data}')
            func(*args, **kwargs)
            # data = data + 10 : this operation is wrong
            print(f'after func inner data is:{data}')
            #return func
        return inner_wrapper
    return wrapper

@decorator3(10)
def decoed3(para):
    print(f'decoed3 data is: {para}')


decoed3(20)
decoed3(20)
decoed3(20)



# for class
print("\nfor class:=============================")
class decorator_class():
    def __init__(self, func):
        print("call from __init__")
        self.func = func
    def __call__(self):
        self.func()

@decorator_class
def decoed3():
    print("call from decoed3")

# decoed3() if I do this directly, It can't operate because of the uncallable class
decoed3.__call__()
decoed3() # if I define __call__ explicitly, I can use the class as functions
fun = decoed3
fun.func()


# decoed3()
# here we have a simple explaination of closure
# def layer1(data):
#     print("layer1")
#     def layer2():
#         print("layer2")
#         def layer3():
#             print("layer3")
#             print(data)
#         return layer3
#     return layer2

# layer1(10)()()
