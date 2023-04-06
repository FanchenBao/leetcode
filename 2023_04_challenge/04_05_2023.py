# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate


class Solution1:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        """LeetCode 2439

        Use binary search. We search for the smallest max value possible for
        nums. We start with some hypothetical max value. Then we go through nums
        and apply the rules to see if it is possible to get all the values
        smaller or equal to the target max value.

        We go from right to left. For each value that is larger than mid, we
        decrease it to mid and increase its previous value by the difference.
        Then we move on to the previous one and repeat the same procedure. If
        we can go through the entire nums without any value breaching mid, this
        mid works. So we need to seek a smaller version. Otherwise, mid does
        not work and we need to make it bigger.

        O(NlogM), where N = len(nums) and M is max(nums) - min(nums)

        2251 ms, faster than 10.32%
        """
        lo, hi = min(nums) - 1, max(nums) + 1
        N = len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[0] > mid:
                lo = mid + 1
                continue
            diff = 0
            for i in range(N - 1, -1, -1):
                cur = nums[i] + diff
                diff = max(0, cur - mid)
            if diff == 0:
                hi = mid
            else:
                lo = mid + 1
        return lo


class Solution2:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        """This is from the official solution. Think about it this way. Say
        we have nums = [3, 7]. The answer is (3 + 7) // 2, because we can always
        average them out.

        However, if nums = [7, 3], we cannot average because the extra value can
        only go from right to left. In this case, the answer is 7.

        Say we have solved nums[:k] with min max value p. Now consider nums[k].
        If nums[k] <= p, there is no need to make any change. If nums[k] > p,
        then we can re-average the whole thing. Thus, we also need to take
        prefix sum.

        O(N) 765 ms, faster than 88.79% 
        """
        return max(math.ceil(s / (i + 1)) for i, s in enumerate(accumulate(nums)))


sol = Solution2()
tests = [
    ([3,7,1,6], 5),
    ([10,1], 10),
    ([34,534,5,778654,5,67], 194807),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.minimizeArrayValue(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
