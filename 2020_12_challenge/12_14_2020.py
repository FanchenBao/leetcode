# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def partition(self, s: str) -> List[List[str]]:
        """Straightforward recursion solution with no optimization.

        Worst case O(n!), 692 ms, too bad a runtime to have a percentage.

        This solution can pass OJ because the limit of input s length is only
        16.
        """

        def helper(start: int) -> List[List[str]]:
            if start == len(s) - 1:
                return [[s[start]]]
            res = []
            for j in range(start, len(s)):
                cur_str = s[start:j + 1]
                if cur_str == cur_str[::-1]:
                    for remain in helper(j + 1):
                        res.append([cur_str] + remain)
                    if j == len(s) - 1:  # special case: s is palindrome itself
                        res.append([cur_str])
            return res

        return helper(0)


class Solution2:
    def partition(self, s: str) -> List[List[str]]:
        """Using memoization to speed up.

        632 ms, 9% ranking.
        """
        memo = {}

        def helper(start: int) -> List[List[str]]:
            if start == len(s) - 1:
                return [[s[start]]]
            res = []
            if memo.get(start, None):
                return memo[start]
            for j in range(start, len(s)):
                cur_str = s[start:j + 1]
                if cur_str == cur_str[::-1]:
                    for remain in helper(j + 1):
                        res.append([cur_str] + remain)
                    if j == len(s) - 1:  # special case: s is palindrome itself
                        res.append([cur_str])
            memo[start] = res
            return res

        return helper(0)


class Solution3:
    def partition(self, s: str) -> List[List[str]]:
        """Using memoization and is_palindrome mapping to speed up.
        
        604 ms, 10% ranking.

        Apparently, the problem is with the overall algorithm, which cannot be
        sped up by the small boosts.
        """
        memo = {}
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                cur_str = s[i:j + 1]
                is_palindrome[i][j] = cur_str == cur_str[::-1]

        def helper(start: int) -> List[List[str]]:
            if start == n - 1:
                return [[s[start]]]
            res = []
            if memo.get(start, None):
                return memo[start]
            for j in range(start, n):
                if is_palindrome[start][j]:
                    for remain in helper(j + 1):
                        res.append([s[start:j + 1]] + remain)
                    if j == n - 1:  # special case: s is palindrome itself
                        res.append([s[start:j + 1]])
            memo[start] = res
            return res

        return helper(0)


class Solution4:
    def partition(self, s: str) -> List[List[str]]:
        """Better palindrome detection, per idea in the official solution.
        
        644 ms, 8% ranking.
        """
        memo = {}
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        def helper(start: int) -> List[List[str]]:
            if start == n - 1:
                return [[s[start]]]
            res = []
            if memo.get(start, None):
                return memo[start]
            for j in range(start, n):
                if s[start] == s[j] and (j - start <= 1 or is_palindrome[start + 1][j - 1]):
                    is_palindrome[start][j] = True
                    for remain in helper(j + 1):
                        res.append([s[start:j + 1]] + remain)
                    if j == n - 1:  # special case: s is palindrome itself
                        res.append([s[start:j + 1]])
            memo[start] = res
            return res

        return helper(0)


class Solution5:
    def partition(self, s: str) -> List[List[str]]:
        """Backtracking. Official solution

        636 ms, 9% ranking.

        Ok, now I think the test cases have been updated to include either more
        test cases or more extreme cases, because the 50 ms submission has the
        same logic as this one.
        """
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        res = []

        def dfs(start: int, cur_lst: List[str]):
            if start == n:
                res.append(cur_lst[:])
            for j in range(start, n):
                if s[start] == s[j] and (j - start <= 1 or is_palindrome[start + 1][j - 1]):
                    is_palindrome[start][j] = True
                    cur_lst.append(s[start:j + 1])
                    dfs(j + 1, cur_lst)
                    cur_lst.pop()

        dfs(0, [])
        return res


sol = Solution5()
tests = [
    ('aab', [['a', 'a', 'b'], ['aa', 'b']]),
    ('a', [['a']]),
    ('bb', [['b', 'b'], ['bb']]),
    ('abac', [['a', 'b', 'a', 'c'], ['aba', 'c']]),
    ('aabaacbbc', [['a', 'a', 'b', 'a', 'a', 'c', 'b', 'b', 'c'], ['a', 'a', 'b', 'a', 'a', 'c', 'bb', 'c'], ['a', 'a', 'b', 'a', 'a', 'cbbc'], ['a', 'a', 'b', 'aa', 'c', 'b', 'b', 'c'], ['a', 'a', 'b', 'aa', 'c', 'bb', 'c'], ['a', 'a', 'b', 'aa', 'cbbc'], ['a', 'aba', 'a', 'c', 'b', 'b', 'c'], ['a', 'aba', 'a', 'c', 'bb', 'c'], ['a', 'aba', 'a', 'cbbc'], ['aa', 'b', 'a', 'a', 'c', 'b', 'b', 'c'], ['aa', 'b', 'a', 'a', 'c', 'bb', 'c'], ['aa', 'b', 'a', 'a', 'cbbc'], ['aa', 'b', 'aa', 'c', 'b', 'b', 'c'], ['aa', 'b', 'aa', 'c', 'bb', 'c'], ['aa', 'b', 'aa', 'cbbc'], ['aabaa', 'c', 'b', 'b', 'c'], ['aabaa', 'c', 'bb', 'c'], ['aabaa', 'cbbc']]),
]

for i, (s, ans) in enumerate(tests):
    res = sol.partition(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
