while True:
    password = list(input('Придумайте пароль: '))
    length = len(password)
    capital_letters = len(list(filter(lambda x: x.isupper(), password)))
    numbers = len(list(filter(lambda x: x.isdigit(), password)))

    if (length >= 8) and (capital_letters >= 1) and (numbers >= 3):
        print('Это надежный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')

