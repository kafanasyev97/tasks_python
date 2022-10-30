alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
string = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
first_list = [alphabet[(alphabet.index(sym) + shift) % 33] if sym != ' ' else ' ' for sym in string]
new_str = ''
for i in first_list:
    new_str += i

print('Зашифрованное сообщение:', new_str)
