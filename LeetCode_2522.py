# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def minimumPartition(self, s: str, k: int) -> int:
        """Greedy. From the start, find the largest substring that is smaller or
        equal to k.

        Don't forget to check the last element remaining.

        O(N), 353 ms, faster than 27.34%
        """
        res = cur = 0
        for d in s:
            dd = int(d)
            nex = cur * 10 + dd
            if 0 < cur <= k and nex > k:
                res += 1
            elif cur > k:
                return -1
            cur = dd if nex > k else nex
        if cur <= k:
            res += 1
        else:
            return -1
        return res if res > 0 else -1


class Solution2:
    def minimumPartition(self, s: str, k: int) -> int:
        """better implementation

        O(N), 133 ms, faster than 87.69%
        """
        res = cur = 0
        for d in s:
            dd = int(d)
            cur = cur * 10 + dd
            if cur > k:
                res += 1
                cur = dd
            if cur > k:
                return -1
        if cur <= k:
            res += 1
        else:
            return -1
        return res



sol = Solution2()
tests = [
    ("165462", 60, 4),
    ("238182", 5, -1),
    ("12456", 5, -1),
]

for i, (s, k, ans) in enumerate(tests):
    res = sol.minimumPartition(s, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
