user = int(input('Введите число: '))
for result in range(user, 1, -1):
    if user % result == 0:
        number = result
print('Наименьший делитель, отличный от единицы:', number)