class Cell:
    def __init__(self, num):
        self.num = num
        self.place = True

    def place_true_false(self, value):
        Board.ssd[self.num - 1].num = value
        self.num = value
        self.place = False


class Board:
    ssd = [Cell(num) for num in range(1, 10)]

    def draw_board(self):
        print("-" * 13)
        for i in range(3):
            print("|", Board.ssd[0 + i * 3].num, "|", Board.ssd[1 + i * 3].num, "|", Board.ssd[2 + i * 3].num, "|")
            print("-" * 13)

    def check_win(self):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if Board.ssd[each[0]].num == Board.ssd[each[1]].num == Board.ssd[each[2]].num:
                return Board.ssd[each[0]].num
        return False


class Player:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def take_input(self):
        while True:
            player_answer = input("Куда поставим " + self.value + "? ")
            try:
                player_answer = int(player_answer)
            except:
                print("Некорректный ввод. Вы уверены, что ввели число?")
                continue
            if player_answer >= 1 and player_answer <= 9:
                if Board.ssd[player_answer - 1].place:
                    Board.ssd[player_answer - 1].place_true_false(self.value)
                    break
                else:
                    print('Клетка занята!')
            else:
                print("Некорректный ввод. Введите число от 1 до 9.")


player_1 = Player('Вася', 'X')
player_2 = Player('Петя', '0')
field = Board()


counter = 0
win = False
while not win:
    field.draw_board()
    if counter % 2 == 0:
        player_1.take_input()
    else:
        player_2.take_input()
    counter += 1
    if counter > 4:
        tmp = field.check_win()
        if tmp:
            print(tmp, "выиграл!")
            win = True
            break
    if counter == 9:
        print("Ничья!")
        break
field.draw_board()
