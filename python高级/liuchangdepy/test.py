from collections import abc
s = 'ABC'
it = iter(s)
print(it)
print(type(it))

while True:
    try:
        print(next(it))
    except StopIteration:
        pass

