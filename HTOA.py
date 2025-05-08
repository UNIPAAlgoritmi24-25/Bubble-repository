import random

class OpenAddressingHashTable:
    def __init__(self, size=11):
        self.size = size
        self.table = [None] * size

    def __str__(self):
        result = ""
        for i, val in enumerate(self.table):
            result += f"{i}: {val}\n"
        return result


# Linear Probing -
class HashTableLinearProbing(OpenAddressingHashTable):
    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        i = 0
        while i < self.size:
            index = (self.hash_function(key) + i) % self.size
            if self.table[index] is None:
                self.table[index] = key
                return
            i += 1

    def search(self, key):
        i = 0
        while i < self.size:
            index = (self.hash_function(key) + i) % self.size
            if self.table[index] is None:
                return None
            if self.table[index] == key:
                return index
            i += 1
        return None


#Double Hashing Version
class HashTableDoubleHashing(OpenAddressingHashTable):
    def h1(self, key):
        return key % self.size

    def h2(self, key):
        return 1 + (key % (self.size - 1)) #-1 per prendere un coprimo poco più piccolo

    def hash_function(self, key, i):
        return (self.h1(key) + i * self.h2(key)) % self.size

    def insert(self, key):
        i = 0
        while i < self.size:
            index = self.hash_function(key, i)
            if self.table[index] is None:
                self.table[index] = key
                return
            i += 1

    def search(self, key):
        i = 0
        while i < self.size:
            index = self.hash_function(key, i)
            if self.table[index] is None:
                return None
            if self.table[index] == key:
                return index
            i += 1
        return None


if __name__ == "__main__":
    keys = random.sample(range(1, 100), 8)

    print("Linear Probing:")
    ht_linear = HashTableLinearProbing(size=11)
    for k in keys:
        ht_linear.insert(k)
    print(ht_linear)
    for k in [keys[0], keys[1], 999]:
        res = ht_linear.search(k)
        print(f"{k} found at {res}" if res is not None else f"{k} not found")

    print("\nDouble Hashing:")
    ht_double = HashTableDoubleHashing(size=11)
    for k in keys:
        ht_double.insert(k)
    print(ht_double)
    for k in [keys[0], keys[1], 999]:
        res = ht_double.search(k)
        print(f"{k} found at {res}" if res is not None else f"{k} not found")
