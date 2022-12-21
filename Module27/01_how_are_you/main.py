from typing import Callable
import functools


def how_are_you(func: Callable) -> Callable:
    """Декоратор. Спрашивает у пользователя как его дела."""
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> None:
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        func(*args, **kwargs)
    return wrapped_func


@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


test()
