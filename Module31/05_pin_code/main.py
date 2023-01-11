import itertools


# for x in itertools.permutations('0123456789', 4):
#     print(*x)


pin_code = itertools.product('0123456789', repeat=4)
print('Результат работы программы:')
for number in pin_code:
    print(*number)

