def test():
    val = yield 1 # ln 9
    print(val)  # "pokemon" is used here, ln 10
    yield 2  # when pokemon was sent, ln 10, ln 11
    yield 3


gen = test()
print(next(gen))
print(gen.send("pokemon"))
gen.throw(Exception("My Custom Error"))
# print(next(gen))