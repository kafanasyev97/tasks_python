def need_func(num):
    if num != 1:
        need_func(num - 1)
    print(num)


num = int(input('Введите num: '))
need_func(num)
