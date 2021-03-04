# from pudb import set_trace; set_trace()
from typing import List
from operator import xor
from functools import reduce


class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        """LeetCode 268

        This is the same idea as yesterday when we were trying to come up
        with an O(1) space solution. We perform hopping whenever a number is NOT
        in its correct position. The slight trick is to set aside an additional
        value to record when the largest number is encountered.

        O(N), 144 ms, 37% ranking.
        """
        n_ = -1
        for i, n in enumerate(nums):
            if n != i:
                nums[i] = -1
                target = n
                while 0 <= target < len(nums) and target != nums[target]:
                    nums[target], target = target, nums[target]
                if target == len(nums):
                    n_ = target
        return len(nums) if n_ < 0 else nums.index(-1)


class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        """Let's try the flipping idea. The flipping idea also works, but we
        need to increment each value in nums by 1 to avoid the unflippable 0.

        O(N), 160 ms, 28% ranking.
        """
        N = len(nums)
        for i in range(N):
            nums[i] += 1  # avoid 0
        for n in nums:
            if abs(n) - 1 == abs(N):
                N *= -1
            else:
                nums[abs(n) - 1] *= -1
        if N > 0:
            return N
        for i, n in enumerate(nums):
            if n > 0:
                return i


class Solution3:
    def missingNumber(self, nums: List[int]) -> int:
        """Very brilliant. Use sum to identify the missing part.
        And we use the walrus operator again!!

        O(N), 120 ms, 96% ranking.
        """
        return (N := len(nums)) * (N + 1) // 2 - sum(nums)


class Solution4:
    def missingNumber(self, nums: List[int]) -> int:
        """This is a better way to do hopping, courtesy of myself more than two
        years ago. Apparently, I had a better understanding of hopping back
        then.
        """
        nums.append(-1)  # this is the only time that -1 is added
        for i in range(len(nums)):
            while nums[i] != i and nums[i] != -1:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return nums.index(-1)


class Solution5:
    def missingNumber(self, nums: List[int]) -> int:
        """This is the official XOR solution. The key is that XOR is both
        associative and commutative. That means we can XOR all the values along
        with their indices, and there will always be a way to group all correct
        value-index pairs. And since the XOR of the correct value-index pair
        results in zero, any value left is the missing number.

        And very cheekily, we write it in oneline
        """
        return reduce(xor, (i ^ n for i, n in enumerate(nums))) ^ len(nums)


sol = Solution5()
tests = [
    ([3, 0, 1], 2),
    ([0, 1], 2),
    ([1, 0], 2),
    ([0, 2], 1),
    ([2, 0], 1),
    ([1, 2], 0),
    ([2, 1], 0),
    ([0, 1], 2),
    ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ([0], 1),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.missingNumber(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
