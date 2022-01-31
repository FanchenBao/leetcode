# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        left, right = 0, nums.count(1)
        score = left + right
        res = [0]
        for i in range(1, len(nums) + 1):
            if nums[i - 1] == 0:
                left += 1
            else:
                right -= 1
            if left + right > score:
                score = left + right
                res = [i]
            elif left + right == score:
                res.append(i)
        return res


# sol = Solution()
# tests = [
#     ([3,1,-2,-5,2,-4], [3,-2,1,-5,2,-4]),
#     ([-1,1], [1, -1]),
# ]

# for i, (nums, ans) in enumerate(tests):
#     res = sol.rearrangeArray(nums)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
