# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """LeetCode 1695

        The technique is the same as the problems in the previous days. We use
        a dict to record the indices of the last occurrences of each number.
        And we use a prefix sum to quickly compute the sum of any subarray.
        Each time a new number is encountered, we check whether its last
        occurrence happens within or outside the longest unique subarray ending
        in the number to the left of the current number. If it is outside, we
        can add the current number to the longest unique subarray of the number
        to the left. Otherwise, we have to re-compute the range which cannot
        include the last occurrence of the current number.

        O(N), 1872 ms, faster than 45.74%
        """
        presum = [0]
        indices = {}
        res, pre_ext_idx = 0, 1
        for i, n in enumerate(nums, 1):
            presum.append(presum[-1] + n)
            if indices.get(n, -1) >= pre_ext_idx:
                pre_ext_idx = indices.get(n, -1) + 1
            res = max(res, presum[i] - presum[pre_ext_idx - 1])
            indices[n] = i
        return res


sol = Solution()
tests = [
    ([4,2,4,5,6], 17),
    ([5,2,1,2,5,2,1,2,5], 8),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.maximumUniqueSubarray(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
