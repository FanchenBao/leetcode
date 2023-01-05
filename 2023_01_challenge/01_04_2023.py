# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        """LeetCode 2244

        To get minimum steps, we want to take 3 at a time as much as possible.
        If a difficulty's count is divisible by 3, we are good. If divided by
        3, the remainder is 2, we are good. If the remainder is one and if there
        is at least one three to borrow, we can form a 4 and we are good. The
        only case when we are not good is when the count is only one.

        O(N), 1053 ms, faster than 68.85%
        """
        res = 0
        for v in Counter(tasks).values():
            if v == 1:
                return -1
            q, r = divmod(v, 3)
            res += q + int(r != 0)
        return res


sol = Solution()
tests = [
    ([2,2,3,3,2,4,4,4,4,4], 4),
    ([2,3,3], -1),
]

for i, (tasks, ans) in enumerate(tests):
    res = sol.minimumRounds(tasks)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
