# yield from allows us to pass any next(), send() and throw()
# into an inner most nested generator
# if the inner generator returns a value, it is also the
# return value of yield from 


def inner():
    # a generator inside of another generator
    inner_result = yield 2 # 5
    print("inner", inner_result) # 7 (place of the last yield)
    return 3 # 8


def outer():
    yield 1 # 2
    val = yield from inner() # 4, 8
    print("outer", val) # 9
    yield 4 # 9


gen = outer()
print(next(gen)) # 1

print(next(gen)) # Goes inside inner() automatically # 3

print(gen.send("abc")) # 6

# ouput:
# 1
# 2
# inner abc
# outer 3
# 4