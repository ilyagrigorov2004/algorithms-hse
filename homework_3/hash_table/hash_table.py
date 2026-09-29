class HashTable:

    def __init__(self, size=10):
        self.size = size
        a = []
        for _ in range(size):
            a.append([])
        self.table = a
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)

        for i in range(len(self.table[index])):
            k, v = self.table[index][i]
            if k == key:
                self.table[index][i] = (key, value)
                return

        self.table[index].append((key, value))
        self.count += 1

        if self.count / self.size > 0.75:
            self._resize()

    def get(self, key):
        index = self._hash(key)
        for i in range(len(self.table[index])):
            k, v = self.table[index][i]
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        for i in range(len(self.table[index])):
            k, v = self.table[index][i]
            if k == key:
                self.table[index].pop(i)
                self.count -= 1
                return True
        return False

    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)



