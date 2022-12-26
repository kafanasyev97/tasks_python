class File:
    """Контекст - менеджер для открытия и закрытия файлов"""
    def __init__(self, name: str, mode: str) -> None:
        self.name = name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.name, self.mode, encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        return True


with File('example.txt', 'w+') as file:
    file.write('Всем привет!')
