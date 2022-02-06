# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even, odd = [], []
        for i, n in enumerate(nums):
            if i % 2:
                odd.append(n)
            else:
                even.append(n)
        even.sort(reverse=True)
        odd.sort()
        for i in range(len(nums)):
            if i % 2:
                nums[i] = odd.pop()
            else:
                nums[i] = even.pop()
        return nums
        
        



# sol = Solution()
# tests = [
#     (9, 6),
#     (2, 2),
#     (9, 6),
#     (20, 6),
#     (21, 6),
#     (22, 8),
#     (23, 8),
#     (100, 54),
# ]

# for i, (n, ans) in enumerate(tests):
#     res = sol.lastRemaining(n)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
