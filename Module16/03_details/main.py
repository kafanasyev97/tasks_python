shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100],
        ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
detail = input('Название детали: ')
count = 0
summ = 0

for i_el in range(len(shop)):
    if shop[i_el][0] == detail:
        count += 1
        summ += shop[i_el][1]

print('Кол-во деталей —', count)
print('Общая стоимость —', summ)