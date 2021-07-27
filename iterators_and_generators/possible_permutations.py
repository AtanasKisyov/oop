from itertools import permutations


def possible_permutations(seq):
    result = permutations(seq)
    for el in result:
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]
