total_num = int(input('Введите количество чисел: '))
n = 0
num_list = []
for _ in range(total_num):
    user = int(input('Введите число: '))
    num_list.append(user)

for b in range(total_num - 1):
    n = 0
    for i in range(total_num - 1):
        if num_list[n] > num_list[n + 1]:
            num_list[n], num_list[n + 1] = num_list[n + 1], num_list[n]
        n += 1

print(num_list)