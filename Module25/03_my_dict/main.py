class MyDict(dict):
    """
    Класс Мой Словарь. Родитель: Словарь
    """
    def get(self, key, value=0):
        if key in self:
            return self[key]
        else:
            return value




