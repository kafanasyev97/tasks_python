class Gardener:
    def __init__(self, name, count):
        self.name = name
        self.gard = PotatoGarden(count)
        self.count = count

    def tend(self):
        while True:
            answer = input('Собрать картошку(1 - да; 2- нет)? ')
            if answer == '1':
                if self.gard.are_all_ripe():
                    print('Собрал урожай из', self.count, 'картошек!')
                    break
                else:
                    print('Картошка не дозрела!')
            two_answer = input('\nУхаживать за картошкой(1 - да; 2- нет)? ')
            if two_answer == '1':
                for x in self.gard.potatoes:
                    x.grow()


class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {},'.format(
            self.index, self.states[self.state]
        ))



class PotatoGarden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        for i_potato in self.potatoes:
            if not i_potato.is_ripe():
                return False
        else:
            return True


user_1 = Gardener('Вася', 5)
user_1.tend()

