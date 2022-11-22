def need_func(a, b):
    spis = [(a[i_elem], b[i_elem])
             for i_elem in range(min(len(a), len(b)))]
    return spis


# syms_str = 'abcd'
# nums_tpl = (10, 20, 30, [1, 33, 2])
# print(need_func(syms_str, nums_tpl))