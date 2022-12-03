count = 0
string = 1
error = ''
with open('people.txt', 'r', encoding='utf-8') as file:
    for x in file:
        try:
            if len(x.strip()) < 3:
                raise Exception(f'Ошибка: менее трёх символов в строке {string}.')
        except Exception as esc:
            print(esc)
            error += str(esc) + '\n'
        count += len(x.strip())
        string += 1
print('Общее количество символов:', count)
with open('errors.log', 'w', encoding='utf-8') as finish_file:
    finish_file.write(error)
