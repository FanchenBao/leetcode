# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution1:
    def partition(self, s: str) -> List[List[str]]:
        """LeetCode 131

        DFS with DP, finding the partition of substring starting from each
        position in s to the end.

        O(N*2^N), 1236 ms, 5% ranking.
        """
        N = len(s)

        @lru_cache(maxsize=None)
        def helper(idx: int) -> List[List[str]]:
            if idx == N:
                return [[]]
            res = []
            for i in range(idx, N):
                cand = s[idx:i + 1]
                if cand == cand[::-1]:
                    for par in helper(i + 1):
                        res.append([cand] + par)
            return res

        return helper(0)


class Solution2:
    def partition(self, s: str) -> List[List[str]]:
        """Bottom up DP, with both partition and palindrome check cached.

        969 ms, 12% ranking.
        """
        N = len(s)
        dp = [[] for _ in range(N + 1)]
        dp[-1].append([])
        is_palindrome = [[False] * N for _ in range(N)]
        for i in range(N - 1, -1, -1):
            for j in range(i, N):
                if s[i] == s[j] and (i + 1 >= j or is_palindrome[i + 1][j - 1]):
                    is_palindrome[i][j] = True
                    cur = s[i:j + 1]
                    for par in dp[j + 1]:
                        dp[i].append([cur] + par)
        return dp[0]


class Solution3:
    def partition(self, s: str) -> List[List[str]]:
        """Backtracking, from the solution of a year ago.

        1036 ms, 8% ranking.

        From this, we can be sure that the test case has been updated. This
        method runs in 636 ms a year ago, but now it runs a lot slower.
        """
        N = len(s)
        is_palindrome = [[False] * N for _ in range(N)]
        res = []

        def dfs(idx: int, cur_par: List[List[str]]):
            if idx == N:
                res.append(cur_par[:])
            else:
                for i in range(idx, N):
                    if s[idx] == s[i] and (idx + 1 >= i or is_palindrome[idx + 1][i - 1]):
                        is_palindrome[idx][i] = True
                        cur_par.append(s[idx:i + 1])
                        dfs(i + 1, cur_par)
                        cur_par.pop()  # backtracking

        dfs(0, [])
        return res


sol = Solution3()
tests = [
    ('aab', [['a', 'a', 'b'], ['aa', 'b']]),
    ('a', [['a']]),
]

for i, (s, ans) in enumerate(tests):
    res = sol.partition(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
