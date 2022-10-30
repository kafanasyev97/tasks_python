total = list('I' * int(input('Количество палок: ')))
for i in range(1, int(input('Количество бросков: ')) + 1):
    for j in range(int(input(f'Бросок {i}. Сбиты палки с номера ')) - 1, int(input('по номер '))):
        total[j] = '.'
new_str = ''
for sym in total:
    new_str += sym

print('Результат:', new_str)
