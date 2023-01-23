# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution1:
    def partition(self, s: str) -> List[List[str]]:
        """LeetCode 131

        DFS with memoization. helper(i) returns all the palindrome partition
        of s[i:]. Thus, for each helper(i), we find the first parlindrome
        partition, and delegate the remaining for the next recursion.

        595 ms, faster than 99.82%
        """
        N = len(s)

        @lru_cache(maxsize=None)
        def helper(idx: int) -> List[List[str]]:
            if idx == N:
                return [[]]
            res = []
            for i in range(idx, N):
                cur = s[idx:i + 1]
                if cur == cur[::-1]:
                    for part in helper(i + 1):
                        res.append([cur] + part)
            return res

        return helper(0)


class Solution2:
    def partition(self, s: str) -> List[List[str]]:
        """Backtracking, with the smart idea for checking palindrome.

        1723 ms, faster than 21.65%
        """
        N = len(s)
        is_palin = [[False] * N for _ in range(N)]
        res = []

        def dfs(idx: int, par: List[str]) -> None:
            if idx == N:
                res.append(par[:])
            else:
                for i in range(idx, N):
                    if s[i] == s[idx] and (i == idx or idx + 1 == i or is_palin[idx + 1][i - 1]):
                        is_palin[idx][i] = True
                        par.append(s[idx:i + 1])
                        dfs(i + 1, par)
                        par.pop()
        dfs(0, [])
        return res


sol = Solution2()
tests = [
    ("aab", [["a","a","b"],["aa","b"]]),
    ('a', [['a']]),
]

for i, (s, ans) in enumerate(tests):
    res = sol.partition(s)
    res.sort()
    ans.sort()
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
