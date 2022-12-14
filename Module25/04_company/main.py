import random


class Person:
    """
    Базовый класс, описывающий человека

    Args:
        __name(str): имя человека
        __surname(str): фамилия человека
        __age(int): возраст человека
    """
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age


class Employee(Person):
    """
    Класс Работник. Родитель Person
    """
    def account_salary(self):
        pass


class Manager(Employee):
    """
    Класс Менеджер. Родитель Работник
    """
    def account_salary(self):
        """
        метод возвращает размер зарплаты
        :return: 13000(int)
        """
        return 13000


class Agent(Employee):
    """
    Класс Агент. Родитель Работник

    Attributes:
        volume_sale(int): объем продаж
    """
    volume_sale = 0

    def account_salary(self):
        return 5000 + (5 / 100 * self.volume_sale)


class Worker(Employee):
    """
    Класс Рабочий. Родитель Работник

    Attributes:
        hours(int): количество часов
    """
    hours = 0

    def account_salary(self):
        return 100 * self.hours


ssd = []
user_names = ['Алексей', 'Женя', 'Иван', 'Петр', 'Семен', 'Антон', 'Максим']
user_surnames = ['Алексеев', 'Сметанин', 'Иванов', 'Семенов', 'Петров', 'Антонов']


def humans():
    name = random.choice(user_names)
    surname = random.choice(user_surnames)
    age = random.randint(20, 60)
    return name, surname, age


for x in range(3):
    ssd.append(Manager(*humans()))

for x in range(3):
    agent = Agent(*humans())
    agent.volume_sale = random.randint(2000, 20000)
    ssd.append(agent)

for x in range(3):
    worker = Worker(*humans())
    worker.hours = random.randint(20, 50)
    ssd.append(worker)

summ = 0
for user in ssd:
    summ += user.account_salary()

print('Сумма зарплат всех служащих:', round(summ, 2))
