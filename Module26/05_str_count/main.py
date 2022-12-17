import os
from collections.abc import Iterable


def strings_count(directory: str) -> Iterable[tuple]:
    for address, dirs, files in os.walk(directory):
        for file in files:
            count = 0
            if os.path.join(address, file).endswith('.py'):
                curr_file = open(os.path.join(address, file), 'r', encoding='utf-8')
                for line in curr_file.readlines():
                    if line != '\n' and not line.startswith('#'):
                        count += 1
                yield os.path.join(address, file), count


total_str = 0
for element in strings_count(directory='..'):
    print('Файл "{}": строк кода - {}'.format(element[0], element[1]))
    total_str += element[1]
print('Общее кол-во строк кода:', total_str)

