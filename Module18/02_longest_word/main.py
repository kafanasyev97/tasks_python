text = input('Введите строку:').split()
count = 0
maxx_str = ''

for i in text:
    if len(i) > count:
        count = len(i)
        maxx_str = i

print('Самое длинное слово:', maxx_str)
print('Длина этого слова:', count)