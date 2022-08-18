# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        """
        Greedy. The optimal position for any number is to be grouped with the
        number immediately to its left or immediately to its right. Thus, we
        sort the orignal numbers, and then compute the difference of each
        consecutive parts of the sorted nums. Once the overall diff of a part
        exceeds k, that part can be detached, and we start over.
        
        O(N), 1367 ms, faster than 59.62%
        """
        nums.sort()
        res, c = 0, 0
        for i in range(1, len(nums)):
            c += nums[i] - nums[i - 1]
            if c > k:
                res += 1
                c = 0
        return res + 1


sol = Solution()
tests = [
    ([3,6,1,2,5], 2, 2),
    ([1,2,3], 1, 2),
    ([2,2,4,5], 0, 3),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.partitionArray(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
