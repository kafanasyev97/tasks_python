n = int(input('Введите число: '))
number_list = []

for i in range(1, n + 1):
    if i % 2 != 0:
        number_list.append(i)

print(f'Список из нечётных чисел от одного до {n}: {number_list}')