import os

def find_file(cur_path, count_file):
    count_dir = 0
    summ = 0
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if os.path.isfile(path):
            count_file.append(1)
            summ += os.path.getsize(path)
        elif os.path.isdir(path):
            result = find_file(path, count_file)
            count_dir += 1
            summ += result[2]
    return count_dir, len(count_file), summ


count_file = []
file_path = find_file(os.path.abspath('C:\\Users\\user\\PycharmProjects\\dpo_python_basic\\Module14'), count_file)
print('Количество подкаталогов:', file_path[0])
print('Количество файлов:', file_path[1])
print('Размер каталога (в Кб):', file_path[2] / 1024)

