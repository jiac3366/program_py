def howlong(a, *other):
    print(len(other))
    print(other)
    print(other[0])
    print(other[1])

if __name__ == '__main__':
    howlong(1, 3 ,43 ,43, 32, 32)