user = input('Введите текст: ')
need_list = [x for x in user if x == 'а' or x == 'у' or x == 'о' or x == 'е'
             or x == 'э' or x == 'ы' or x == 'я' or x == 'и' or x == 'ю']
print('Список гласных букв:', need_list)
print('Длина списка:', len(need_list))
# Не стал добавлять еще заглавные буквы, т.к. список получился бы очень большой))


# Можно использовать такой код, чтобы было короче, но мы его еще не прошли

#letters = "аоиеёэыуюя"

#text = input("Введите текст: ")
#a = [c for c in text if c in letters]
#print("Список гласных букв:", a)
#print("Длина списка:", len(a))