# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution1:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        """Record the min number of moves that convert s to t. Use a counter to
        keep track of the number of times each move is needed.

        Then for all duplicated moves, we need to add the most number of cycles
        needed to the move (each cycle has 26 additional moves), and compare it
        to k. If it is larger than k, we cannot make the convertion.

        O(N), 624 ms, faster than 38.05%
        """
        if len(s) != len(t):
            return False
        if s == t:
            return True
        counter = Counter()
        for ls, lt in zip(s, t):
            if ls != lt:
                diff = ord(lt) - ord(ls)
                counter[diff if diff > 0 else diff + 26] += 1
        if max(counter) > k:
            return False
        return all(move + 26 * (c - 1) <= k for move, c in counter.items())


class Solution2:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        """Same idea but better implementation

        Ref: https://leetcode.com/problems/can-convert-string-in-k-moves/discuss/779903/JavaPython-3-O(n)-Count-the-shift-displacement-w-brief-explanation-and-analysis.

        O(N)
        """
        if len(s) != len(t):
            return False
        if s == t:
            return True
        # record number of times a certain number of moves is duplicated.
        # min number of moves is at most 25, so we can use a list
        counter = [0] * 26
        for ls, lt in zip(s, t):
            if ls != lt:
                diff = ord(lt) - ord(ls)
                if diff < 0:
                    diff += 26
                if counter[diff] * 26 + diff > k:
                    return False
                counter[diff] += 1
        return True


sol = Solution2()
tests = [
    ("input", "ouput", 9, True),
    ("abc", "bcd", 10, False),
    ("aab", "bbb", 27, True),
    ('aa', 'aa', 0, True),
]

for i, (s, t, k, ans) in enumerate(tests):
    res = sol.canConvertString(s, t, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
