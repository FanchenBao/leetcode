# from pudb import set_trace; set_trace()
from typing import List
from itertools import accumulate


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        """LeetCode 1413

        Prefix sum

        O(N), 28 ms, 90% ranking.
        """
        return max(1 - min(accumulate(nums)), 1)


# sol = Solution()
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
