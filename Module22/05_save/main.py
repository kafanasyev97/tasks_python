import os




text = input('Введите строку: ')
user = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ').split()
file_name = input('Введите имя файла: ')
dir_path = os.path.abspath(os.path.sep)
print(dir_path)
path_text = os.path.join(dir_path, os.path.sep.join(user))
print(path_text)

result = os.path.join(path_text, file_name)
if os.path.exists(path_text):
    for i_elem in os.listdir(path_text):
        if i_elem == file_name:
            answer = input('Вы действительно хотите перезаписать файл? ').lower()
            if answer == 'да':
                help_file = open(result, 'w')
                help_file.write(text)
                print('Файл успешно сохранён!')
                help_file.close()
                total = open(result, 'r')
                total_text = total.read()
                total.close()
                print('Содержимое файла:\n', total_text)
            else:
                print('Нет так нет.')

else:
    print('Такого пути нет на диске.')
