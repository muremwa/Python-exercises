# Write a generator function which returns a few values.
# Launch it.
# Retrieve a value using next (the global function).
# Retrieve a value using next (a method of the generator object).
# Throw an exception into the generator using throw (a method).
# Look at the traceback.


def gen_v():
    for i in range(6, 20):
        yield i


gens = gen_v()
print(next(gens))
print(gens.__next__())
# gens.throw(ValueError)
