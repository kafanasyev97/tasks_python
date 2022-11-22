def fibonacci(n):
    cur = 1
    if n > 2:
        cur = fibonacci(n-1) + fibonacci(n-2)
    return cur

element = int(input('Введите позицию числа в ряде Фибоначчи: '))
value = fibonacci(element)
print('Число:', value)