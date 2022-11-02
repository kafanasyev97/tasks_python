def palindrom(string):
    need_dict = {}
    for i in string:
        need_dict[i] = need_dict.get(i, 0) + 1

    need_count = 0
    for i in need_dict.values():
        if i % 2 != 0:
            need_count += 1

    return need_count

user = input('Введите строку: ')

count = palindrom(user)
if count <= 1:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')

