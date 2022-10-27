total_count = int(input('Количество клеток: '))
count = []
for i in range(1, total_count + 1):
    cell = int(input(f'Эффективность {i} клетки: '))
    if i > cell:
        count.append(cell)

print('Неподходящие значения:', count)
