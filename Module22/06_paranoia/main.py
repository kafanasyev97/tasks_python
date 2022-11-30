def find_file(one_fil, num):
    result = ''
    for i_elem in one_fil:
        for elem in i_elem:
            if elem != '\n' and elem != ' ':
                if elem.isupper():
                    result += alpha[(alpha.index(elem.lower()) + num) % len(alpha)].upper()
                else:
                    result += alpha[(alpha.index(elem) + num) % len(alpha)]
            elif elem == ' ':
                result += ' '
            else:
                result += '\n'
        num += 1
    return result


alpha = 'abcdefghijklmnopqrstuvwxyz'
start_file = open('text.txt', 'r', encoding='utf-8')
shift = 1

total = find_file(start_file, shift)
start_file.close()

finish_file = open('cipher_text.txt', 'w')
finish_file.write(total)
finish_file.close()

file = open('text.txt', 'r')
one_file = file.read()
print('Содержимое файла text.txt:')
print(one_file)
file.close()

print('\nСодержимое файла cipher_text.txt:')
print(total)



# alpha = 'abcdefghijklmnopqrstuvwxyz'
# start_file = open('text.txt', 'r', encoding='utf-8')
# shift = 1
# result = ''
# for i_elem in start_file:
#     for elem in i_elem:
#         if elem != '\n' and elem != ' ':
#             if elem.isupper():
#                 result += alpha[(alpha.index(elem.lower()) + shift) % len(alpha)].upper()
#             else:
#                 result += alpha[(alpha.index(elem) + shift) % len(alpha)]
#         elif elem == ' ':
#             result += ' '
#         else:
#             result += '\n'
#     shift += 1
# start_file.close()
#
# finish_file = open('cipher_text.txt', 'w')
# finish_file.write(result)
# finish_file.close()
#
# file = open('text.txt', 'r')
# one_file = file.read()
# print('Содержимое файла text.txt:')
# print(one_file)
# file.close()
#
# print('\nСодержимое файла cipher_text.txt:')
# print(result)
