all_names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
need_names = []

for i in range(len(all_names)):
    if i % 2 == 0:
        need_names.append(all_names[i])

print('Первый день:', need_names)
