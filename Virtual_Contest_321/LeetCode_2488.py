# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """This is O(N^2). No wonder it TLE.
        """
        psmall = [0]
        for n in nums:
            if n < k:
                psmall.append(psmall[-1] + 1)
            else:
                psmall.append(psmall[-1])
        idx = nums.index(k)
        N = len(nums)
        res = 1
        for l in range(2, N + 1):
            tgt = (l - 1) // 2
            left, right = max(idx - (l - 1), 0), min(idx + (l - 1), N - 1)
            if psmall[right + 1] - psmall[left] < tgt:
                continue
            for i in range(left, right - l + 2):
                res += int(psmall[i + l] - psmall[i] == tgt)
        return res


sol = Solution()
tests = [
    ([3,2,1,4,5], 4, 3),
    ([2,3,1], 3, 1),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.countSubarrays(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
