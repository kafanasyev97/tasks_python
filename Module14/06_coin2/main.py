print('Введите координаты монетки:')
x = float(input('x: '))
y = float(input('y: '))
r = float(input('Введите радиус: '))
if (x ** 2 + y ** 2) ** 0.5 <= r:
    print('Монетка где то рядом')
else:
    print('Монетки в области нет')