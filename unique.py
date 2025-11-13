from gen_random import gen_random

class unique:
    def __init__(self, items, **kwargs):
        self.items = iter(items)  #превращаем в итератор
        self.seen = set()
        self.ignore_case = kwargs.get('ignore_case', False) #чтобы учитывать или не учитывать регистр букв
                                                            # **kwargs — способ передать в функцию любое количество
                                                            #именованных аргументов (ключ=значение).
    def __next__(self):
        while True:
            try:
                item = next(self.items)
            except StopIteration:
                raise StopIteration

            key = item
            if self.ignore_case and isinstance(item, str):   #если важен регистр, для проверки повторов делает временный key нижнего регистра
                key = item.lower()

            if key not in self.seen:
                self.seen.add(key)
                return item


    def __iter__(self):
        return self

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 3, 2, 4, 4]
    print(list(unique(nums)))

    random_nums = gen_random(10, 1, 3)
    print(list(unique(random_nums)))

    letters = ['a', 'A', 'b', 'b', 'C', 'c']
    print(list(unique(letters)))
    print(list(unique(letters, ignore_case=True)))