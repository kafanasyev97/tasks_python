def need_func(*args, result=[]):
    for elem in args:
        for num in elem:
            if isinstance(num, int):
                result.append(num)
            else:
                a = need_func(num)
    return result

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print(need_func(nice_list))


