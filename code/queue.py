from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedListQueue(Generic[T]):
    """[ ] Implement using linked-list, with tail pointer:
    - enqueue(value) - adds value at a position at the tail
    - dequeue() - returns value and removes least recently added element (front)
    - empty()
    """

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            self.size = 1
            return
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.size += 1

    def dequeue(self) -> Optional[T]:
        if self.empty():
            return None
        if self.size == 1:
            res = self.head.value
            self.head = None
            self.tail = None
            self.size -= 1
            return res
        res = self.head.value
        self.head = self.head.next
        self.size -= 1
        return res

    def empty(self):
        return self.size == 0


class ArrayQueue(Generic[T]):
    """[ ] Implement using a fixed-sized array:
    - enqueue(value) - adds item at end of available storage
    - dequeue() - returns value and removes least recently added element
    - empty()
    - full()
    """

    def __init__(self, size) -> None:
        self.queue: List[Optional[T]] = [None for _ in range(size)]
        self.head = 0
        self.tail = 0
        self.size = 0
        self.max_size = size

    def enqueue(self, value):
        if not self.full():
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1

    def dequeue(self):
        if not self.empty():
            res = self.queue[self.head]
            self.head = (self.head + 1) % self.max_size
            self.size -= 1
            return res

    def empty(self):
        return self.size == 0

    def full(self):
        return self.max_size == self.size


if __name__ == "__main__":
    llq: LinkedListQueue[int] = LinkedListQueue()
    llq.enqueue(1)
    llq.enqueue(2)
    llq.enqueue(3)
    assert llq.size == 3
    assert llq.dequeue() == 1
    assert llq.size == 2
    assert llq.dequeue() == 2
    assert llq.dequeue() == 3
    assert llq.empty()

    aq: ArrayQueue[int] = ArrayQueue(6)
    aq.enqueue(1)
    aq.enqueue(2)
    aq.enqueue(3)
    aq.enqueue(4)
    aq.enqueue(5)
    assert aq.dequeue() == 1
    assert aq.dequeue() == 2
    aq.enqueue(6)
    aq.enqueue(7)
    aq.enqueue(8)
    assert aq.full()
    assert aq.dequeue() == 3
