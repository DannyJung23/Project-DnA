class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class Linked_List:
    def __init__(self):
        self.head = None

    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def remove(self, item):
        found = False
        current = self.head
        previous = None

        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if found:
            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

    def search(self, item):
        current = self.head

        while current != None:
            if current.get_data() == item:
                return True
            else:
                current = current.get_next()

        return False

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count = count + 1
            current = current.get_next()

        return count
