# Communication with generators


def test():
    val = yield 1 # ln 12
    print(val)  # "pokemon" is used here, ln 14
    yield 2  # when pokemon was sent, ln 14, ln 17
    yield 3


gen = test()
print(next(gen))
# value is passed as return value from the yield keyword
print(gen.send("pokemon"))
# throws exception inside the generators
# the exception is raised at the same spot the yield was called
gen.throw(Exception("My Custom Error"))