# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        """LeetCode 137

        Go through the entire nums and count the number of 1s at each position.
        The count mod 3 is the bit of the position of the single value.

        O(N) time and O(1) space. 182 ms, faster than 23.03%
        """
        mask = (1 << 32) - 1
        counts = [0] * 32
        for n in nums:
            if n < 0:
                b = bin(~(n ^ mask))[2:]
            else:
                b = f'{n:032b}'
            for i in range(32):
                counts[i] += int(b[i] == '1')
        res = sum(1 << (32 - i - 1) for i in range(32) if counts[i] % 3)
        return res - mask - 1 if (1 << 31) & res else res


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        """We can MOD 3 while counting, which probably can make things faster
        """
        mask = (1 << 32) - 1
        counts = [0] * 32
        for n in nums:
            if n < 0:
                b = bin(~(n ^ mask))[2:]
            else:
                b = f'{n:032b}'
            for i in range(32):
                counts[i] = (counts[i] + int(b[i] == '1')) % 3
        res = sum(1 << (32 - i - 1) for i in range(32) if counts[i])
        return res - mask - 1 if (1 << 31) & res else res


sol = Solution2()
tests = [
    ([2,2,3,2], 3),
    ([0,1,0,1,0,1,99], 99),
    ([-2,-2,-2,-1,-3,-3,-3], -1),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.singleNumber(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
