# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        i = j = 0
        N = len(nums)
        while i < N or j < N:
            if i == j:
                j += 1
            while j < N and j - i < k:
                if nums[j] < nums[j - 1]:
                    return False
                j += 1
            left = nums[i]
            while i < j and nums[i] == left:
                nums[i] -= left
                i += 1
            nums[j - 1] -= left
            if i < j - 1:
                nums[i] -= left 
            print(nums, j)
        return True
                


sol = Solution()
tests = [
    ([60,72,87,89,63,52,64,62,31,37,57,83,98,94,92,77,94,91,87,100,91,91,50,26], 4, True),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.checkArray(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
