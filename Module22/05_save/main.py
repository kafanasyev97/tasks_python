import os


def find_file(res, string):
    help_file = open(res, 'w')
    help_file.write(string)
    help_file.close()

    total = open(res, 'r')
    total_text = total.read()
    total.close()
    print('Содержимое файла:\n', total_text)


text = input('Введите строку: ')
user = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ').split()
file_name = input('Введите имя файла: ')
dir_path = os.path.abspath(os.path.sep)
path_text = os.path.join(dir_path, os.path.sep.join(user))

result = os.path.join(path_text, file_name)
if os.path.exists(path_text):
    for i_elem in os.listdir(path_text):
        if i_elem == file_name:
            answer = input('Вы действительно хотите перезаписать файл? ').lower()
            if answer == 'да':
                print('Файл успешно перезаписан!')
                find_file(result, text)
                break
            else:
                print('Нет так нет.')
                break
    else:
        print('Файл успешно сохранён!')
        find_file(result, text)
else:
    print('Такого пути нет на диске.')
