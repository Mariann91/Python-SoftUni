class reverse_iter:

    def __init__(self, iterable: list) -> None:
        self.iterable = iterable
        self.counter = len(iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.counter == -1:
            raise StopIteration

        index = self.counter
        self.counter -= 1

        return self.iterable[index]
