# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """LeetCode 238

        We did this three days ago. So the same method is used. Two passes, with
        each pass computing cumulative product from start to end, and from end
        to start.

        O(N) time, O(1) extra space (not counting the return list).

        236 ms, 78% ranking.
        """
        N = len(nums)
        res = [1] * N
        for i in range(1, N):
            res[i] = res[i - 1] * nums[i - 1]
        p = 1
        for j in range(N - 2, -1, -1):
            p *= nums[j + 1]
            res[j] *= p
        return res


sol = Solution()
tests = [
    ([1,2,3,4], [24,12,8,6]),
    ([-1,1,0,-3,3], [0,0,9,0,0])
]

for i, (nums, ans) in enumerate(tests):
    res = sol.productExceptSelf(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
