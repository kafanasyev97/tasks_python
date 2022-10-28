def need_func(num_list):
    reverse_list = []
    for i_num in range(len(num_list) - 1, -1, -1):
        reverse_list.append(num_list[i_num])
    if num_list == reverse_list:
        return True
    else:
        return False

count_nums = int(input('Кол-во чисел: '))
nums_list = []

for _ in range(count_nums):
    user = int(input('Число: '))
    nums_list.append(user)

new_nums = []
result = []

for i_nums in range(0, count_nums):
    for i_help in range(i_nums, count_nums):
        new_nums.append(nums_list[i_help])
    if need_func(new_nums):
        for i_result in range(0, i_nums):
            result.append(nums_list[i_result])
        result.reverse()
        break
    new_nums = []

print('Последовательность:', nums_list)
print('Нужно приписать чисел:', len(result))
print('Сами числа:', result)
