import random

count = int(input('Введите количество элементов в списке: '))
first_list = [random.randint(0, 2) for x in range(count)]
second_list = [x for x in first_list if x != 0]
print('Список до сжатия:', first_list)
print('Список после сжатия:', second_list)