class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = 0
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):

        if self.counter == self.number:
            raise StopIteration

        self.counter += 1
        self.index += 1

        if self.index == len(self.sequence):
            self.index = 0

        return self.sequence[self.index]
      
