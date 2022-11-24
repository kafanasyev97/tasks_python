def need_func(*args):
    minimum = min(len(elem) for elem in args)
    return [tuple(i_element[index] for i_element in args) for index in range(minimum)]


# syms_str = 'abcd'
# nums_tpl = (10, 20, 30, [1, 33, 2])
# print(need_func(syms_str, nums_tpl))
