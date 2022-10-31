def compression(text):
    counter = 1
    compressed = []

    for symbol in range(len(text)):
        if text[symbol] == text[symbol + 1: symbol + 2]:
            counter += 1
            continue
        compressed.append(text[symbol] + str(counter))
        counter = 1
    return compressed

plain_text = input('Введите строку: ')
print('Закодированная строка: {}'.format(''.join(compression(plain_text))))
