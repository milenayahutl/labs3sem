import random

def gen_random(num, min, max):
    for _ in range(num):
        yield random.randint(min, max)

print(list(gen_random(5, 1, 3)))