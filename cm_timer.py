import time
from time import sleep
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start
        print(f'time: {elapsed:.2f}s')

@contextmanager
def cm_timer_2():
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f'time: {elapsed:.2f}s')


if __name__ == '__main__':
    print('ждем 1.5 секунды')
    with cm_timer_1():
        sleep(1.5)

    print('Сумма (цикл):')
    with cm_timer_2():
        s = 0
        for i in range(1000000):
            s+=1

    print('Сумма (функция):')
    with cm_timer_2():
        s = sum(range(1000000))
