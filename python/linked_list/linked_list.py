class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        pass

    def insert(self, value):
        node =  Node(value, self.head)
        self.head = node

    def append(self, value):
        current = self.head
        while current:
            if current.next == None:
                node = Node(value)
                current.next = node
                return
            current = current.next


    def insert_before(self, value):
        node =  Node(value, self.head)
        self.head = node

    def insert_after(self, value, new_value):
        current = self.head
        while current:
            if current.value == value:
                current.next = Node(new_value, current.next)
            current
