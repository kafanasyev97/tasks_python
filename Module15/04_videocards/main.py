total_cards = int(input('Количество видеокарт: '))
cards_list = []
new_list = []

for i in range(1, total_cards + 1):
    user = int(input(f'{i} Видеокарта: '))
    cards_list.append(user)

maximum = 0

for i in cards_list:
    if i > maximum:
        maximum = i

for i in cards_list:
    if i != maximum:
        new_list.append(i)

print('Старый список видеокарт:', cards_list)
print('Новый список видеокарт:', new_list)
