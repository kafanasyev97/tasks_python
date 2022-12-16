class Number: #Итератор
    def __init__(self, number):
        self.number = number
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter <= self.number:
            return self.counter ** 2
        else:
            raise StopIteration


user = int(input('Введите число: '))
gen = Number(user)
for x in gen:
    print(x, end=' ')
#----------------------------------------------------------------

def square(num):  # Генератор
    for x in range(1, num + 1):
        yield x ** 2


user = int(input('Введите число: '))
for x in square(user):
    print(x, end=' ')
#----------------------------------------------------


user = int(input('Введите число: ')) #Генераторное выражение
gen = (num ** 2 for num in range(1, user + 1))
for x in gen:
    print(x, end=' ')
