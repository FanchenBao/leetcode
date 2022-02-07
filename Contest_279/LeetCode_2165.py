# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            return -int(''.join(sorted(str(-num), reverse=True)))
        digits = sorted(str(num))
        for i in range(len(digits)):
            if digits[i] != '0':
                break
        digits[i], digits[0] = digits[0], digits[i]
        return int(''.join(digits))


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
