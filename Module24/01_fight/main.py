import random


class Warrior:
    health = 100   #через __init__ не стал делать потому, что здоровье у обоих одинаковое


warrior_1 = Warrior()
warrior_2 = Warrior()
while True:
    answer = random.randint(1, 2)
    if answer == 1:
        warrior_2.health -= 20
        print('Атаковал 1 воин')
        print('Здоровье 2 воина:', warrior_2.health, '\n')
    elif answer == 2:
        warrior_1.health -= 20
        print('Атаковал 2 воин')
        print('Здоровье 1 воина:', warrior_1.health, '\n')

    if warrior_1.health == 0:
        print('Победу одержал 2 воин!')
        break
    elif warrior_2.health == 0:
        print('Победу одержал 1 воин!')
        break
