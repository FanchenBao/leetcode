# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        """Easy question. Iterate through all elements in nums. If the element
        is 1, we compare its index with the previous 1's index to see whether
        there are sufficient number of zeros in between. If not, we return
        False. If no False has been returned during the iteration, we return
        True.

        O(N), 548 ms, 87% ranking.
        """
        pre_pos = -math.inf
        for i, n in enumerate(nums):
            if n == 1:
                if i - pre_pos - 1 < k:
                    return False
                pre_pos = i
        return True


class Solution2:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        """Bit manipulation. Much slower and not intuitive at all."""
        x = int(''.join(str(n) for n in nums), 2)
        # remove trailing zeros
        while x and x & 1 == 0:
            x >>= 1
        while x:
            x >>= 1  # remove trailing 1
            count = 0
            if not x:
                break
            while x & 1 == 0:  # remove trailing 0s and keep count
                x >>= 1
                count += 1
            if count < k:
                return False
        return True


sol = Solution2()
tests = [
    ([1, 0, 0, 0, 1, 0, 0, 1], 2, True),
    ([1, 0, 0, 1, 0, 1], 2, False),
    ([1, 1, 1, 1, 1], 0, True),
    ([0, 1, 0, 1], 1, True),
    ([0], 100, True),
    ([1], 100, True),
    ([1, 0, 1], 2, False),
    ([1, 0, 0, 0, 1, 0, 0, 1, 0], 2, True),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.kLengthApart(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
