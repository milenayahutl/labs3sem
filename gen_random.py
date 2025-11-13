import random

def gen_random(num, min, max):
    for _ in range(num):
        yield random.randint(min, max)

if __name__ == '__main__':
    print(list(gen_random(5, 1, 3)))