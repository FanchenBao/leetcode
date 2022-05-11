# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """LeetCode 216

        Backtracking.

        O(9Ck), 33 ms, faster than 84.45%
        """
        res = []

        def helper(start: int, c: List[int], s: int) -> None:
            if len(c) == k and s == n:
                res.append(c[:])
            elif s < n:
                for v in range(start, 10):
                    c.append(v)
                    helper(v + 1, c, s + v)
                    c.pop()  # backtracking

        helper(1, [], 0)
        return res


sol = Solution()
tests = [
    (3, 7, [[1,2,4]]),
    (3, 9, [[1,2,6],[1,3,5],[2,3,4]]),
    (4, 1, []),
]

for i, (k, n, ans) in enumerate(tests):
    res = sol.combinationSum3(k, n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
