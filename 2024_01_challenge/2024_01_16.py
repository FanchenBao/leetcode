# from pudb import set_trace; set_trace()
from typing import List
import math
from random import randint


class RandomizedSet:

    def __init__(self):
        self.val_map = {}
        self.val_lst = []
        self.hi = 0

    def insert(self, val: int) -> bool:
        if val not in self.val_map:
            if self.hi < len(self.val_lst):
                self.val_lst[self.hi] = val
            else:
                self.val_lst.append(val)
            self.val_map[val] = self.hi
            self.hi += 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.val_map:
            return False
        idx = self.val_map.pop(val)
        self.val_lst[idx] = self.val_lst[self.hi - 1]
        self.hi -= 1
        return True

    def getRandom(self) -> int:
        idx = randint(0, self.hi - 1)
        return self.val_lst[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


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
