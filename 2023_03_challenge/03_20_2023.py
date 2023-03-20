# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """LeetCode 605

        This is not really greedy. Given the number of empty spots between two
        flowers are k, we can plant at most (k - 1) // 2 flowers. Thus, we just
        need to find all the indices of the flowers and find the max number of
        flowers possible to plant in between.

        The trick is to set the imaginary first flower position at -2, because
        in the situation of [0,0,0,0,1], we can place a flower at the first
        spot, which means the imaginary first flower should be at -2.

        Another trick is set the imaginary last flower at position
        len(flowerbed) + 1 to handle situations such as [1,0,0,0,0].

        O(N), 159 ms, faster than 89.08%
        """
        pre = -2
        max_flowers = 0
        for i, f in enumerate(flowerbed):
            if f:
                max_flowers += (i - pre - 2) // 2
                pre = i
        max_flowers += (len(flowerbed) - pre - 1) // 2  # the suffix zeros
        return max_flowers >= n


sol = Solution()
tests = [
    ([1,0,0,0,1], 1, True),
    ([1,0,0,0,1], 2, False),
    ([1,0,0,0,1,0,0], 2, True),
]

for i, (flowerbed, n, ans) in enumerate(tests):
    res = sol.canPlaceFlowers(flowerbed, n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
