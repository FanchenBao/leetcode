# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter
from bisect import bisect_left


class Solution1:
    def specialArray(self, nums: List[int]) -> int:
        """A generalized solution"""
        counter = Counter(nums)
        res = 0
        for n in sorted(counter.keys(), reverse=True):
            if res > n:
                return res
            else:
                res += counter[n]
                if res > n:
                    return -1
        return res


class Solution2:
    def specialArray(self, nums: List[int]) -> int:
        """A hack solution"""
        nums.sort()
        for n in range(1000):
            if len(nums) - bisect_left(nums, n) == n:
                return n
        return -1


class Solution3:
    def specialArray(self, nums: List[int]) -> int:
        """Standard solution.
        
        For each while loop, we are ceterin that there are i numbers that are
        larger than or equal to i. If nums[i] == i, then we will have i + 1
        numbers that are larger than or equal to i, which violates the special
        array requirement. 
        """
        nums.sort(reverse=True)
        i = 0
        while i < len(nums) and nums[i] > i:
            i += 1
        return -1 if i < len(nums) and nums[i] == i else i


class Solution4:
    def specialArray(self, nums: List[int]) -> int:
        """Binary search"""
        nums.sort(reverse=True)
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if mid < nums[mid]:
                left = mid + 1
            else:
                right = mid
        return -1 if left < len(nums) and nums[left] == left else left



sol = Solution4() 
tests = [
    ([3, 5], 2),
    ([0, 0], -1),
    ([0, 4, 3, 0, 4], 3),
    ([3, 6, 7, 7, 0], -1),
    ([2, 2], 2),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.specialArray(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
