def need_func(elem, result):
    if elem[1] == '+':
        result += (int(elem[0]) + int(elem[2]))
    elif elem[1] == '-':
        result += (int(elem[0]) - int(elem[2]))
    elif elem[1] == '*':
        result += (int(elem[0]) * int(elem[2]))
    elif elem[1] == '/':
        result += (int(elem[0]) / int(elem[2]))
    else:
        raise Exception
    return result


summ = 0
with open('calc.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.split()
        try:
            summ = need_func(line, summ)
        except Exception:
            print('Обнаружена ошибка в строке:', ' '.join(line), end='')
            answer = input('   Хотите исправить? ').lower()
            if answer == 'да':
                new_string = input('Введите исправленную строку: ').split()
                summ = need_func(new_string, summ)
print('Сумма результатов:', summ)
