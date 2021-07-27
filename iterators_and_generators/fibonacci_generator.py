def get_fibonacci(n):
    if n <= 1:
        return n
    return get_fibonacci(n - 1) + get_fibonacci(n - 2)


def fibonacci():
    n = 0
    while True:
        yield get_fibonacci(n)
        n += 1


generator = fibonacci()
for i in range(5):
    print(next(generator))
