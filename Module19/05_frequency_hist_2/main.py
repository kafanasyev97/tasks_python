def histogram(text):
    sym_dict = dict()
    for sym in text:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict

def need_func(sym_dict):
    text_dict = dict()
    for i_letter, i_num in sym_dict.items():
        text_dict.setdefault(i_num, []).append((i_letter))
    return text_dict

text = input('Введите текст: ')
print('Оригинальный словарь частот: ')

sym_dict = histogram(text)

for i_sym in sorted(sym_dict.keys()):
    print(i_sym, ':', sym_dict[i_sym])

print('\nИнвертированный словарь частот: ')

text_dict = need_func(sym_dict)

for i in text_dict:
    print(i, ':', text_dict[i])
