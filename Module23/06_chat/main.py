user = input('Введите ваше имя: ')
while True:
    print('Введите 1, если хотите увидеть текущий текст чата. Введите 2 если хотите написать сообщение. ')
    choice = int(input('Введите 1 или 2: '))
    if choice == 1:
        try:
            with open('our_chat.txt', 'r', encoding='utf-8') as file:
                messages = file.readlines()
                print(''.join(messages), '\n')
        except Exception:
            print('Чат пустой\n')
    elif choice == 2:
        new_message = input('Введите сообщение: ')
        with open('our_chat.txt', 'a', encoding='utf-8') as new_file:
            new_file.write(f'{user}: {new_message}\n')
    else:
        print('Такого варианта нет\n')

