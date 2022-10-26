# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate
from collections import defaultdict


class Solution1:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """LeetCode 523

        This problem is notorious for its many tricky edge cases involving zero.
        The basic idea is to create a prefix mod, which is composed of prefix
        sum mod k. As long as we have 0 or some repeats of prefix mod, we will
        have a high chance to get a subarray sum to be multiple of k.

        However, the tricky part is that with zero in the mix, we have a lot
        of conditions to consider. For instance, [1,0] with k = 2 is false,
        but its prefix mod is [1, 1], which seems to be good. My initial idea
        is to get rid of all zeroes, but then I failed test cases such as
        [5,0,0,0] with k = 3 and [0,1,0] with k = 1.

        Eventually, I decided to not use any fancy method. We simply create
        both the prefix sum and prefix mod. For each possible case in prefix
        mod, we check the length of the subarray and the sum of the subarray
        before making the decision. This turns out to be correct.

        O(N), 2411 ms, faster than 40.06%
        """
        presum = list(accumulate(nums, initial=0))
        premod_dict = defaultdict(list)
        premod_dict[0].append(0)
        for i, ps in enumerate(presum[1:], 1):
            m = ps % k
            premod_dict[m].append(i)
            j = premod_dict[m][0]
            if i - j >= 2 and (presum[i] - presum[j] >= k or presum[i] == presum[j]):
                return True
        return False


class Solution2:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """Same idea as Solution1, but two key insights.

        1. we don't have to keep a list of premod indices. We only need the
        index of the first occurrence of a mod value.
        2. We don't have to check for presum[i] - presum[j] >= k, because if
        its smaller than k, it's impossible if i - j < 2, but it is possible
        if i - j >= 2 (this is the case where we have multiple consecutive
        zeroes)
        """
        ps = 0
        premod_dict = {0: -1}
        for i, n in enumerate(nums):
            ps = (ps + n) % k
            if ps not in premod_dict:
                premod_dict[ps] = i
            if i - premod_dict[ps] >= 2:
                return True
        return False


sol = Solution2()
tests = [
    ([23,2,4,6,7], 6, True),
    ([23,2,6,4,7], 6, True),
    ([23,2,6,4,7], 13, False),
    ([1,0], 2, False),
    ([5,0,0,0], 3, True),
    ([0,1,0], 1, True),
    ([0,2], 2, True),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.checkSubarraySum(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
