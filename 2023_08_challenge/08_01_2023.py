# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """LeetCode 77

        helper(val, rem) gives all the combinations starting from val with rem
        number of elements. We also cache the results.

        78 ms, faster than 99.15%
        """

        @lru_cache(maxsize=None)
        def helper(val: int, rem: int) -> List[List[int]]:
            if n - val + 1 < rem:
                return []
            if n - val + 1 == rem:
                return [list(range(val, n + 1))]
            if rem == 1:
                return [[val]]
            res = []
            for i in range(val + 1, n + 1):
                for comb in helper(i, rem - 1):
                    res.append([val] + comb)
            return res

        res = []
        for i in range(1, n + 1):
            res.extend(helper(i, k))
        return res


class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """This is the more conventional solution with backtracking.

        273 ms, faster than 79.43%
        """
        res = []

        def helper(val: int, comb: List[int]) -> None:
            if len(comb) == k:
                res.append(comb[:])
            else:
                for i in range(val, n + 1):
                    comb.append(i)
                    helper(i + 1, comb)
                    comb.pop()

        helper(1, [])
        return res


sol = Solution2()
tests = [
    (4, 2, [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]),
    (1, 1, [[1]]),
]

for i, (n, k, ans) in enumerate(tests):
    res = sol.combine(n, k)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
