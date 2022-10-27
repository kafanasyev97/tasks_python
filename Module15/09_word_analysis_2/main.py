user = input('Введите слово: ')
start_list = list(user)
finish_list = []
count = 1

for i in range(len(start_list)):
    finish_list.append(start_list[len(start_list) - count])
    count += 1

if start_list == finish_list:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
