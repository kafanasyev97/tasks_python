class Parent:
    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = children

    def info_parent(self):
        print()
        print(self.name, self.age)
        print('Дети:')
        for x in self.children:
            print(x.name, x.age)

    def child_calmness(self):
        choice = int(input('\nВведите номер ребенка, которого хотите успокоить: '))
        if self.children[choice - 1].calmness:
            print('Ребенок уже спокоен.')
        else:
            self.children[choice - 1].calmness = True
            print('Ребенок по имени', self.children[choice - 1].name, 'успокоен!')

    def child_hunger(self):
        choice = int(input('\nВведите номер ребенка, которого хотите покормить: '))
        if self.children[choice - 1].hunger:
            print('Ребенок уже сыт.')
        else:
            self.children[choice - 1].hunger = True
            print('Ребенок по имени', self.children[choice - 1].name, 'накормлен!')


class Child:
    calmness = False
    hunger = False

    def __init__(self, name, age):
        self.name = name
        self.age = age


ssd = []
parent_name = input('Введите имя родителя: ')
parent_age = int(input('Введите возраст родителя: '))
count_child = int(input('Введите кол-во детей: '))
for _ in range(count_child):
    child_name = input('Введите имя ребенка: ')
    child_age = int(input('Введите возраст ребенка: '))
    if parent_age - child_age < 16:
        raise Exception
    ssd.append(Child(child_name, child_age))

user_1 = Parent(parent_name, parent_age, ssd)
user_1.info_parent()
user_1.child_calmness()
user_1.child_hunger()
user_1.child_calmness()
