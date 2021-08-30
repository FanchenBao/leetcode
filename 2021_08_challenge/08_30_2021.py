# from pudb import set_trace; set_trace()
from typing import List
import operator


class Solution1:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        """LeetCode 598

        The goal is to find the region that is overlapped by all ops. The
        size of the region is the final answer. To find such region, we always
        keep the min value of the row and col count of each op.

        O(N) time and O(1) space. 109 ms, 6% ranking.
        """
        r, c = m, n
        for i, j in ops:
            r = min(r, i)
            c = min(c, j)
        return r * c


class Solution2:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        """Use zip(*ops) to transpose ops such that we have each column in ops
        as an array.

        Courtesy: https://leetcode.com/problems/range-addition-ii/discuss/1434377/Python-oneliner-explained/1066215
        """
        return operator.mul(*(min(col) for col in zip(*ops))) if ops else m * n


sol = Solution2()
tests = [
    (3, 3, [[2, 2], [3, 3]], 4),
    (3, 3, [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]], 4),
    (3, 3, [], 9),
]

for i, (m, n, ops, ans) in enumerate(tests):
    res = sol.maxCount(m, n, ops)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
