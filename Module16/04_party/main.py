guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while True:
    print(f'\nСейчас на вечеринке {len(guests)} человек: {guests}')
    user = input('Гость пришёл или ушёл? ')
    if user == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    name_guest = input('Имя гостя: ')
    if user == 'пришел':
        if len(guests) == 6:
            print(f'Прости, {name_guest}, но мест нет.')
        else:
            print(f'Привет, {name_guest}!')
            guests.append(name_guest)
    elif user == 'ушел':
            for i in guests:
                if i == name_guest:
                    print(f'Пока, {name_guest}!')
                    guests.remove(name_guest)
                    break
            else:
                print('Стоп! Такого гостя нет на вечеринке!')