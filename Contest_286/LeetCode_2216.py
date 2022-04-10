# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        stack = []
        iseven = True
        for n in nums:
            if iseven:
                stack.append(n)
                iseven = False
            elif n != stack[-1]:
                stack.append(n)
                iseven = True
        if len(stack) % 2:
            stack.pop()
        return len(nums) - len(stack)


sol = Solution()
tests = [
    ([1,1,2,3,5], 1),
    ([1,1,2,2,3,3], 2),
    ([1,2,3,3,4,4,5,5,6], 1),
    ([1], 1),
    ([], 0),
    ([1,1,1,1,1], 5),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.minDeletion(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
