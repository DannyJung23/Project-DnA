class DoubleHashTable:
    def __init__(self, size=7, secondary_hash_value=5):
        self.size = size
        self.slots = [None] * size
        self.secondary_hash_value = secondary_hash_value

    def __str__(self):
        return str(self.slots)

    def get_hash_index(self, key):
        return key % self.size

    def clear(self):
        self.slots = [None] * self.size

    def is_empty(self):
        return self.__len__() == 0

    def __len__(self):
        return sum([1 if item != None else 0 for item in self.slots])

    def put(self, key):
        original_index = index = self.get_hash_index(key)
        step = 1
        step_size = self.get_step_size(key)
        while self.slots[index] != None:
            index = (original_index + step * step_size) % self.size
            step += 1
        self.slots[index]=key

    def get_step_size(self, key):
        return self.secondary_hash_value - (key % self.secondary_hash_value)
