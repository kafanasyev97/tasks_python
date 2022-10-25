first_year = int(input('Введите первый год: '))
second_year = int(input('Введите первый год: '))
for total_year in range(first_year, second_year + 1):
    count = 0
    for number in str(total_year):
      result = str(total_year % 10)
      if number == result:
          count += 1
          if count == 3:
              print(total_year)
