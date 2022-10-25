def reve(number):
    flag = True
    whole = ''
    fraction = ''
    for symbol in number:
        if symbol == '.':
            flag = False
        elif flag:
            whole += symbol
        else:
            fraction += symbol
    whole = int(whole)
    fraction = int(fraction)
    n1 = 0
    n2 = 0
    while whole != 0:
        help_whole = whole % 10
        whole //= 10
        n1 = n1 * 10
        n1 += help_whole

    while fraction != 0:
        help_fraction = fraction % 10
        fraction //= 10
        n2 = n2 * 10
        n2 += help_fraction

    help_whole = str(n1)
    help_fraction = str(n2)


    rev = float(help_whole + '.' + help_fraction)
    return rev

number1 = input('Введите первое число: ')
number2 = input('Введите второе число: ')

result1 = reve(number1)
result2 = reve(number2)
total = result1 + result2

print('Первое число наоборот:', result1)
print('Второе число наоборот:', result2)
print('Сумма:', total)


