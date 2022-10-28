total_people = int(input('Кол-во человек: '))
number = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {number}-й человек.')
mens_list = list(range(1, total_people + 1))
out = 0

for _ in range(total_people - 1):
   print('Текущий круг людей', mens_list)
   start_count = out % len(mens_list)
   out = (start_count + number - 1) % len(mens_list)
   print('Начало счёта с номера', mens_list[start_count])
   print('Выбывает человек под номером', mens_list[out])
   mens_list.remove(mens_list[out])
   print()
print('Остался человек под номером', mens_list)