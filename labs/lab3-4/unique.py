class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()

    def __next__(self):
        for item in self.items:
            if self.ignore_case and isinstance(item, str):
                item_key = item.lower()
            else:
                item_key = item

            if item_key not in self.seen:
                self.seen.add(item_key)
                return item

        raise StopIteration

    def __iter__(self):
        return self

data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
unique_data = Unique(data)
for item in unique_data:
    print(item)  # prints 1, 2

data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
unique_data = Unique(data)
for item in unique_data:
    print(item)  # prints 'a', 'A', 'b', 'B'

unique_data = Unique(data, ignore_case=True)
for item in unique_data:
    print(item)  # prints 'a', 'b'