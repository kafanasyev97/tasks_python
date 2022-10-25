print('Введите координаты монетки:')
x = float(input('x: '))
y = float(input('y: '))
r = float(input('Введите радиус: '))
if x <= r and y <= r:
    print('Монетка где то рядом')
else:
    print('Монетки в области нет')