# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """LeetCode 228

        48 ms, faster than 34.95%
        """
        if not nums:
            return []
        res = []
        st = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                if st == nums[i - 1]:
                    res.append(str(st))
                else:
                    res.append(f'{st}->{nums[i - 1]}')
                st = nums[i]
        if st == nums[-1]:
            res.append(str(st))
        else:
            res.append(f'{st}->{nums[-1]}')
        return res
        

# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
