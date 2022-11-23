import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def need_func(struct, key, meaning):
    if key in struct:
        struct[key] = meaning
        return struct

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = need_func(sub_struct, key, meaning)
            if result:
                return struct



count_sites = int(input('Сколько сайтов: '))
goods = {}
for x in range(count_sites):
    user = input('Введите название продукта для нового сайта: ')
    key = {'title': f'Куплю/продам {user} недорого', 'h2': f'У нас самая низкая цена на {user}'}
    site_copy = copy.deepcopy(site)
    for i in key:
        need_func(site_copy, i, key[i])
    name_of_product = f'Сайт для {user}'
    goods[name_of_product] = site_copy
    for index, value in goods.items():
        print(index)
        print(value)

