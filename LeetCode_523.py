# from pudb import set_trace; set_trace()
from typing import List
from itertools import accumulate
from collections import Counter


class Solution1:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """One of the worst case of trial and error in all of my journey with
        LeetCode. The number of edge cases is through the roof and really
        frustrated me. The problem is with two things. One is the existence of
        0, and the other is the case where a single number can be divided by k.
        Eventually, I settled for the prefix sum solution. I check from back
        to front, for each prefix sum, whether it plus a multiple of k exists
        in the set of prefix sum, AND to assure that if such a value exists, it
        does not occupy the position right after the current prefix sum. Also
        the last two prefix sums, if exist, must be evaluated on their own.

        O(N * max*(nums) / k), 1674 ms, 10% ranking.
        """
        if len(nums) == 1:
            return False
        presum = list(accumulate(nums))
        presumset = set(presum)
        if (presum[-1] % k) * (presum[-2] % k) == 0:
            return True
        for i in range(len(presum) - 3, -1, -1):
            if i > 0 and presum[i] % k == 0:
                return True
            kp = 0
            while presum[i] + kp <= presum[-1]:
                if presum[i] + kp in presumset and presum[i + 2] <= presum[i] + kp:
                    return True
                kp += k
        return False


class Solution2:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """The trick is with the MOD!!

        Ref: https://leetcode.com/problems/continuous-subarray-sum/discuss/99499/Java-O(n)-time-O(k)-space

        The referenced solution has the same idea, but it solves the problem of
        how many ks to check in O(1) time. We simply mod each prefix sum. Note
        that what we want is that given the current prefix sum, we want to know
        whether there exists a previous prefix sum such that sum_cur - sum_pre
        is a multiple of k. This is equivalent to say (sum_cur - sum_pre) % k =
        0, which is equivalent to sum_cur % k - sum_pre % k == 0. Thus, if we
        keep track of the remainder of each prefix sum divided by k, we can
        avoid the problem of having to find how many ks to deduct (or add).

        Then the other thing to keep in mind is to avoid a match that is right
        behind (or in front of) the current value.

        O(N), 904 ms, 82% ranking.
        """
        presum = 0
        hashmap = {0: -1}
        for i, n in enumerate(nums):
            presum = (presum + n) % k  # this is where the magic happens
            if i > hashmap.get(presum, i) + 1:
                return True
            hashmap[presum] = min(hashmap.get(presum, i), i)
        return False


sol = Solution2()
tests = [
    ([23,2,4,6,7], 6, True),
    ([23,2,6,4,7], 6, True),
    ([23,2,6,4,7], 13, False),
    ([5,0,0,0], 3, True),
    ([0], 1, False),
    ([1, 0], 2, False),
    ([1,2,12], 6, False),
    ([1,0,1,0,1], 4, False),
    ([0,1,0],1, True),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.checkSubarraySum(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
