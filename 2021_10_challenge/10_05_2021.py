# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution1:
    
    @lru_cache(maxsize=None)
    def climbStairs(self, n: int) -> int:
        """LeetCode 70

        Top down DP
        O(N), 49 ms
        """
        if n == 2:
            return 2
        if n == 1:
            return 1
        return self.climbStairs(n - 2) + self.climbStairs(n - 1)


class Solution2:
    def climbStairs(self, n: int) -> int:
        """Bottom up DP
        O(N), 24 ms
        """
        if n == 2:
            return 2
        if n == 1:
            return 1
        pp, p = 1, 2
        for i in range(3, n + 1):
            pp, p = p, pp + p
        return p


# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
