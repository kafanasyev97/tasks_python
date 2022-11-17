students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict):
    lst = []
    for i in dict.values():
        lst.extend(i['interests'])
    # lst = [', '.join(x['interests']) for x in dict.values()] хотел сделать код выше через comprehensions,
    # но получается немного неправильно. Буду рад если подскажите как можно его упростить(если можно конечно).
    cnt = [len(x['surname']) for x in dict.values()]
    cnt = sum(cnt)
    return lst, cnt


pairs = [(index, value['age']) for index, value in students.items()]
print('Список пар "ID студента — возраст":', pairs)



my_lst, lenn = f(students)
print('Полный список интересов всех студентов:', my_lst)
print('Общая длина всех фамилий студентов:', lenn)

