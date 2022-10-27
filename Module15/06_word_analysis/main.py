user = input('Введите слово: ')
text_list = list(user)
need_number = 0

for i in text_list:
    count = 0
    for sym in text_list:
        if sym == i:
            count += 1
    if count == 1:
        need_number += 1

print('Количество уникальных букв:', need_number)
