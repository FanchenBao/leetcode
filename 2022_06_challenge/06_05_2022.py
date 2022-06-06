# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        """LeetCode 52

        This is just the same as N-Queen.

        79 ms, faster than 52.65%
        """
        not_col = set()
        not_tlbr = set()
        not_trbl = set()
        self.res = 0

        def dfs(r: int) -> None:
            if r == n:
                self.res += 1
                return
            for c in range(n):
                if c not in not_col and r + c not in not_trbl and r - c not in not_tlbr:
                    not_col.add(c)
                    not_trbl.add(r + c)
                    not_tlbr.add(r - c)
                    dfs(r + 1)
                    not_col.remove(c)
                    not_trbl.remove(r + c)
                    not_tlbr.remove(r - c)

        dfs(0)
        return self.res


sol = Solution()
tests = [
    ([4,2,1,3], [[1,2],[2,3],[3,4]]),
    ([1,3,6,10,15], [[1,3]]),
    ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.minimumAbsDifference(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
