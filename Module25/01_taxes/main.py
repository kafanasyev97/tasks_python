class Property:
    """
    Базовый класс, показывает стоимость имущества

    Args:
        worth(int): передается стоимость имущества
    """
    def __init__(self, worth):
        self.worth = worth

    def tax(self, user_money):
        """
        Метод подсчета налога
        :param user_money: количество денег пользователя(int)
        :return: налог(int)
        """
        return self.worth / user_money


class Apartment(Property):
    """
    Класс Квартира. Родитель: Property
    """
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self, user_money):
        """
        Метод подсчета налога
        :param user_money: количество денег пользователя(int)
        if: денег не хватает
        else: выводим налог
        """
        if self.worth / 500 + self.worth > user_money:
            print('Не хватает', self.worth / 500 + self.worth - user_money)
        else:
            print('Налог:', self.worth / 500)


class Car(Property):
    """
    Класс Машина. Родитель: Property
    """
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self, user_money):
        """
        Метод подсчета налога
        :param user_money: количество денег пользователя(int)
        if: денег не хватает
        else: выводим налог
        """
        if self.worth / 500 + self.worth > user_money:
            print('Не хватает', self.worth / 500 + self.worth - user_money)
        else:
            print('Налог:', self.worth / 500)


class CountryHouse(Property):
    """
    Класс Дача. Родитель: Property
    """
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self, user_money):
        """
        Метод подсчета налога
        :param user_money: количество денег пользователя(int)
        if: денег не хватает
        else: выводим налог
        """
        if self.worth / 500 + self.worth > user_money:
            print('Не хватает', self.worth / 500 + self.worth - user_money)
        else:
            print('Налог:', self.worth / 500)


user_money = int(input('Введите количество денег: '))
price = int(input('Введите стоимость имущества: '))

user_1 = CountryHouse(price)
user_1.tax(user_money)

