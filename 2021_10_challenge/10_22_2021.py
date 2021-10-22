# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        """LeetCode 451

        Thanks to Python's very rich built in library, we can solve this
        problem in oneline using Counter.

        O(NlogN), because most_common() most likely takes O(NlogN).

        58 ms, 48% ranking.
        """
        return ''.join(k * v for k, _ in Counter(s).most_common())
        



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
