# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """LeetCode 1074

        Yet another difficult one, but this one is significantly easier than
        yesterday's, because its implementation is complex but not necessarily
        difficult. I did have to use the hint, which points to the most
        important insight: restrict the problem to a space between rows. Once
        we do that, we basically try to find the number of "subarray"
        bounded by the two rows that sum up to target. We can do that with a
        counter of prefix sum.

        O(MN^2), 1714 ms, faster than 25.60% 
        """
        m, n = len(matrix), len(matrix[0])
        psum = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            pr = 0
            for j in range(n):
                pr += matrix[i][j]
                psum[i][j] += pr + (psum[i - 1][j] if i > 0 else 0)
        for r1 in range(m):
            for r2 in range(r1, m):
                counter = Counter([0])
                for j in range(n):
                    cur = psum[r2][j] - (psum[r1 - 1][j] if r1 > 0 else 0)
                    res += counter[cur - target]
                    counter[cur] += 1
        return res


sol = Solution()
tests = [
    ([[0,1,0],[1,1,1],[0,1,0]], 0, 4),
    ([[1,-1],[-1,1]], 0, 5),
    ([[904]], 0, 0),
]

for i, (matrix, target, ans) in enumerate(tests):
    res = sol.numSubmatrixSumTarget(matrix, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
