# Doubly Ended Stack
class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.data = [-1] * k
        self.front = 0
        self.rear = 0
        self.count = 0  # Number of elements in the deque

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.k) % self.k  # Move front backward
        self.data[self.front] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.rear] = value  # Insert value at rear
        self.rear = (self.rear + 1) % self.k  # Move rear forward
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k  # Move front forward
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.k) % self.k  # Move rear backward
        self.count -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.front]  # Element at front

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.rear - 1 + self.k) % self.k]  # Element at rear

    def isEmpty(self) -> bool:
        return self.count == 0  # True if no elements

    def isFull(self) -> bool:
        return self.count == self.k  # True if count equals capacity

