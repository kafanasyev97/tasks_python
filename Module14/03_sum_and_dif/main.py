def first_fun(number):
    summ = 0
    while number != 0:
        one_num = number % 10
        number //= 10
        summ += one_num
    return summ

def second_fun(number):
    count = 0
    while number != 0:
        one_num = number % 10
        number //= 10
        count += 1
    return count


number = int(input('Введите число: '))

print('Сумма чисел:', first_fun(number))
print('Количество цифр в числе:', second_fun(number))
print('Разность суммы и количества цифр:', first_fun(number) - second_fun(number))
