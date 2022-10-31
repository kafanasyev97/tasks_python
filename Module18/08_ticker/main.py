first_str = input('Первая строка: ')
second_str = input('Вторая строка: ')
count = 0
for i in range(len(first_str)):
    if first_str == second_str:
        print('Первая строка получается из второй со сдвигом', count)
        break
    second_str = ''.join([second_str[-1], second_str[:-1]])
    count += 1
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
