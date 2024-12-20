# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        This is the monotonic increasing stack solution. As we produce the
        monotonic increasing stack, we only keep track of the max value when
        popping happens. These max values mark the boundaries of the chunks.
        We do not keep track of the smaller values.

        Think of it this way. Once all the values smaller than the current max
        have been exhausted, no other value down the line can pop the current
        max. Thus, the current max, which marks the bonudary of the current
        chunk, will always sit in the monotonic increasing stack.

        O(N)
        """
        mon: List[int] = []
        for a in arr:
            if not mon or mon[-1] <= a:
                mon.append(a)
            else:
                cur_max = mon[-1]
                while mon and mon[-1] > a:
                    mon.pop()
                mon.append(cur_max)
        return len(mon)


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
