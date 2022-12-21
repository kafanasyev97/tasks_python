from typing import Callable
import functools


def counter(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        wrapped_func.count += 1
        res = func(*args, **kwargs)
        print(f'Функция {func.__name__} была вызвана {wrapped_func.count} раз')
        return res
    wrapped_func.count = 0
    return wrapped_func


@counter
def test():
    print('test')


test()
test()
