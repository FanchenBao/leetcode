# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution:
    @lru_cache
    def fib(self, n: int) -> int:
        """LeetCode 509

        51 ms, faster than 52.11%
        """
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2) 
        

# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
