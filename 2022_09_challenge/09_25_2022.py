# from pudb import set_trace; set_trace()
from typing import List
import math


class MyCircularQueue:

    def __init__(self, k: int):
        """LeetCode 622

        Use an array, two pointers, a default value for empty cell, and modulo.

        One pointer h always points to the front. One pointer t always points
        to the position right after the end. Since the inputs are all non-
        negative, we use -1 as the sentinel for empty cell. Then empty queue
        happens when t == h and its cell points to -1. Full queueu means t == h
        and its cell points to some non-negative value. The rest becomes self-
        explanatory.

        All operations are O(1). 156 ms, faster than 14.91%
        """
        self.q = [-1] * k
        self.h = 0
        self.t = 0
        self.k = k
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.t] = value
        self.t = (self.t + 1) % self.k
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.h] = -1
        self.h = (self.h + 1) % self.k
        return True

    def Front(self) -> int:
        return self.q[self.h]

    def Rear(self) -> int:
        return self.q[(self.t - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.h == self.t and self.q[self.h] == -1

    def isFull(self) -> bool:
        return self.h == self.t and self.q[self.h] >= 0
        


sol = Solution()
tests = [
    ([4,2,1,3], [[1,2],[2,3],[3,4]]),
    ([1,3,6,10,15], [[1,3]]),
    ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.minimumAbsDifference(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
