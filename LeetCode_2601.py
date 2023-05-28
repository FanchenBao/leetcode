# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_left


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        """Not very difficult, but I still had to go through a few test cases to
        fix some edge cases.

        O(NlogN), 115 ms, faster than 86.38% 
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
        pre = 0
        for n in nums:
            if n <= pre:
                return False
            if n - pre <= 2:
                pre = n
                continue
            idx = bisect_left(primes, n - pre) - 1
            pre = n - primes[idx]
        return True


sol = Solution()
tests = [
    ([4,9,6,10], True),
    ([6,8,11,12], True),
    ([5,8,3], False),
    ([1,1,1], False),
    ([9,8,7,6,5], False),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.primeSubOperation(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
