class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.current_outer = 0
        self.current_inner = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_outer < len(self.list_of_list):
            current_inner_list = self.list_of_list[self.current_outer]
            if self.current_inner < len(current_inner_list):
                item = current_inner_list[self.current_inner]
                self.current_inner += 1
                return item
            else:
                self.current_outer += 1
                self.current_inner = 0
                return next(self)
        else:
            raise StopIteration


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
