def sum_me(*args, summ=0):
    for num in args:
        if isinstance(num, int):
            summ += num
        else:
            for x in num:
                a = sum_me(x)
                summ += a
    return summ
# print(sum_me([[1, 2, [3]], [1], 3]))