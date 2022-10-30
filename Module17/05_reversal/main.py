text = input('Введите: ')
first = text.index('h')
last = text.rindex('h')
last -= 1
print('Развёрнутая последовательность между первым и последним h:', text[last:first:-1])