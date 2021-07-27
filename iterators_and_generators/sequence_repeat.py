class sequence_repeat:

    def __init__(self, seq, number):
        self.sequence = seq
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.number:
            raise StopIteration
        i = self.index
        self.index += 1
        return self.sequence[i % len(self.sequence)]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')