asd = dict()
while True:
    deist = int(input('\nВведите номер действия:\n1. Добавить контакт\n2. Найти человека '))
    if deist == 1:
        user = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').title().split())
        if user in asd:
            print('Такой человек уже есть в контактах.')
        else:
            number = int(input('Введите номер телефона: '))
            asd[user] = number
        print('Текущий словарь контактов:', asd)
    elif deist == 2:
        user_2 = input('Введите фамилию для поиска: ').title()
        flag = False
        for index, value in asd.items():
            if user_2 in index:
                print(*index, value)
                flag = True
        if not flag:
            print('Контакта с такой фамилией нет!')
    else:
        print('Такого действия нет!')
