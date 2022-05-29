# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        """LeetCode 268

        This is O(1) in space and O(N) in time. But it's kinda slow.

        250 ms, faster than 25.89%
        """
        nums.append(-1)
        for i in range(len(nums)):
            j = i
            while nums[j] >= 0 and j != nums[j]:
                temp = nums[nums[j]]
                nums[nums[j]] = nums[j]
                nums[j] = temp
        for i in range(len(nums)):
            if nums[i] < 0:
                return i


class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        """Use sum
        """
        return (N := len(nums)) * (N + 1) // 2 - sum(nums)
 

class Solution3:
    def missingNumber(self, nums: List[int]) -> int:
        """XOR. We can XOR everything, and the one left is the missing number.
        """
        res = len(nums)
        for i, n in enumerate(nums):
            res ^= (i ^ n)
        return res
 




sol = Solution3()
tests = [
    ([3,0,1], 2),
    ([0, 1], 2),
    ([9,6,4,2,3,5,7,0,1], 8),
] 

for i, (nums, ans) in enumerate(tests):
    res = sol.missingNumber(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
