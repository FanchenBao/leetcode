# from pudb import set_trace; set_trace()
from typing import List


class MyCircularQueue:
    """This is a fairly straightforward question with only one trick: how to
    design the pointer that points to the front and rear of the circular queue.
    The answer is that when the queue is empty, the front pointer is always one
    position ahead of the rear pointer. And of course, in our implementation,
    the rear pointer has to start from -1. The wrap around is a simple mod.

    O(N), 68 ms, 72% ranking.
    """

    def __init__(self, k: int):
        self.size = 0
        self.cap = k
        self.f = 0
        self.r = -1
        self.queue: List = [-1] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.r = (self.r + 1) % self.cap
        self.queue[self.r] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.f = (self.f + 1) % self.cap
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.queue[self.f] if self.size else -1

    def Rear(self) -> int:
        return self.queue[self.r] if self.size else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap


# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
