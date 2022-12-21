def debug(func):
    def wrapped_func(*args, **kwargs):
        print('Вызывается', func.__name__, repr(args), repr(kwargs))
        print(func.__name__, 'вернула значение', repr(func(*args, **kwargs)))
        print(func(*args, **kwargs))
        print()
    return wrapped_func


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)