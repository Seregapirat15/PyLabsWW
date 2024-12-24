def field(items, *args):
    assert len(args) > 0
    for item in items:
        if len(args) == 1:
            value = item.get(args[0])
            if value is not None:
                yield value
        else:
            result = {}
            for arg in args:
                value = item.get(arg)
                if value is not None:
                    result[arg] = value
            if result:
                yield result

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]

for value in field(goods, 'title'):
    print(value)  # Output: 'Ковер', 'Диван для отдыха'

for result in field(goods, 'title', 'price'):
    print(result)  # Output: {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха'}