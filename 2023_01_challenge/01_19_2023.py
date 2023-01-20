# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter
from itertools import accumulate


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """LeetCode 974

        Use prefix sum, find each prefix sum's remainder after MOD k, then count
        the frequency of each remainder. For each frequency we use combination
        to calculate the total number. The only tricky part is to consider
        remainder zero separately, because each individual prefix sum that has
        zero remainder counts towards the results.

        O(N), 296 ms, faster than 92.70% 
        """
        return sum(int(k == 0) * c + math.comb(c, 2) for k, c in Counter(a % k for a in accumulate(nums)).items())
        

sol = Solution()
tests = [
    ([4,5,0,-2,-3,1], 5, 7),
    ([5], 9, 0),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.subarraysDivByK(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
