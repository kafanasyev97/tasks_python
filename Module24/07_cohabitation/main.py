import random


class Person:
    food = 50
    money = 0

    def __init__(self, name):
        self.name = name
        self.satiety = 50

    def eat(self):
        self.satiety += 1
        Person.food -= 1
        return f'Ест, сытость {self.satiety}, еда {Person.food}'

    def work(self):
        self.satiety -= 1
        Person.money += 1
        return f'Работает, сытость {self.satiety}, деньги {Person.money}'

    def play(self):
        self.satiety -= 1
        return f'Играет, сытость {self.satiety}'

    def repast(self):
        Person.food += 1
        Person.money -= 1
        return f'Идет в магазин, еда {Person.food}, деньги {Person.money}'

def action(person):
    number_cubes = random.randint(1, 6)
    if person.satiety < 0:
        print(f'К сожалению, {person.name} помер с голоду ')
        return True
    if person.satiety < 20:
        text = person.eat()
    elif Person.food < 10:
        text = person.repast()
    elif Person.money < 50:
        text = person.work()
    elif number_cubes == 1:
        text = person.work()
    elif number_cubes == 2:
        text = person.eat()
    else:
        text = person.play()
    print(person.name, text)
    return False



person_1 = Person('Вася')
person_2 = Person('Федя')

for i in range(365):
    if action(person_1) or action(person_2):
        print('Все плохо')
        break
else:
    print('Выжили')
