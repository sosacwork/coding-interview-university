from typing import Any, Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList(Generic[T]):
    """[ ] Implement (I did with tail pointer & without):
    - [ ] size() - returns the number of data elements in the list
    - [ ] empty() - bool returns true if empty
    - [ ] value_at(index) - returns the value of the nth item (starting at 0 for first)
    - [ ] push_front(value) - adds an item to the front of the list
    - [ ] pop_front() - remove the front item and return its value
    - [ ] push_back(value) - adds an item at the end
    - [ ] pop_back() - removes end item and returns its value
    - [ ] front() - get the value of the front item
    - [ ] back() - get the value of the end item
    - [ ] insert(index, value) - insert value at index, so the current item at that index is pointed to by the new item at the index
    - [ ] erase(index) - removes node at given index
    - [ ] value_n_from_end(n) - returns the value of the node at the nth position from the end of the list
    - [ ] reverse() - reverses the list
    - [ ] remove_value(value) - removes the first item in the list with this value
    """

    def __init__(self) -> None:
        self.head: Any[Node] = None
        self.tail: Any[Node] = None
        self.size = 0

    def empty(self):
        return self.size == 0

    def value_at(self, index):
        cur: Any[Node] = self.head
        cur_index = 0
        while cur_index < index:
            cur = cur.next
            cur_index += 1
        return cur.value

    def push_front(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            self.size = 1
            return

        new_head = Node(value, self.head)
        self.head = new_head
        self.size += 1

    def pop_front(self):
        # handle size 0
        if not self.head:
            return

        # handle size 1
        if not self.head.next:
            self.head = None
            self.tail = self.head
            self.size -= 1
            return

        new_head = self.head.next
        self.head.next = None
        self.head = new_head
        self.size -= 1

    def push_back(self, value):
        if self.empty():
            self.head = Node(value)
            self.tail = self.head
            self.size = 1
            return

        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.size += 1

    def pop_back(self):
        if not self.tail:
            return

        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return

        self.size -= 1
        cur_index = 0
        cur_node = self.head
        while cur_index < self.size - 1:
            cur_node = cur_node.next
            cur_index += 1
        cur_node.next = None
        self.tail = cur_node

    def front(self):
        return self.head.value

    def value(self):
        return self.tail.value

    def insert(self, index, value):
        if index > self.size:
            return
        # handle size 0
        if self.empty():
            self.head = Node(value)
            self.tail = self.head
            self.size = 1
            return

        if index == 0:
            self.push_front(value)
        elif index == self.size:
            self.push_back(value)
        else:
            cur_node = self.head
            cur_index = 0
            # traverse to index-1
            while cur_index < index - 1:
                cur_index += 1
                cur_node = cur_node.next
            new_node = Node(value, next=cur_node.next)
            cur_node.next = new_node
            self.size += 1

    def erase(self, index):
        if index >= self.size:
            return
        # handle size 1
        if self.size == 1:
            self.head = None
            self.tail = self.head
            self.size = 0
            return

        cur_index = 0
        cur_node = self.head
        while cur_index < index - 1:
            cur_node = cur_node.next
            cur_index += 1
        cur_node.next = cur_node.next.next
        self.size -= 1

    def value_n_from_end(self, n):
        if n > self.size:
            return
        index = self.size - n
        return self.value_at(index)

    def reverse(self):
        if self.empty() or self.size == 1:
            return

        new_head = LinkedList()
        cur_node = self.head
        while cur_node:
            new_head.push_front(cur_node.value)
            cur_node = cur_node.next

        self.head = new_head.head
        self.tail = new_head.tail
        self.size = new_head.size

    def remove_value(self, value):
        if self.empty():
            return

        cur_node = self.head
        prev_node = None
        while cur_node:
            if cur_node.value == value:
                if not prev_node:
                    self.head = self.head.next
                    self.size -= 1
                    return
                else:
                    prev_node.next = cur_node.next
                    self.size -= 1
                    return

    def display(self):
        cur_node = self.head
        display_str = ""
        while cur_node:
            display_str += f" {cur_node.value}"
            cur_node = cur_node.next
        return display_str


if __name__ == "__main__":
    ll: LinkedList = LinkedList()
    ll.push_front("b")
    ll.push_front("a")
    ll.push_back("c")
    assert " a b c" == ll.display()
    assert ll.size == 3

    ll.pop_back()
    assert " a b" == ll.display()
    ll.pop_front()
    assert " b" == ll.display()
    assert ll.size == 1

    ll.remove_value("b")
    assert ll.empty()

    ll.push_front("b")
    assert "b" == ll.value_at(0)

    ll.insert(0, "a")
    ll.insert(2, "c")
    assert " a b c" == ll.display()
    assert ll.size == 3

    ll.erase(1)
    assert " a c" == ll.display()
    assert ll.size == 2
    assert "a" == ll.value_n_from_end(2)

    ll.reverse()
    assert " c a" == ll.display()
