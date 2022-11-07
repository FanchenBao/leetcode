# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import deque


class Solution:
    def solve_k_equal_one(self, s: str) -> str:
        """UPDATE: this can be written in a much easier way"""
        res = s
        for i in range(1, len(s)):
            res = min(res, s[i:] + s[:i])
        return res

    def orderlyQueue(self, s: str, k: int) -> str:
        """LeetCode 899

        Think about it this way. If each time we select the smallest value in
        the first k letters and put it to the end, eventually after going
        through all the letters, it is guaranteed that the largest letter in s
        is in the first k letters. We can then put that letter to the end, such
        that we have successfully placed the largest letter in its sorted place.
        Then, we don't have to worry about that sorted letter again, because
        it is already in place, which means we know exactly when that letter
        needs to be popped and pushed to the back in the future rounds.
        Therefore, we can focus on the remaining letters and find the second
        largest letter. Eventually, this will leads to a fully sorted string.

        The only exception is when k == 1, because in this scenario, it is not
        possible to do any choices. Thus, k == 1 has to be treated separately.
        """
        if k == 1:
            return self.solve_k_equal_one(s)
        return ''.join(sorted(s))
        

sol = Solution()
tests = [
    ("cba", 1, 'acb'),
    ("baaca", 3, 'aaabc'),
    ("caaba", 3, 'aaabc'),
    ("rewtrgfsw", 2, "efgrrstww"),
    ("wqeqertyuikjgh", 3, "eeghijkqqrtuwy"),
]

for i, (s, k, ans) in enumerate(tests):
    res = sol.orderlyQueue(s, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
