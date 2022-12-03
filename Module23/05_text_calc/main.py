summ = 0
with open('calc.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.split()
        try:
            summ += eval(' '.join(line))
        except Exception:
            print('Обнаружена ошибка в строке:', ' '.join(line), end='')
            answer = input('   Хотите исправить? ').lower()
            if answer == 'да':
                new_string = input('Введите исправленную строку: ').split()
                summ += eval(' '.join(new_string))
print('Сумма результатов:', summ)
