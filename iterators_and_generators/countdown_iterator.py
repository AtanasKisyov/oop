class countdown_iterator:

    def __init__(self, count):
        self.count = count
        self.counter = self.count

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < 0:
            raise StopIteration
        helper = self.counter
        self.counter -= 1
        return helper


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")