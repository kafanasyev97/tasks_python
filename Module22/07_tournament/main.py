first_file = open('first_tour.txt', 'r', encoding='utf-8')
k = int(first_file.readline())
new_list = []
for line in first_file:
    new_line = line.split()
    if int(new_line[2]) > k:
        new_list.append(new_line)
first_file.close()
new_list.sort(key=lambda student: student[2])
new_list.reverse()

count = str(len(new_list))
out_lst = []
num = 1
for i in new_list:
    name_sim = str(i[1][0]) + '.'
    s_win = [str(num) + ')',  name_sim, str(i[0]), str(i[2])]
    out_lst.append(s_win)
    num += 1

result = ''
for i_elem in out_lst:
    result += ' '.join(i_elem) + '\n'

finish_file = open('second_tour.txt', 'a')
finish_file.write(count + '\n')
finish_file.write(result)
finish_file.close()

one_file = open('first_tour.txt', 'r', encoding='utf-8')
elem = one_file.read()
print('Содержимое файла first_tour.txt:')
print(elem)
one_file.close()

two_file = open('second_tour.txt', 'r', encoding='utf-8')
two_elem = two_file.read()
print('\nСодержимое файла second_tour.txt:')
print(two_elem)
two_file.close()
