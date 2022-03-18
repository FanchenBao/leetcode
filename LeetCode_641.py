# from pudb import set_trace; set_trace()
from typing import List


class Node:
    def __init__(self, val=-1):
        self.val = val
        self.next = None
        self.prev = None


class MyCircularDeque:
    """Use a doubly linked list, this problem is not very hard

    All operations is in O(1)

    108 ms, 43% ranking.
    """

    def __init__(self, k: int):
        self.cap = k
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.cap -= 1
        node = Node(val=value)
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.cap -= 1
        node = Node(val=value)
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.cap += 1
        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        node.next = node.prev = None
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.cap += 1
        node = self.tail.prev
        self.tail.prev = node.prev
        node.prev.next = self.tail
        node.next = node.prev = None
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.val
        
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def isFull(self) -> bool:
        return self.cap == 0


class MyCircularDeque:
    """Much faster than the doubly linked list implementation. This one uses a
    single list. By performing index wrapping around, we are able to keep two
    pointers always pointing to the next position for adding values. In this
    set up, we can tell emptiness by checking f + 1 == b, and fullness by
    checking f == b. Of course, all the plus or minus index arithmetic must
    go through modulo.

    O(1) for each operation.

    68 ms, 96% ranking.
    """

    def __init__(self, k: int):
        self.deque = [0] * (k + 1)
        self.f = 0
        self.b = 1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque[self.f] = value
        self.f = (self.f - 1 + len(self.deque)) % len(self.deque)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque[self.b] = value
        self.b = (self.b + 1) % len(self.deque)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.f = (self.f + 1) % len(self.deque)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.b = (self.b - 1 + len(self.deque)) % len(self.deque)
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[(self.f + 1) % len(self.deque)]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[(self.b - 1 + len(self.deque)) % len(self.deque)]

    def isEmpty(self) -> bool:
        return (self.f + 1) % len(self.deque) == self.b

    def isFull(self) -> bool:
        return self.f == self.b


# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
