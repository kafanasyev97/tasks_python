class Student:
    def __init__(self, name, number_group, progress):
        self.name = name
        self.number_group = number_group
        self.progress = progress
        self.average = sum(progress) / len(progress)

    def sort_by_list(self):
        return self.average


ssd = []
for x in range(2):
    name_user = input('Введите инициалы пользователя: ')
    number_group_user = int(input('Введите номер группы: '))
    grade_user = list(map(int, input('Введите оценки(через пробел): ').split()))
    ssd.append(Student(name_user, number_group_user, grade_user))

ssd.sort(key=Student.sort_by_list)

for x in ssd:
    print(x.name, x.number_group, '  ', *x.progress)

