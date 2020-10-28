# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """39% ranking"""
        if not nums:
            return []
        start = nums[0]
        ranges = []
        for i, n in enumerate(nums[1:], 1):
            if n - nums[i - 1] > 1:
                ranges.append(
                    [start, nums[i - 1]] if start < nums[i - 1] else [start],
                )
                start = n
        ranges.append([start, nums[-1]] if start < nums[-1] else [start])
        return ['->'.join([str(r) for r in ran]) for ran in ranges]


sol = Solution()
tests = [
    ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
    ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
    ([], []),
    ([-1], ['-1']),
    ([0], ['0']),
    ([1, 5], ['1', '5'])
]

for i, (nums, ans) in enumerate(tests):
    res = sol.summaryRanges(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
