from typing import Generic, List, TypeVar, Union

T = TypeVar("T")


class Array(Generic[T]):
    """
    - [ ] Implement a vector (mutable array with automatic resizing):
    - [ ] Practice coding using arrays and pointers, and pointer math to jump to an index instead of using indexing.
    - [ ] New raw data array with allocated memory
        - can allocate int array under the hood, just not use its features
        - start with 16, or if the starting number is greater, use power of 2 - 16, 32, 64, 128
    - [ ] size() - number of items
    - [ ] capacity() - number of items it can hold
    - [ ] is_empty()
    - [ ] at(index) - returns the item at a given index, blows up if index out of bounds
    - [ ] push(item)
    - [ ] insert(index, item) - inserts item at index, shifts that index's value and trailing elements to the right
    - [ ] prepend(item) - can use insert above at index 0
    - [ ] pop() - remove from end, return value
    - [ ] delete(index) - delete item at index, shifting all trailing elements left
    - [ ] remove(item) - looks for value and removes index holding it (even if in multiple places)
    - [ ] find(item) - looks for value and returns first index with that value, -1 if not found
    - [ ] resize(new_capacity) // private function
        - when you reach capacity, resize to double the size
        - when popping an item, if the size is 1/4 of capacity, resize to half
    """

    def __init__(self, capacity) -> None:
        self.size = 0
        self.capacity = capacity
        self.cur_list: List[Union[T, bool]] = [False for _ in range(capacity)]
        self.last_index = 0  # index that can insert

    def is_empty(self):
        return self.size == 0

    def at(self, index):
        self._validate_index(index)
        return self.cur_list[index]

    def push(self, item):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self.cur_list[self.last_index] = item
        self.last_index += 1
        self.size += 1

    def insert(self, index, value):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self._validate_index(index)
        i = 0
        res = []
        while i <= self.size:
            if i == index:
                res.append(value)
            res.append(self.get(i))
            i += 1
        self.size += 1
        self.last_index += 1
        return res

    def prepend(self, item):
        self.insert(0, item)

    def pop(self):
        if self.size == 0:
            return
        res = self.cur_list[self.last_index - 1]
        self.last_index = max(self.last_index - 1, 0)
        self.size -= 1
        if self.size <= self.capacity / 4:
            self._resize(self.capacity // 2)
        return res

    def delete(self, index):
        """delete(index) - delete item at index, shifting all trailing elements left"""
        self._validate_index(index)
        while index < self.size - 1:
            self.cur_list[index] = self.cur_list[index + 1]
            index += 1
        self.size -= 1
        self.last_index -= 1
        if self.size <= self.capacity / 4:
            self._resize(self.capacity // 2)

    def remove(self, item):
        """looks for value and removes index holding it (even if in multiple places)"""
        i = self.size - 1
        while i >= 0:
            if self.cur_list[i] == item:
                self.delete(i)
            i -= 1

    def find(self, item):
        """looks for value and returns first index with that value, -1 if not found"""
        i = 0
        while i < self.size:
            if self.cur_list[i] == item:
                return i
            i += 1
        return -1

    def _resize(self, new_capacity):
        """
        resize(new_capacity) // private function
        - when you reach capacity, resize to double the size
        - when popping an item, if the size is 1/4 of capacity, resize to half
        """
        print(f"resize to {new_capacity}")
        new_list = [False for _ in range(new_capacity)]
        for i in range(0, self.last_index):
            new_list[i] = self.cur_list[i]
        self.cur_list = new_list
        self.capacity = new_capacity

    def _validate_index(self, index):
        if index < 0 or index >= self.size:
            return Exception("Index out of range")


if __name__ == "__main__":
    dynamic_array: Array = Array(3)
    dynamic_array.push(1)
    assert dynamic_array.size == 1
    dynamic_array.push(2)
    dynamic_array.push(3)
    assert dynamic_array.size == 3
    assert dynamic_array.last_index == 3
    assert dynamic_array.capacity == 3
    dynamic_array.push(4)
    assert dynamic_array.last_index == 4
    assert dynamic_array.capacity == 6

    dynamic_array.pop()
    assert dynamic_array.last_index == 3
    assert dynamic_array.size == 3

    assert dynamic_array.find(3)
    assert dynamic_array.find(4) == -1

    dynamic_array.delete(1)
    assert dynamic_array.last_index == 2
    assert dynamic_array.size == 2
    assert dynamic_array.find(2) == -1

    dynamic_array.push(1)
    dynamic_array.push(1)
    dynamic_array.push(1)
    dynamic_array.remove(1)
    assert dynamic_array.last_index == 1
    assert dynamic_array.size == 1
