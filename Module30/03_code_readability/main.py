def is_prime(number):
    if number == 0 or number == 1:
        return False
    for x in range(2, number):
        if number % x == 0:           #Читабельней первое решение
            return False
    return True


if __name__ == '__main__':
    result = [num for num in range(0, 1001) if is_prime(num)]
    print(result)

    print(list(filter(lambda x: all(map(lambda i: x % i != 0, range(2, int(x ** 0.5) + 1))), range(2, 1001))))
