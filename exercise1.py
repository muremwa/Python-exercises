# Write a decorator which wraps functions to log function arguments and the
# return value on each call. Provide support for both positional and named
# arguments (your wrapper function should take both *args and **kwargs and print them both):

# >>> @logged
# ...def func(*args):
# ... return 3 + len(args)
# >>> func(4, 4, 4)
# you called func(4, 4, 4) it returned 6
# 6

from functools import wraps


# function implementation
def logit(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print('you called {}{}'.format(func.__name__, args))
        val = func(*args, **kwargs)
        print('it returned {}'.format(val))
        return val
    return wrap


@logit
def fun(*args):
    return 3 + len(args)


# as a class
class logitc():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('you called {}{}'.format(self.func.__name__, args))
        val = self.func(*args, **kwargs)
        print('it returned ', val)
        return val


@logitc
def fun_c(*args):
    return 3 + len(args)


print('decorator as a function')
print('\n')
print(fun(4, 4, 4))
print('='*50)
print('decorator as a class')
print('\n')
print(fun_c(4, 4, 4))
