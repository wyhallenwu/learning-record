import time
def deco_timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'consume time: {end - start}')
    return wrapper

@deco_timer
def count():
    list = [x * x for x in range(100000)]

count()