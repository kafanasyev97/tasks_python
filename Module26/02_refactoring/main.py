list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]


def square():
    for x in list_1:
        for y in list_2:
            yield x, y, x * y
            if x * y == 56:
                print('Found!!!')
                return


for elem in square():
    print(*elem)
