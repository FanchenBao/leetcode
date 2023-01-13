# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """Just use counter

        O(N), 878 ms, faster than 77.35%
        """
        cur_sum = sum(nums[:k])
        counter = Counter(nums[:k])
        res = cur_sum if len(counter) == k else 0
        for i in range(k, len(nums)):
            counter[nums[i - k]] -= 1
            if not counter[nums[i - k]]:
                del counter[nums[i - k]]
            counter[nums[i]] += 1
            cur_sum += nums[i] - nums[i - k]
            if len(counter) == k:
                res = max(res, cur_sum)
        return res


sol = Solution()
tests = [
    ([1,5,4,2,9,9,9], 3, 15),
    ([4,4,4], 3, 0),
    ([1,1,1,7,8,9], 3, 24),
    ([9,9,9,1,2,3], 3, 12),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.maximumSubarraySum(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
