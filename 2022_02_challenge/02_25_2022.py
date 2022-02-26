# from pudb import set_trace; set_trace()
from typing import List
from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """LeetCode 165

        Split on dot, zip longest with '0' as fill, and compare from left to
        right.

        O(N), 51 ms, 29% ranking.
        """
        for v1, v2 in zip_longest(version1.split('.'), version2.split('.'), fillvalue='0'):
            if int(v1) > int(v2):
                return 1
            if int(v1) < int(v2):
                return -1
        return 0


sol = Solution()
tests = [
    ('1.01', '1.001', 0),
    ('1.0', '1.0.0', 0),
    ('0.1', '1.1', -1),
]

for i, (version1, version2, ans) in enumerate(tests):
    res = sol.compareVersion(version1, version2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
