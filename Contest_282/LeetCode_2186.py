# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs, ct = Counter(s), Counter(t)
        res = 0
        for a, c in cs.items():
            dif = max(c - ct[a], 0)
            ct[a] += dif
            res += dif
        for a, c in ct.items():
            dif = max(c - cs[a], 0)
            cs[a] += dif
            res += dif
        return res
        
        


# sol = Solution()
# tests = [
#     ([3,1,3,2,4,3], 3),
#     ([1,2,2,2,2], 2),
#     ([1], 0),
# ]

# for i, (nums, ans) in enumerate(tests):
#     res = sol.minimumOperations(nums)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
