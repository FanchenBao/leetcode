# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        LeetCode 645

        O(N) time and O(N) space. 146 ms, faster than 96.81% 
        """
        N = len(nums)
        arr = [-1] * (N + 1)
        res = [0, 0]
        for n in nums:
            if arr[n] > 0:
                res[0] = n
            arr[n] = 1
        for i in range(1, N + 1):
            if arr[i] < 0:
                res[1] = i
                break
        return res


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        LeetCode 645

        O(NlogN) time and O(1) space. 159 ms, faster than 80.43%
        """
        nums.sort()
        res = [0, 0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 0:
                res[0] = nums[i]
            elif nums[i] - nums[i - 1] > 1:
                res[1] = nums[i] - 1
        # check whether the missing is at the beginning or end
        if res[1] == 0:
            res[1] = 1 if nums[0] != 1 else len(nums)
        return res
 


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
