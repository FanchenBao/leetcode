# from pudb import set_trace; set_trace()
from typing import List
from itertools import groupby


class Solution1:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """LeetCode 485

        Easy problem. Just iterate through and keep counting the consecutive
        ones.

        O(N), 372 ms, 42% ranking.
        """
        res, temp = 0, 0
        for i, n in enumerate(nums):
            if n == 1:
                if i == 0 or nums[i - 1] == 1:
                    temp += 1
                else:
                    res = max(res, temp)
                    temp = 1
        return max(res, temp)


class Solution2:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """Use grouby. The edge case is groupby part returns an empty array.

        O(N), 328 ms, 99% ranking.
        """
        return max([len(list(g)) for k, g in groupby(nums) if k == 1] or [0])


sol = Solution2()
tests = [
    ([1, 1, 0, 1, 1, 1], 3),
    ([1, 0, 1, 1, 0, 1], 2),
    ([0], 0),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findMaxConsecutiveOnes(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
