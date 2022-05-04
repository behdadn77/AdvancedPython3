def foo():
	return 1

def bar():
	yield 2
	yield 3
	yield 4
	yield 5

print(foo())
print(bar())

b=bar()

print(b.__next__())
print(b.__next__())
print(next(b))
print(next(b))
