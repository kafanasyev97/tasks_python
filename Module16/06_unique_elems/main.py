first_list = []
second_list = []
for i_one in range(3):
    user = int(input(f'Введите {i_one + 1} число для первого списка: '))
    first_list.append(user)

for i_two in range(7):
    user = int(input(f'Введите {i_two + 1} число для второго списка: '))
    second_list.append(user)

print(f'Первый список: {first_list}')
print(f'Второй список: {second_list}')

first_list.extend(second_list)

for number in first_list:
    for _ in range(first_list.count(number) - 1):
        first_list.remove(number)


print('Новый первый список с уникальными элементами:', first_list)