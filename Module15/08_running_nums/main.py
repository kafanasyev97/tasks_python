n = int(input('Введите количество чисел: '))
first_list = []
second_list = []

for i in range(n):
    user = int(input('Введите число: '))
    first_list.append(user)

k = int(input('Сдвиг: '))
count = k
while count != 0:
    second_list.append(first_list[len(first_list) - count])
    count -= 1

numbers = n - k  #оставшееся кол-во цифр
for i in range(numbers):
    second_list.append(first_list[count])
    count += 1

print('Изначальный список:', first_list)
print('Сдвинутый список:', second_list)