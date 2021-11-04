# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Basic state machine, with no obvious trick.

        O(N), 56 ms, 93% ranking.
        """
        h, e = -math.inf, 0
        for p in prices:
            h, e = max(h, e - p), max(e, h + p)
        return e
        


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
