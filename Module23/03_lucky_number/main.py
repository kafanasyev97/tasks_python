import random

summ = 0
with open('out_file.txt', 'a') as file:
    try:
        while summ < 777:
            n = random.randint(1, 13)
            if n == 13:
                raise Exception('Вас постигла неудача!')
            number = int(input('Введите число: '))
            file.write(str(number) + '\n')
            summ += number
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
    except Exception as esc:
        print(esc)
with open('out_file.txt', 'r') as second_file:
    print('\nСодержимое файла out_file.txt:')
    for line in second_file:
        print(line.strip())
