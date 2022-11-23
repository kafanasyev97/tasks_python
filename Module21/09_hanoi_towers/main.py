def move(n, start, finish):
    if n > 0:
        tmp = 6 - start - finish
        move(n - 1, start, tmp)
        print(f'Переложить диск {n} со стержня номер {start} на стержень номер {finish}')
        move(n - 1, tmp, finish)
n=int(input('Введите количество дисков: '))
move(n, 1, 3)