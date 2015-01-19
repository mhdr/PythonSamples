__author__ = 'Mahmood'

def ages():
    yield 1
    yield 2
    yield 3


result=ages()

print(result)

print(next(result))
print(next(result))
print(next(result))