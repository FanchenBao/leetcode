# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        """Use sliding window to find a subarray that has at least k pairs. We
        use a counter to facilitate the counting of pairs.

        We increment hi until the first subarray is found where there are at
        least k pairs. We then reduce lo to find the longest subarray
        with the number of pairs just below k. Then we know, from start to
        nums[lo - 1], every subarray is good. We increment result by lo.

        As we increment hi, the new subarray might not have k pairs. However,
        since we have already shown that a previous subarray satisfies the
        requirement. Thus, as long as the current subarray include the previous
        good subarray, we will have the same number of good subarrays as the
        previous one. That's why we can add lo to the result if the current
        nums[hi] does not help reach k pairs.

        Basically, once we reach k or more pairs, we shrink lo in order to
        increase the number of good subarrays that we can take. Then we go
        through a period of waiting, during which each hi can command the same
        number of good subarrays as the last time when k or more pairs are found.

        O(N), 870 ms, faster than 29.42%
        """
        lo, hi = 0, 0
        num_pairs = 0
        counter = Counter()
        res = 0
        for hi in range(len(nums)):
            num_pairs += counter[nums[hi]]
            counter[nums[hi]] += 1
            if num_pairs >= k:
                while lo < hi and num_pairs >= k:
                    counter[nums[lo]] -= 1
                    num_pairs -= counter[nums[lo]]
                    lo += 1
            # if adding nums[hi] does not reach k pairs, then whatever
            # has worked previously must also work with the subarray
            # ending at nums[hi]
            res += lo
        return res


sol = Solution()
tests = [
    ([1,1,1,1,1], 10, 1),
    ([3,1,4,3,2,2,4], 2, 4),
    ([2,3,1,3,2,3,3,3,1,1,3,2,2,2], 18, 9),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.countGood(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
