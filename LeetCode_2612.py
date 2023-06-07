# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        """TLE
        """
        res = [-1] * n
        res[p] = 0
        queue = [p]
        steps = 0
        banned_set = set(banned)
        while queue:
            tmp = []
            for i in queue:
                lo = max(0, i - k + 1)
                while lo <= i and lo + k - 1 < n:
                    j = lo + k - 1 - (i - lo)
                    if res[j] == -1 and j not in banned_set:
                        res[j] = steps + 1
                        tmp.append(j)
                    lo += 1
            steps += 1
            queue = tmp
        return res


sol = Solution()
tests = [
    (4, 0, [1,2], 4, [0,-1,-1,1]),
    (5, 0, [2,4], 3, [0,-1,-1,-1,-1]),
    (4, 2, [0,1,3], 1, [-1,-1,0,-1]),
]

for i, (n, p, banned, k, ans) in enumerate(tests):
    res = sol.minReverseOperations(n, p, banned, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
