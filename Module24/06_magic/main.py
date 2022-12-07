class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Brick):
            return Sand()
        else:
            return None


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Shtorm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Shtorm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Brick):
            return Clay()
        else:
            return None


class Earth:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Air):
            return Dust()
        else:
            return None


class Shtorm:
    def __str__(self):
        return 'Шторм'


class Steam:
    def __str__(self):
        return 'Пар'


class Dirt:
    def __str__(self):
        return 'Грязь'


class Lightning:
    def __str__(self):
        return 'Молния'


class Dust:
    def __str__(self):
        return 'Пыль'


class Lava:
    def __str__(self):
        return 'Лава'


class Brick:
    def __str__(self):
        return 'Кирпич'


class Sand:
    def __str__(self):
        return 'Песок'


class Clay:
    def __str__(self):
        return 'Глина'


f = Fire()
s = Air()
a = f + s
print(a)
