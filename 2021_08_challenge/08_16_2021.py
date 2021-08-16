# from pudb import set_trace; set_trace()
from typing import List
from itertools import accumulate


class NumArray:

    def __init__(self, nums: List[int]):
        """LeetCode 303

        Prefix sum is sufficient for this problem.

        O(N) for initiation, O(1) for sumRange. 76 ms, 81% ranking.
        """
        self.prefix_sum = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right] - (self.prefix_sum[left - 1] if left else 0)


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
