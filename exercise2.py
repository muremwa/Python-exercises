# Write a decorator to cache function invocation results.
# Store pairs arg:result in a dictionary in an attribute of the function object.


def cache(func):
    """ this is a decorator to cache the results of a function """
    func.cache = {}

    def wrapper(*args):
        assert len(args) == 1
        if args[0] in func.cache:
            val = func.cache[args[0]]
        else:
            val = func(*args)
            func.cache[args[0]] = val

        return val

    return wrapper


@cache
def fibonacci(n):
    assert n >= 0
    if n < 2:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(50))
