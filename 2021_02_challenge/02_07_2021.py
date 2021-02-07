# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        """We are going to first identify the indices of the letter c in the
        string s. And we know that in the result list, these indices will have
        value 0. For all the other positions, we can evaluate their values by
        starting from the 0 values going to the left and right, and increment
        the distance along the way. We will stop when the incremented distance
        becomes larger than the ones already recorded in the result list.

        O(N), 40 ms, 81% ranking,
        """
        res = [math.inf] * len(s)
        c_idx = []
        for i, le in enumerate(s):
            if le == c:
                res[i] = 0
                c_idx.append(i)
        for j in c_idx:
            # go left:
            m = j - 1
            while m >= 0 and res[m] > j - m:
                res[m] = j - m
                m -= 1
            # go right:
            m = j + 1
            while m < len(s) and res[m] > m - j:
                res[m] = m - j
                m += 1
        return res


class Solution2:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        """The official solution. 2 passes.

        O(N), 32 ms, 97% ranking.
        """
        res = []
        # first pass
        c_idx = -math.inf
        for i in range(len(s)):
            if s[i] == c:
                c_idx = i
            res.append(i - c_idx)
        # second pass
        c_idx = math.inf
        for j in range(len(s) - 1, -1, -1):
            if s[j] == c:
                c_idx = j
            res[j] = min(res[j], c_idx - j)
        return res


sol = Solution2()
tests = [
    ('loveleetcode', 'e', [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]),
    ('aaab', 'b', [3, 2, 1, 0]),
    ('loveleetcode', 'l', [0, 1, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7]),
]

for i, (s, c, ans) in enumerate(tests):
    res = sol.shortestToChar(s, c)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
