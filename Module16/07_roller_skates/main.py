skates = int(input('Кол-во коньков: '))
skates_list = []
for i_size in range(skates):
    size_skates = int(input(f'Размер {i_size + 1}-й пары: '))
    skates_list.append(size_skates)

people = int(input('Кол-во людей: '))
people_list = []
for i_people in range(people):
    size_people = int(input(f'Размер ноги {i_people + 1}-ого человека: '))
    people_list.append(size_people)

count = 0

for i in people_list:
    for n in skates_list:
        if i <= n:
            count += 1
            skates_list.remove(n)
            break
print('Наибольшее кол-во людей, которые могут взять ролики:', count)
