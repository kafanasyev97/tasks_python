films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
user_count = int(input('Сколько фильмов хотите добавить? '))
user_list = []

for _ in range(user_count):
    count = 0
    choice = input('Введите название фильма: ')
    for text in films:
        if text == choice:
            user_list.append(choice)
            count += 1
    if count == 0:
        print('Ошибка: фильма', choice, 'у нас нет :(')

print('Ваш список любимых фильмов:', user_list)