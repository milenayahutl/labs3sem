def field(items, *args):
    assert len(args) > 0

    for item in items:
        if len(args) == 1:
            key = args[0]
            if key in item and item[key] is not None:
                yield item[key]
        else:
            filtered = {}
            for key in args:
                if key in item and item[key] is not None:
                    filtered[key] = item[key]
            if filtered:
                yield filtered

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'},
    {'title': 'Стол', 'price': 2000},
    {'title': 'Кресло'}
]

print(list(field(goods, 'title')))
print(list(field(goods,'title', 'price')))
print(list(field(goods,'title','price', 'color')))