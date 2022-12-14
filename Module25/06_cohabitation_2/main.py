import random


class House:
    """
    Базовый класс, описывающий жизнь семьи и имущество в доме

    Args:
        family(list): список семьи

    Attributes:
        all - (int)
        money: деньги семьи
        food_human: еда людей
        food_for_cat: еда кота
        dirt: грязь в доме
        total_money: итого заработано денег за год
        total_eat: сколько было съедено еды
        total_fur_coat: шуб куплено за год
        total_eat_cat: съедено еды котом за год
    """
    money = 100
    food_human = 50
    food_for_cat = 30
    dirt = 0
    total_money = 0
    total_eat = 0
    total_fur_coat = 0
    total_eat_cat = 0

    def __init__(self, family):
        self.family = family

    def pollution(self):
        """
        Ежедневная грязь в любом случае
        """
        self.dirt += 5

    def life(self):
        """
        Процесс жизни семьи
        """
        for i_person in self.family:
            if House.dirt > 90 and not isinstance(i_person, Cat):
                i_person.happiness -= 10

            if isinstance(i_person, Cat) and House.food_for_cat >= 20 <= i_person.satiety:
                i_person.eating_cat()
                print('Кот поел')
                House.total_eat_cat += 10

            elif isinstance(i_person, Cat):
                if random.randint(1, 3) == 1:
                    i_person.wallpaper()
                    print('Кот подрал обои')
                else:
                    i_person.sleep()
                    print('Кот спит')

            elif House.food_human >= 60 and i_person.satiety <= 30:
                i_person.eating_human()
                print(i_person.name, 'поел')
                House.total_eat += 30

            elif isinstance(i_person, Husband):
                if House.money <= 150:
                    i_person.work()
                    House.total_money += 150
                elif i_person.happiness <= 50:
                    i_person.play()
                elif i_person.happiness <= 70:
                    i_person.petting_a_cat()
                else:
                    i_person.work()
                    House.total_money += 150

            elif isinstance(i_person, Wife):
                if House.food_human <= 60 and House.money > 100:
                    i_person.buy_food()
                elif House.food_for_cat <= 20:
                    i_person.buy_food_cat()
                elif House.dirt >= 50:
                    i_person.cleaning()
                elif i_person.happiness <= 70:
                    i_person.petting_a_cat()
                elif House.money > 450:
                    i_person.purchase()
                    House.total_fur_coat += 1
                else:
                    i_person.petting_a_cat()


class Human:
    """
    Базовый класс, описывающий человека
    Args:
        name(str): имя человека

    Attributes:
        satiety(int): сытность
        happiness(int): счастье
    """
    def __init__(self, name):
        self.name = name
        self.satiety = 30
        self.happiness = 100

    def eating_human(self):
        """
        процесс еды
        """
        self.satiety += 30
        House.food_human -= 30


class Husband(Human):
    """
    Класс Муж. Родитель: Human
    Args:
        name(str): имя мужа
    """
    def __init__(self, name):
        super().__init__(name)

    def work(self):
        """
        работа мужа
        """
        House.money += 150
        self.satiety -= 10
        print('Муж работает. Деньги:', House.money)

    def play(self):
        """
        Муж играет

        """
        self.happiness += 20
        self.satiety -= 10
        print('Муж играет')

    def petting_a_cat(self):
        """
        муж кормит кота
        """
        self.happiness += 5
        self.satiety -= 10
        print('Муж погладил кота.')


class Wife(Human):
    """
        Класс Жена. Родитель: Human
        Args:
            name(str): имя жены
        """
    def __init__(self, name):
        super().__init__(name)

    def buy_food(self):
        """
        Покупка еды

        """
        House.food_human += 100
        House.money -= 100
        self.satiety -= 10
        print('Жена купила еду. Еда:', House.food_human, ', деньги:', House.money)

    def buy_food_cat(self):
        """
        Покупка еды коту

        """
        House.food_for_cat += 50
        House.money -= 50
        print('Жена купила еду коту. Еда кота:', House.food_for_cat, ', деньги:', House.money)

    def purchase(self):
        """
        Покупка шубы

        """
        House.money -= 350
        self.happiness += 60
        self.satiety -= 10
        print('Жена купила шубу. Деньги:', House.money)

    def petting_a_cat(self):
        """
        Жена гладит кота

        """
        self.happiness += 5
        self.satiety -= 10
        print('Жена погладила кота.')

    def cleaning(self):
        """
        Жена убирается

        """
        House.dirt -= 100
        self.satiety -= 10
        print('Жена убралась. Грязь:', House.dirt)


class Cat:
    """
    Класс Кот

    Args:
        name_cat(str): имя кота
    """
    def __init__(self, name_cat):
        self.name_cat = name_cat
        self.satiety = 30

    def eating_cat(self):
        """
        Кот ест

        """
        self.satiety += 20
        House.food_for_cat -= 10

    def wallpaper(self):
        """
        Кот дерет обои

        """
        House.dirt += 5
        self.satiety -= 10

    def sleep(self):
        """
        Кот спит

        """
        self.satiety -= 10


def life_dead(family):
    for i_elem in family:
        if i_elem.satiety <= 0:
            print('Один из жильцов умер от голода')
            return True
        elif i_elem.happiness == 0 and not isinstance(i_elem, Cat):
            print('Один из жильцов умер от депрессии')
            return True
        else:
            return False


husband = Husband('Виталя')
wife = Wife('Юлия')
cat = Cat('Васька')
family_list = [husband, wife, cat]
house = House(family_list)

for day in range(365):
    print(f'День:', day + 1)
    house.pollution()
    if life_dead(family_list):
        print('Все плохо')
    elif day == 364:
        print('\nВсе живы')
        break
    else:
        house.life()

print('\nКуплено шуб:', House.total_fur_coat)
print('Заработано:', House.total_money)
print('Съедено:', House.total_eat)
print('Съедено котом:', House.total_eat_cat)

