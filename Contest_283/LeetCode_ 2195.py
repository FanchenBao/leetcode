# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(set(nums))
        res, pre = 0, 0
        for n in nums:
            inbetween = n - pre - 1
            if inbetween <= k:
                res += (n - 1 + pre + 1) * inbetween // 2
                k -= inbetween
                pre = n
            else:
                res += (pre + 1 + pre + k) * k // 2
                k = 0
                break
        if k:
            res += (nums[-1] + 1 + nums[-1] + k) * k // 2
        return res

        

sol = Solution()
tests = [
    ([96,44,99,25,61,84,88,18,19,33,60,86,52,19,32,47,35,50,94,17,29,98,22,21,72,100,40,84], 35, 794),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.minimalKSum(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
