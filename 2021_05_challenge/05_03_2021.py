# from pudb import set_trace; set_trace()
from typing import List
from itertools import accumulate


class Solution1:
    def runningSum(self, nums: List[int]) -> List[int]:
        """LeetCode 1480
        Very simple question. Nothing more to say
        """
        return list(accumulate(nums))


class Solution2:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [nums[0]]
        for n in nums[1:]:
            res.append(n + res[-1])
        return res


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
