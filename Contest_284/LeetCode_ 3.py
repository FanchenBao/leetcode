# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        N = len(nums)
        if k == 0:
            return nums[0]
        elif k == 1:
            if N == k:
                return -1
            return nums[1]
        else:
            if N < k:
                if N == 1:
                    return -1 if k % 2 else nums[0]
                return max(nums)
            elif N == k:
                return max(nums[:k - 1])
            return max(max(nums[:k - 1]), nums[k])
        
        
sol = Solution()
tests = [
    ([5,2,2,4,0,6], 4, 5),
    ([2], 1, -1),
    ([18], 3, -1),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.maximumTop(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
