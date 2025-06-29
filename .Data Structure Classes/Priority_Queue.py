class PriorityQueue:
    def __init__(self, values=None):
        self.binary_heap = [0]
        self.size = 0
        if values is not None:
            for num in values:
                self.insert(num)
            self.size = len(values)

    def __str__(self):
        return str(self.binary_heap)

    def __len__(self):
        return self.size

    def percolate_up(self, i):
        while i // 2 > 0 and self.binary_heap[i] < self.binary_heap[i//2]:
            self.binary_heap[i], self.binary_heap[i//2] = self.binary_heap[i//2], self.binary_heap[i]
            i = i // 2

    def get_smaller_child_index(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.binary_heap[i*2] < self.binary_heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def percolate_down(self, i):
        while (i * 2) <= self.size:
            min_child_index = self.get_smaller_child_index(i)
            if self.binary_heap[i] > self.binary_heap[min_child_index]:
                self.binary_heap[min_child_index], self.binary_heap[i] = self.binary_heap[i], self.binary_heap[min_child_index]
            i = min_child_index

    def insert(self, item):
        self.binary_heap.append(item)
        self.size += 1
        self.percolate_up(self.size)

    def get_minimum(self):
        return self.binary_heap[1]        

    def delete_minimum(self):
        return_val = self.binary_heap[1]
        self.binary_heap[1] = self.binary_heap[self.size]
        self.size = self.size - 1
        self.binary_heap.pop()
        self.percolate_down(1)
        return return_val
