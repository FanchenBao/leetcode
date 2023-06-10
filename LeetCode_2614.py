# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def is_prime(self, n: int) -> bool:
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def diagonalPrime(self, nums: List[List[int]]) -> int:
        """The more tricky part is to write a simple function to check for
        primes.

        722 ms, faster than 98.19% 
        """
        diags = []
        N = len(nums)
        for i in range(N):
            diags.append(nums[i][i])
            diags.append(nums[i][N - i - 1])
        diags.sort(reverse=True)
        for d in diags:
            if self.is_prime(d):
                return d
        return 0
        

# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
