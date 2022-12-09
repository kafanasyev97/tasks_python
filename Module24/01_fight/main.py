import random


class Warrior:
    def __init__(self, health):
        self.health = health

    def hit(self):
        self.health -= 20

    def live(self):
        if self.health > 0:
            print('Жив!\n')
        else:
            print('Погиб!\n')


warrior_1 = Warrior(100)
warrior_2 = Warrior(100)
while True:
    answer = random.randint(1, 2)
    if answer == 1:
        warrior_2.hit()
        print('Атаковал 1 воин')
        print('Здоровье 2 воина:', warrior_2.health)
        warrior_2.live()
    elif answer == 2:
        warrior_1.hit()
        print('Атаковал 2 воин')
        print('Здоровье 1 воина:', warrior_1.health)
        warrior_1.live()

    if warrior_1.health == 0:
        print('Победу одержал 2 воин!')
        break
    elif warrior_2.health == 0:
        print('Победу одержал 1 воин!')
        break



# import random
#
#
# class Warrior:
#     def __init__(self, name, health):
#         self.health = health
#         self.name = name
#
#     def hit(self):
#         self.health -= 20
#
#     def live(self):
#         if self.health > 0:
#             print('Жив!\n')
#         else:
#             print('Погиб воин', self.name)
#
#     def true_false(self):
#         if self.health > 0:
#             return True
#         else:
#             return False
#
#
# warrior_1 = Warrior('Вася', 100)
# warrior_2 = Warrior('Петя', 100)
# while True:
#     answer = random.randint(1, 2)
#     if answer == 1:
#         warrior_2.hit()
#         print('Атаковал 1 воин')
#         print('Здоровье 2 воина:', warrior_2.health)
#         warrior_2.live()
#     elif answer == 2:
#         warrior_1.hit()
#         print('Атаковал 2 воин')
#         print('Здоровье 1 воина:', warrior_1.health)
#         warrior_1.live()
#
#     if not warrior_1.true_false() or not warrior_2.true_false():
#         break
