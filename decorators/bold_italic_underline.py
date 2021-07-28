def make_bold(function):
    def wrapper(*args):
        func = function(*args)
        return f"<b>{func}</b>"
    return wrapper


def make_italic(function):
    def wrapper(*args):
        func = function(*args)
        return f"<i>{func}</i>"
    return wrapper


def make_underline(function):
    def wrapper(*args):
        func = function(*args)
        return f"<u>{func}</u>"
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
