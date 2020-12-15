# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """Very easy question. All built-in function calls.

        O(N) because Python uses timsort, 204 ms, 86%
        """
        return sorted(n * n for n in nums)


class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """Two pointer solution. I saw it in the title of the discussion posts
        and decided to implement it myself.

        O(N), 240 ms, 31% ranking.
        """
        i, n = 0, len(nums)
        while i < n and nums[i] < 0:
            i += 1
        j = i - 1
        res = []
        while i < len(nums) or j >= 0:
            i2 = nums[i] * nums[i] if i < n else math.inf
            j2 = nums[j] * nums[j] if j >= 0 else math.inf
            if i2 < j2:
                res.append(i2)
                i += 1
            else:
                res.append(j2)
                j -= 1
        return res


class Solution3:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """Better two pointer solution, from
        https://leetcode.com/explore/featured/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3567/discuss/221922/Java-two-pointers-O(N)

        The intuition is that the largest possible values are always towards the
        end of the original nums array. So we pick either one each time and
        move the two pointers towards the center.

        O(N), 232 ms, 38% ranking.
        """
        i, j = 0, len(nums) - 1
        res = []
        while i <= j:
            i2, j2 = nums[i] * nums[i], nums[j] * nums[j]
            if i2 > j2:
                res.append(i2)
                i += 1
            else:
                res.append(j2)
                j -= 1
        return res[::-1]


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
