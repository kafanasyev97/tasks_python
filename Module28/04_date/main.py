class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return f'День: {self.day}\tМесяц: {self.month}\tГод: {self.year}'

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        dmy_list = date.split('-')
        day, month, year = int(dmy_list[0]), int(dmy_list[1]), int(dmy_list[2])
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999

    @classmethod
    def from_string(cls, date: str) -> 'Date':
        dmy_list = date.split('-')
        day, month, year = int(dmy_list[0]), int(dmy_list[1]), int(dmy_list[2])
        date_obj = cls(day, month, year)
        return date_obj


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
