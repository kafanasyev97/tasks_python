class Stack:
    """
    Класс Stack, в нем содержится структура данных стек
    __st: список
    """
    def __init__(self):
        self.__st = []

    def __str__(self):
        return '; '.join(self.__st)

    def push(self, elem):
        """
        добавляем элемент в список
        """
        self.__st.append(elem)

    def pop(self):
        """
        удаляем последнее значение из списка
        """
        if len(self.__st) == 0:
            return None
        return self.__st.pop()


class TaskManager:
    """
    класс TaskManager
    task: словарь
    """
    def __init__(self):
        self.task = {}

    def __str__(self):
        """
        выводим результат на экран
        """
        display = []
        if self.task:
            for i_priority in sorted(self.task.keys()):
                display.append(f'{str(i_priority)} {self.task[i_priority]}\n')

        return ''.join(display)

    def new_task(self, goal, priority):
        """
        добавляем ключ и значение(стек) в словарь
        :param goal: строка, которая будет добавлена в стек
        :param priority: ключ
        """
        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].push(goal)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
