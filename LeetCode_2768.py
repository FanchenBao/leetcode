# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        """
        Go through the coordinates and for each black cell, we can increment
        black cells for at most four blocks. We use a tuple as key to keep
        the count of black cells for each block. At the end, we know the number
        of black cells for each recorded blocks.
        
        O(C), where C = len(coordinates), 1705 ms, faster than 91.82%
        """
        coordinates.sort();
        res = [0] * 5
        counter = defaultdict(int)
        for i, j in coordinates:
            for di, dj in [(0, 0), (0, -1), (-1, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m - 1 and 0 <= nj < n - 1:
                    counter[(ni, nj)] += 1
        for v in counter.values():
            res[v] += 1
        res[0] = (n - 1) * (m - 1) - sum(res)
        return res


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
