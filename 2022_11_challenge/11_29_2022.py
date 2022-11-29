# from pudb import set_trace; set_trace()
from typing import List
import math
from random import choice


class RandomizedSet1:

    def __init__(self):
        """LeetCode 380

        This is cheating. We use O(N) for the getRandom method, not the required
        O(1). 1614 ms, faster than 10.94% 
        """
        self.random_set = set()

    def insert(self, val: int) -> bool:
        if val not in self.random_set:
            self.random_set.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.random_set:
            self.random_set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return choice(list(self.random_set))


class RandomizedSet2:

    def __init__(self):
        """getRandom is faster than O(N), but not sure if it can be counted as O(1)

        1153 ms, faster than 36.57%
        """
        self.m = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val not in self.m:
            self.m[val] = 1
            self.vals.append(val)
            return True
        if self.m[val] == 0:
            self.m[val] = 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.m and self.m[val] == 1:
            self.m[val] = 0
            return True
        return False

    def getRandom(self) -> int:
        while True:
            res = choice(self.vals)
            if self.m[res] == 1:
                return res


class RandomizedSet3:

    def __init__(self):
        """This is the smart solution. Use pop of a stack to remove. Use stack
        to keep track of all unique values. Use val-index map to keep track of
        the indices of all values. If a value is to be removed, we find its
        index first, and then swap it with the top of the stack. Then we pop the
        stack for removal.

        436 ms, faster than 90.76%
        """
        self.m = {}
        self.stack = []

    def insert(self, val: int) -> bool:
        if val not in self.m:
            self.stack.append(val)
            self.m[val] = len(self.stack) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.m:
            idx = self.m.pop(val)
            if idx != len(self.stack) - 1:
                self.stack[idx], self.stack[-1] = self.stack[-1], self.stack[idx]
                self.m[self.stack[idx]] = idx
            self.stack.pop()
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.stack)



sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
