# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """LeetCode 228.

        Forgot about two edge cases where nums = [] or [1]. That caused me two
        errors. How can I be this callous?!

        O(N), 49 ms, 34% ranking.
        """
        N = len(nums)
        if not N:
            return []
        res = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                res[-1] = f'{res[-1]}->{nums[i - 1]}' if nums[i - 1] != res[-1] else str(res[-1])
                res.append(nums[i])
        res[-1] = f'{res[-1]}->{nums[N - 1]}' if nums[N - 1] != res[-1] else str(res[-1])
        return res


sol = Solution()
tests = [
    ([0,1,2,4,5,7], ["0->2","4->5","7"]),
    ([0,2,3,4,6,8,9], ["0","2->4","6","8->9"]),
    ([], []),
    ([-1], ['-1']),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.summaryRanges(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
