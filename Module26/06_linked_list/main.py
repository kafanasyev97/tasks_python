class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f'Node {self.value}'


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return f'{values}'
        return 'LinkedList  []'

    def append(self, elem):
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
            self.length += 1
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.length += 1

    def remove(self, index):
        cur_node = self.head
        cur_index = 0
        if self.length == 0 or self.length <= index:
            raise IndexError

        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.length -= 1
                return

        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1

        prev.next = cur_node.next
        self.length -= 1

    def index_check(self, index):
        if not 0 <= index < self.length:
            raise IndexError

    def get(self, index):
        self.index_check(index)
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value



my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(my_list)
# print()
# my_list.remove(2)
# print(my_list)
print(my_list.get(2))
