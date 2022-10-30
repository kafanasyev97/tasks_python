user = int(input('Введите длину списка: '))
first_list = [1 if x % 2 == 0 else x % 5 for x in range(user)]
print(first_list)