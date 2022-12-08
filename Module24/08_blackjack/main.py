import random


class Deck:
    list_card = [
        ['Двойка', 'Пики', 2], ['Двойка', 'Крести', 2], ['Двойка', 'Буби', 2], ['Двойка', 'Черви', 2],
        ['Тройка', 'Пики', 3], ['Тройка', 'Крести', 3], ['Тройка', 'Буби', 3], ['Тройка', 'Черви', 3],
        ['Четыре', 'Пики', 4], ['Четыре', 'Крести', 4], ['Четыре', 'Буби', 4], ['Четыре', 'Черви', 4],
        ['Пятерка', 'Пики', 5], ['Пятерка', 'Крести', 5], ['Пятерка', 'Буби', 5], ['Пятерка', 'Черви', 5],
        ['Шестерка', 'Пики', 6], ['Шестерка', 'Крести', 6], ['Шестерка', 'Буби', 6], ['Шестерка', 'Черви', 6],
        ['Семерка', 'Пики', 7], ['Семерка', 'Крести', 7], ['Семерка', 'Буби', 7], ['Семерка', 'Черви', 7],
        ['Восьмерка', 'Пики', 8], ['Восьмерка', 'Крести', 8], ['Восьмерка', 'Буби', 8], ['Восьмерка', 'Черви', 8],
        ['Девятка', 'Пики', 9], ['Девятка', 'Крести', 9], ['Девятка', 'Буби', 9], ['Девятка', 'Черви', 9],
        ['Десятка', 'Пики', 10], ['Десятка', 'Крести', 10], ['Десятка', 'Буби', 10], ['Десятка', 'Черви', 10],
        ['Валет', 'Пики', 10], ['Валет', 'Крести', 10], ['Валет', 'Буби', 10], ['Валет', 'Черви', 10],
        ['Дама', 'Пики', 10], ['Дама', 'Крести', 10], ['Дама', 'Буби', 10], ['Дама', 'Черви', 10],
        ['Король', 'Пики', 10], ['Король', 'Крести', 10], ['Король', 'Буби', 10], ['Король', 'Черви', 10],
        ['Туз', 'Пики', 11], ['Туз', 'Крести', 11], ['Туз', 'Буби', 11], ['Туз', 'Черви', 11]
    ]


class Player:
    def __init__(self, name):
        self.name = name  # Изначально сделал через comprehensions, но если два одинаковых рандомных числа
        self.ssd = []     # попадаются, то программа ломается. Поэтому такой большой код тут
        num = random.randint(0, len(Deck.list_card) - 1)
        self.ssd.append(Deck.list_card[num])
        num_dop = random.randint(0, len(Deck.list_card) - 1)
        while num_dop == num:
            num_dop = random.randint(0, len(Deck.list_card) - 1)
        self.ssd.append(Deck.list_card[num_dop])
        self.summ = self.ssd[0][2] + self.ssd[1][2]

    def info_user(self):
        print('Выпали карты:')
        print(self.ssd[0][0], self.ssd[0][1])
        print(self.ssd[1][0], self.ssd[1][1])
        print('Ваша сумма карт:', self.summ)

    def cards(self):
        Deck.list_card.remove(self.ssd[0])
        Deck.list_card.remove(self.ssd[1])


user = Player('Виталя')
user.info_user()
user.cards()
comp = Player('Компьютер')
comp.cards()
summ_user = user.summ
summ_comp = comp.summ


while True:
    user_answer = int(input('1 - взять карту. 2 - остановиться: '))
    if user_answer == 1:
        num = random.randint(0, len(Deck.list_card) - 1)
        if summ_user + summ_comp > 21 and Deck.list_card[num][0] == 'Туз':
            summ_user -= 10
        summ_user += Deck.list_card[num][2]
        print('Выпала карта:', Deck.list_card[num][0], Deck.list_card[num][1])
        del Deck.list_card[num]
        print('Ваша сумма карт:', summ_user)
        if summ_user > 21:
            print('Компьютер выйграл!')
            break

        num = random.randint(0, len(Deck.list_card) - 1)
        summ_comp += Deck.list_card[num][2]
        del Deck.list_card[num]
    if user_answer == 2:
        if summ_user > summ_comp or summ_comp > 21:
            print('Игрок выйграл!')
        elif summ_user == summ_comp:
            print('Ничья!')
        else:
            print('Компьютер выйграл!')
        break


# import random
#
#
# list_card = [
#  ['Двойка', 'Пики', 2], ['Двойка', 'Крести', 2], ['Двойка', 'Буби', 2], ['Двойка', 'Черви', 2],
#  ['Тройка', 'Пики', 3], ['Тройка', 'Крести', 3], ['Тройка', 'Буби', 3], ['Тройка', 'Черви', 3],
#  ['Четыре', 'Пики', 4], ['Четыре', 'Крести', 4], ['Четыре', 'Буби', 4], ['Четыре', 'Черви', 4],
#  ['Пятерка', 'Пики', 5], ['Пятерка', 'Крести', 5], ['Пятерка', 'Буби', 5], ['Пятерка', 'Черви', 5],
#  ['Шестерка', 'Пики', 6], ['Шестерка', 'Крести', 6], ['Шестерка', 'Буби', 6], ['Шестерка', 'Черви', 6],
#  ['Семерка', 'Пики', 7], ['Семерка', 'Крести', 7], ['Семерка', 'Буби', 7], ['Семерка', 'Черви', 7],
#  ['Восьмерка', 'Пики', 8], ['Восьмерка', 'Крести', 8], ['Восьмерка', 'Буби', 8], ['Восьмерка', 'Черви', 8],
#  ['Девятка', 'Пики', 9], ['Девятка', 'Крести', 9], ['Девятка', 'Буби', 9], ['Девятка', 'Черви', 9],
#  ['Десятка', 'Пики', 10], ['Десятка', 'Крести', 10], ['Десятка', 'Буби', 10], ['Десятка', 'Черви', 10],
#  ['Валет', 'Пики', 10], ['Валет', 'Крести', 10], ['Валет', 'Буби', 10], ['Валет', 'Черви', 10],
#  ['Дама', 'Пики', 10], ['Дама', 'Крести', 10], ['Дама', 'Буби', 10], ['Дама', 'Черви', 10],
#  ['Король', 'Пики', 10], ['Король', 'Крести', 10], ['Король', 'Буби', 10], ['Король', 'Черви', 10],
#  ['Туз', 'Пики', 11], ['Туз', 'Крести', 11], ['Туз', 'Буби', 11], ['Туз', 'Черви', 11]]
#
#
# summ_user = 0
# summ_comp = 0
#
# for x in range(2):
#     num = random.randint(0, len(list_card) - 1)
#     summ_user += list_card[num][2]
#     print('Выпала карта:', list_card[num][0], list_card[num][1])
#     del list_card[num]
# print('Ваша сумма карт:', summ_user)
#
# for x in range(2):
#     num = random.randint(0, len(list_card) - 1)
#     summ_comp += list_card[num][2]
#     del list_card[num]
#
# while True:
#     user_answer = int(input('1 - взять карту. 2 - остановиться '))
#     if user_answer == 1:
#         num = random.randint(0, len(list_card) - 1)
#         if summ_user + summ_comp > 21 and list_card[num][0] == 'Туз':
#             summ_user -= 10
#         summ_user += list_card[num][2]
#         print('Выпала карта:', list_card[num][0], list_card[num][1])
#         del list_card[num]
#         print('Ваша сумма карт:', summ_user)
#         if summ_user > 21:
#             print('Компьютер выйграл!')
#             break
#
#         num = random.randint(0, len(list_card) - 1)
#         summ_comp += list_card[num][2]
#         del list_card[num]
#     if user_answer == 2:
#         if summ_user > summ_comp or summ_comp > 21:
#             print('Игрок выйграл!')
#         elif summ_user == summ_comp:
#             print('Ничья!')
#         else:
#             print('Компьютер выйграл!')
#         break





