need_file = open('zen.txt', 'r')
ssd = []
for x in need_file:
    ssd.append(x)
need_file.close()
ssd.reverse()
for x in ssd:
    if '\n' in x:
        print(x)
    else:
        print(x, '\n')


# Решение через функцию
# def need_func(g, z):
#     need_file = open(g, z)
#     one_list = []
#     for x in need_file:
#         one_list.append(x)
#     need_file.close()
#     one_list.reverse()
#     return one_list
#
#
# a = 'zen.txt'
# b = 'r'
# ssd = need_func(a, b)
# for x in ssd:
#     if '\n' in x:
#         print(x)
#     else:
#         print(x, '\n')
