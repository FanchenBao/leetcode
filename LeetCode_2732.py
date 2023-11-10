# from pudb import set_trace; set_trace()
from typing import List
import math
import operator
from functools import reduce


class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        """
        Since there are only five cols, it is very natural to consider each row
        as a bitmask.

        Then by observation, to have one row as good, we need the row bitmask to
        be zero. Thus, if we go through the grid and find one bitmask being zero
        we can immediately return its index as the answer.

        If we want to have two rows as good, then the two bitmasks must have an
        AND as zero. This means, if there exists any bitmask_i & bitmask_j == 0,
        we can return [i, j] as answer (i < j)

        Hence, the problem becomes finding any two bitmasks in the grid whose
        AND value is zero.

        We solve this problem by recording one index of each bitmask. Then for
        each bitmask, go through all the other bitmasks that can make it AND to
        zero, and check if that other bitmask exists in the grid. If it does,
        we have found our solution. There are only 31 values to try because the
        largest bitmask is 31.

        O(N), 1823 ms, faster than 38.41%
        """
        indices = [-1] * 32
        for i, row in enumerate(grid):
            b = int(''.join(str(r) for r in row), 2)
            if b == 0:
                return [i]
            indices[b] = i
        for a in range(1, 32):
            if indices[a] >= 0:
                for b in range(1, 32):
                    if a & b == 0 and indices[b] >= 0:
                        return sorted([indices[a], indices[b]])
        return []


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
