good_file = open('registrations_good.log', 'a', encoding='utf-8')
bad_file = open('registrations_bad.log', 'a', encoding='utf-8')

with open('registrations.txt', 'r', encoding='utf-8') as start_file:
    for line in start_file:
        line = line.split()
        try:
            if len(line) < 3:
                raise IndexError('НЕ присутствуют все три поля')
            elif not line[0].isalpha():
                raise NameError('Поле имени содержит НЕ только буквы:')
            elif '@' not in line[1] and '.' not in line[1]:
                raise SyntaxError('Поле «Имейл» НЕ содержит @ и .(точку)')
            elif not 9 < int(line[2]) < 100:
                raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')
            else:
                good_file.write(' '.join(line) + '\n')

        except IndexError as esc:
            bad_file.write(str(' '.join(line)) + '     ' + str(esc) + '\n')
        except NameError as esc:
            bad_file.write(str(' '.join(line)) + '     ' + str(esc) + '\n')
        except SyntaxError as esc:
            bad_file.write(str(' '.join(line)) + '     ' + str(esc) + '\n')
        except ValueError as esc:
            bad_file.write(str(' '.join(line)) + '     ' + str(esc) + '\n')
