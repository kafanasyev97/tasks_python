def slicer(cort, number):
    if number not in cort:
        return {}
    for x in cort:
        if x == number:
            b = cort[cort.index(x):]
            break
    for x in range(1, len(b)):
        if b[x] == number:
            b = b[:x + 1]
            break
    return tuple(b)

print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))