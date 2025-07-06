class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def add_after(self, value):
        new_node = Node(value,self.next )
        self.next = new_node

    def remove_after(self):
        self.next = self.next.get_next()

    def __str__(self):
        return str(self.data)
