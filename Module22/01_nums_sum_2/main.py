speakers_file = open('numbers.txt', 'r')
start = speakers_file.read()
print('Содержимое файла numbers.txt\n', start)
speakers_file.close()

speakers_file = open('numbers.txt', 'r')
ssd = []
for i_line in speakers_file:
    if i_line != '\n':
        ssd.append(int(i_line))
summ = str(sum(ssd))
speakers_file.close()

speakers_file_2 = open('answer.txt', 'w')
speakers_file_2.write(summ)
speakers_file_2.close()

speakers_file_3 = open('answer.txt', 'r')
result = speakers_file_3.read()
print('Содержимое файла answer.txt\n', result)
speakers_file_3.close()
