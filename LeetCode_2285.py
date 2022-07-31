 # from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        """Assign the largest importance to the city with the most number of
        neighbors (is that called degree of a node??). Therefore, this problem
        does not need any search strategy.

        O(N), 2455 ms, faster than 56.28%
        """
        counts = [0] * n
        for a, b in roads:
            counts[a] += 1
            counts[b] += 1
        return sum(c * (i + 1) for i, c in enumerate(sorted(counts)))


sol = Solution()
tests = [
    (5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]], 43),
    (5, [[0,3],[2,4],[1,3]], 20),
]

for i, (n, roads, ans) in enumerate(tests):
    res = sol.maximumImportance(n, roads)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
