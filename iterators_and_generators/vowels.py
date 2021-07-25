class vowels:

    vowel = {
        "A", "E", "Y", "U", "I", "O",
        "a", "e", "y", "u", "i", "o",
    }

    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.text):
            raise StopIteration
        index = self.index
        self.index += 1
        if self.text[index] not in self.vowel:
            return self.__next__()
        return self.text[index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
