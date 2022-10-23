# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution1:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """LeetCode 645

        This is a stupid solution.

        O(N), 467 ms, faster than 43.23% 
        """
        counter = Counter(nums)
        missing, double = 0, 0
        for i in range(len(nums)):
            if counter[nums[i]] == 2:
                double = nums[i]
            if i + 1 not in counter:
                missing = i + 1
            if missing * double > 0:
                return [double, missing]


class Solution2:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """O(N) time and O(1) space

        From the official solution. We jump using the values of each number.
        The jump is achieved by inversing the value at nums[nums[i]].

        If the jump leads us to a value already negative, that means the
        current number must be duplicated.

        After all the jumps, we go through the nums again and the index
        pointing to the only positive value is the missing number.
        """
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                double = abs(nums[i])
            else:
                nums[abs(nums[i]) - 1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                return [double, i + 1]


class Solution3:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """O(NlogN) time and O(1) space

        Use sort
        """
        nums.sort()
        double = missing = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                double = nums[i]
            elif nums[i] - nums[i - 1] > 1:
                missing = nums[i] - 1
            if missing * double != 0:
                return [double, missing]
        return [double, 1] if nums[0] != 1 else [double, len(nums)]


sol = Solution3()
tests = [
    ([1,2,2,4], [2, 3]),
    ([1, 1], [1, 2]),
    ([4, 2, 4, 1], [4, 3]),
    ([3,2,3,4,6,5], [3, 1]),
    ([1,5,3,2,2,7,6,4,8,9], [2, 10]),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findErrorNums(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
