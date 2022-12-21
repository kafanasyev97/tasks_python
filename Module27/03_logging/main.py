import datetime


def logging(func):
    def wrapped_func(*args, **kwargs):
        print(func.__name__)
        print(func.__doc__)
        try:
            res = func(*args, **kwargs)
            return res
        except Exception as exc:
            with open('function_errors.log', 'a', encoding='utf-8') as file:
                file.write(f'{datetime.datetime.now()},  {func.__name__},  {exc}\n')
            print('Обнаружена ошибка!')
    return wrapped_func


@logging
def help_func():
    """Вспомогательная функция"""
    result = 3 / 0
    return result


help_func()
