# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right, bisect_left


class Solution1:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """After sorting nums, we have the range for the second value. We allow
        the lower bound of the second value to be smaller than the current n,
        because that simply means the real lower bound of the value to take is
        the next to n. However, if the higher bound of the second value is
        smaller than the current n, that means we cannot find a proper second
        value. That is the signal to terminate the search.

        Also, pay attention to the use of bisect_right and bisect_left under
        different conditions.

        O(NlogN), 826 ms, faster than 78.53%
        """
        nums.sort()
        res = 0
        for i, n in enumerate(nums):
            lo, hi = lower - n, upper - n
            if hi < n:
                break
            q = bisect_right(nums, hi) - 1
            p = max(i + 1, bisect_left(nums, lo))
            res += q - p + 1
        return res


class Solution2:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """Two pointer solution from: https://leetcode.com/problems/count-the-number-of-fair-pairs/discuss/3174181/Two-Pointers-*-2

        Very genius. The idea is that we sort nums, and find the total number
        of pairs whose sum are smaller than upper. This includes all the pairs
        that are in between lower and upper, as well as all the pairs that are
        smaller equal to lower - 1. Thus, we use the same algo to find the total
        number of pairs smaller equal to lower - 1. The answer is the difference
        between the two.

        So good. This is just brilliant.

        O(NlogN), 713 ms, faster than 95.20%
        """
        nums.sort()

        def num_smaller_equal_to(upper_bound: int) -> int:
            lo, hi = 0, len(nums) - 1
            res = 0
            while lo < hi:
                while lo < hi and nums[lo] + nums[hi] > upper_bound:
                    hi -= 1
                res += hi - lo
                lo += 1
            return res

        return num_smaller_equal_to(upper) - num_smaller_equal_to(lower - 1)



sol = Solution2()
tests = [
    ([0,1,7,4,4,5], 3, 6, 6),
    ([1,7,9,2,5], 11, 11, 1),
    ([0,0,0,0,0,0], -1000000000, 1000000000, 15),
]

for i, (nums, lower, higher, ans) in enumerate(tests):
    res = sol.countFairPairs(nums, lower, higher)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
