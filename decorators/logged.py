def logged(function):
    def wrapper(*args):
        result_from_func = function(*args)
        text = f"you called {function.__name__}({', '.join([str(el) for el in args])})\nit returned {result_from_func}"
        return text
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
