# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        """O(N), 129 ms, faster than 51.36%
        """
        ls, rs = Counter(), Counter(nums)
        res = []
        for n in nums:
            ls[n] += 1
            rs[n] -= 1
            if not rs[n]:
                del rs[n]
            res.append(len(ls) - len(rs))
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
