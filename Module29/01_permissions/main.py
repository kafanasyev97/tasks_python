def check_permission(text):
    def need_func(func):
        def wrapped_func(*args, **kwargs):
            try:
                if text in user_permissions:
                    func(*args, **kwargs)
                else:
                    raise PermissionError(f'У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
            except PermissionError as exc:
                print(exc)
        return wrapped_func
    return need_func


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
