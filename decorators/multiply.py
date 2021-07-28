def multiply(times):
    def decorator(function):
        def wrapper(number):
            num = function(number)
            return num * times
        return wrapper
    return decorator


@multiply(10)
def add_ten(number):
    return number + 10


print(add_ten(5))


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))
