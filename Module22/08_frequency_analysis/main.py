file = open('text.txt', 'r', encoding='utf-8')
text = file.read()
print('Содержимое файла text.txt:')
print(text)
file.close()

need_text = ''
need_dict = dict()
for alpha in text:
    if alpha.isalpha():
        need_text += alpha

need_text = need_text.lower()
for i_elem in need_text:
    need_dict[i_elem] = round(1 / (len(need_text) / need_text.count(i_elem)), 3)

two_dict = {}
for x in sorted(need_dict.keys()):
    two_dict[x] = str(need_dict[x])

ssd = []
for a, b in two_dict.items():
    ssd.append([a, b])
ssd.reverse()

ssd.sort(key=lambda num: num[1])
ssd.reverse()

result = ''
for i_elem in ssd:
    result += ' '.join(i_elem) + '\n'

finish_file = open('analysis.txt', 'w')
finish_file.write(result)
print('\nСодержимое файла analysis.txt:')
print(result)
finish_file.close()
