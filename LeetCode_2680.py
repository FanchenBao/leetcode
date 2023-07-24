# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        """For each value we must commit all the doubling, because
        splitting up the doubling on separate numbers is useless.
        
        Doubling allows us to add one more digit to the left in the
        binary value. Splitting up the doubling would always yield
        values with fewer binary digits. Thus, for each value, we have
        to double all the way down.

        Therefore, we simply choose each big value, double it to the end, and
        find the OR. Choose the largest among them.

        Implementation-wise, we use prefix and suffix OR to find the OR of the
        values ahead of and behind the current value of interest.

        O(N), 775 ms, faster than 78.37%
        """
        preor = [0]
        for i in range(len(nums) - 1):
            preor.append(preor[-1] | nums[i])
        sufor = 0
        res = 0
        for j in range(len(nums) - 1, -1, -1):
            res = max(res, preor[-1] | (nums[j] * (1 << k)) | sufor)
            preor.pop()
            sufor |= nums[j]
        return res
        

sol = Solution()
tests = [
    ([12,9], 1, 30),
    ([8,1,2], 2, 35),
    ([6,9,8], 1, 31),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.maximumOr(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
