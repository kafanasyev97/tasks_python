def calculating_math_func(data, i_dict):
    if data in i_dict:
        return i_dict[data]
    else:
        result = max(i_dict.values())
        for index in range(max(i_dict.keys()) + 1, data + 1):
            result *= index
            i_dict[index] = result
        return result
    result /= data ** 3
    result = result ** 10
    return result

slov = {1: 1}
while True:
    user = int(input('Введите число: '))
    print(calculating_math_func(user, slov))

