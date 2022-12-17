import os.path


def gen_files_path(folder_search):
    for address, dirs, files in os.walk(os.path.abspath(os.path.sep)):
        if address.endswith(folder_search):
            print('Нужный каталог:', address)
            return
        for name in files:
            yield os.path.join(address, name)


user = input("Какой каталог будем искать? ")
for x in gen_files_path(user):
    print(x)

# folder_search = input("Какой каталог будем искать? ")
# for address, dirs, files in os.walk(os.path.abspath(os.path.sep)):
#     if folder_search in dirs:
#         print('Нужный каталог:', os.path.join(address, folder_search))
#         break
#     for name in files:
#         print(os.path.join(address, name))