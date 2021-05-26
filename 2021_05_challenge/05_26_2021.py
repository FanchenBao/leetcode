# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def minPartitions(self, n: str) -> int:
        """LeetCode 1689

        The reasoning is that for each deci-binary number, the max for a
        position is 1. Therefore, for the position in n that has the largest
        digit, we need at least that digit number of deci-binary to sum up to
        that digit. For all the other positions, we can always swap in 0s to
        make the sum work.

        Therefore, the answer is the largest digit in n.

        O(N), 40 ms, 95% ranking.
        """
        return int(max(n))

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
