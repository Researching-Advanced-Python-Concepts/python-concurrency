# Returning Values from generators
# results in the value being put inside the StopIteration
# exception


def test():
    yield 1
    return "pikachu"


gen = test()
print(next(gen))

try:
    next(gen)
except StopIteration as sti:
    print(sti.value)
