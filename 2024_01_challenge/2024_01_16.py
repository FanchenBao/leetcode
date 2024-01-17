# from pudb import set_trace; set_trace()
from typing import List
import math
from random import randint


class RandomizedSet:
    """
    LeetCode 380

    Use a list with a index pointing to the next available spot as a holder
    of all the values. Each time a value is removed, we swap it with the end
    of the list and we move the index backwards.

    There is an edge case that I didn't consider previously, which is when
    the removed item is at the end of the list. When that happens, we should
    not reset the index in the map.

    284 ms, faster than 82.34%

    """
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
        self.hi -= 1
        if self.hi != idx:
            self.val_lst[idx] = self.val_lst[self.hi]
            self.val_map[self.val_lst[idx]] = idx
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
