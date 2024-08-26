class HashTable:
    """Implement with array using linear probing
    - hash(k, m) - m is the size of the hash table
    - add(key, value) - if the key already exists, update value
    - exists(key)
    - get(key)
    - remove(key)
    """

    def __init__(self, m=10) -> None:
        self.size = 0
        self.m = m
        self.hash_table: list = [None for _ in range(self.m)]

    def add(self, k, v):
        print("adding")
        if self.size == self.m:
            print("reach m")
            return
        key = None
        for i in range(0, self.m):
            key = (hash(k) + i) % self.m
            if not self.hash_table[key]:
                break
        if key is not None:
            self.hash_table[key] = (k, v)
            self.size += 1

    def exists(self, k):
        print("checking exists")
        for i in range(0, self.m):
            key = (hash(k) + i) % self.m
            if self.hash_table[key] is None:
                break
            if self.hash_table[key] and self.hash_table[key][0] == k:
                return True
        return False

    def get(self, k):
        print("getting")
        for i in range(0, self.m):
            key = (hash(k) + i) % self.m
            if self.hash_table[key] and self.hash_table[key][0] == k:
                return self.hash_table[key][1]
        return None

    def remove(self, k):
        print("removing")
        for i in range(0, self.m):
            key = (hash(k) + i) % self.m
            if self.hash_table[key]:
                self.hash_table[key] = False
                self.size -= 1
                break

    def display(self):
        print("displaying")
        for i, e in enumerate(self.hash_table):
            print(f"{i} - {e}")


if __name__ == "__main__":
    hash_table = HashTable()
    hash_table.add("a", "elem 1")
    hash_table.display()
    hash_table.add(1, "elem 2")
    hash_table.display()
    assert hash_table.exists("a")
    assert hash_table.exists("b") is False
    for i in range(8):
        hash_table.add(f"a{i}", f"elem {i+2}")
    hash_table.display()
    for i in range(5):
        hash_table.remove(f"a{i}")
    hash_table.display()
    assert hash_table.get("a5") == "elem 7"
