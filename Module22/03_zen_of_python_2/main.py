import os

first_file = open(os.path.abspath('C:\\Users\\user\\PycharmProjects\\dpo_python_basic\\Module22\\02_zen_of_python\\zen.txt'), 'r')
count_str = 0
ssd = [i_line for i_line in first_file]
print('Количество строк в файле:', len(ssd))
first_file.close()

count_letter = [x.lower() for i_elem in ssd for x in i_elem if x.isalpha()]
print('Количество букв в файле:', len(count_letter))

minimum = count_letter[0]
for i_index in range(len(count_letter) - 1):
    if count_letter.count(count_letter[i_index]) < count_letter.count(minimum):
        minimum = count_letter[i_index]
print('Наиболее редкая буква:', minimum)

second_file = open(os.path.abspath('C:\\Users\\user\\PycharmProjects\\dpo_python_basic\\Module22\\02_zen_of_python\\zen.txt'), 'r')
letters = second_file.read()
letters = letters.split()
for x in letters:
    if x == '--':
        letters.remove(x)
print('Количество слов в файле:', len(letters))
second_file.close()

