def field(items, *args):
    assert len(args) > 0

    for item in items:
        if len(args) == 1:    #если передан 1 элемент, возвращаем только его
            key = args[0]
            if key in item and item[key] is not None:
                yield item[key]
        else:                 #если несколько, возвращаем словарь с нужными
            filtered = {}
            for key in args:
                if key in item and item[key] is not None:
                    filtered[key] = item[key]
            if filtered:
                yield filtered

goods = [
    {'title': 'Ковер', 'price': 1700, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'},
    {'title': 'Стол', 'price': 2100},
    {'title': 'Кресло'}
]

print(list(field(goods, 'title')))
print(list(field(goods,'title', 'price')))
print(list(field(goods,'title','price', 'color')))