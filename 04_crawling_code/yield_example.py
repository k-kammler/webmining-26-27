def abc_generator():
    yield("a")
    yield("b")
    yield("c")

x = abc_generator()

print(next(x))
print(next(x))
print(next(x))
