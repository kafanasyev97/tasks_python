import math


class Car:

    def __init__(self, x, y, corner):
        self.x = x
        self.y = y
        self.corner = corner

    def move(self, dist):
        self.x = self.x + dist * math.cos(self.corner)
        self.y = self.y + dist * math.sin(self.corner)


class Bus(Car):
    max_passengers = 60

    def __init__(self, x, y, corner):
        super().__init__(x, y, corner)
        self.now_passengers = 0
        self.money = 0

    def move(self, distance):
        self.money += self.now_passengers * distance
        super().move(distance)

    def enter(self, passengers):
        if passengers + self.now_passengers > Bus.max_passengers:
            print('Столько человек войти не сможет! Достигнута максимальная вместимость автобуса.')
        else:
            self.now_passengers += passengers
            print('Люди вошли. Сейчас в автобусе', self.now_passengers, 'пассажиров.')

    def exit(self, passengers):
        if passengers > self.now_passengers:
            print('В автобусе меньше народа! Значит вышли все.')
            self.now_passengers = 0
        else:
            self.now_passengers -= passengers
            print('Люди вышли. В автобусе осталось', self.now_passengers, 'человек.')
