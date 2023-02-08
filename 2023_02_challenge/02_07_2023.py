# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """LeetCode 904

        Sliding window

        O(N), 1095 ms, faster than 40.61%
        """
        c = Counter()
        res = lo = 0
        for hi in range(len(fruits)):
            c[fruits[hi]] += 1
            while len(c) > 2:
                c[fruits[lo]] -= 1
                if c[fruits[lo]] == 0:
                    del c[fruits[lo]]
                lo += 1
            res = max(res, hi - lo + 1)
        return res


sol = Solution()
tests = [
    ([1,2,1], 3),
    ([0,1,2,2], 3),
    ([1,2,3,2,2], 4),
]

for i, (fruits, ans) in enumerate(tests):
    res = sol.totalFruit(fruits)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
