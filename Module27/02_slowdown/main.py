import time
import functools
from typing import Callable, Any


def decor(func: Callable) -> Callable:
    """Декоратор, замедляющий работу функции"""
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print('</----------\>')
        time.sleep(3)
        func(*args, **kwargs)
        print('<\______/>')
    return wrapped_func


@decor
def help_func() -> None:
    print('помидоры')
    print('--ветчина--')
    print('~салат~')


help_func()
