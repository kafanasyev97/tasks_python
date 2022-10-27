total_containers = int(input('Количество контейнеров: '))
containers_list = []

for i in range(total_containers):
    one_container = int(input('Введите вес контейнера: '))
    if one_container > 200:
        while one_container > 200:
            one_container = int(input('Ошибка! Вес контейнера не должен превышать 200. Введите вес еще раз: '))
    containers_list.append(one_container)

user_weight = int(input('Введите вес нового контейнера: '))
count = 1

for i in containers_list:
    if user_weight > i:
        break
    elif user_weight <= i:
        count += 1

print('Номер, который получит новый контейнер:', count)
