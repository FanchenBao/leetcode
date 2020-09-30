# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """First try the O(nlog(n)) solution
        
        First sort the nums, then find the first smallest
        positive integer. If the smallest positive integer
        is larger than 1, then return 1; else we follow
        through the increments until we find the missing positive integer. 
        """
        # remove negatives
        pos_nums = sorted([n for n in nums if n > 0])
        if not pos_nums or pos_nums[0] > 1:
            return 1
        pre = 0
        for n in pos_nums:
            if n - pre > 1:
                return pre + 1
            pre = n
        return pos_nums[-1] + 1


class Solution2:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """We can create an array of buckets and put values of nums in it. e.g.
        value 2 in nums will be placed in buckets[2], value 4 in buckets[4]. If
        a num in nums is negative or larger than the size of nums, we ignore it
        Eventually, we check the bucket and see which position has not been
        filled. That position will be the smallest postive integer.  
        """
        size = len(nums)
        buckets = [-1] * (size + 1)
        for n in nums:
            if 0 < n <= size:
                buckets[n] = n
        for i in range(1, size + 1):
            if buckets[i] < 0:
                return i
        return size + 1





sol = Solution2()
tests = [
    ([1, 2, 0], 3),
    ([3, 4, -1, 1], 2),
    ([7, 8, 9, 11, 12], 1),
    ([], 1),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.firstMissingPositive(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
