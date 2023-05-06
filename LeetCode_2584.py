# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def __init__(self) -> None:
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    
    def factor(self, n: int) -> Counter:
        primes = Counter()
        lim = int(math.sqrt(n)) + 1
        for p in self.primes:
            if n == 1 or p >= lim:
                break
            while n % p == 0:
                primes[p] += 1
                n //= p
        if n > 1:
            primes[n] += 1
        return primes

    def findValidSplit(self, nums: List[int]) -> int:
        """Holly guacamole! To speed up the factoring, I use a little cheat
        by setting the primes from 1 to 1000 as default values. Then factoring
        can happen directly on primes, and terminated immediately when the
        prime to be factored is larger than sqrt of the number.

        After that, we find the key_primes that make the pre and suf not
        co-prime. Each time a new number if removed from the suf, if the prime
        factors in the removed value still exists in suf, we add that prime
        factor to key_primes. If there is no more such prime factor in suf,
        we remove it from the key_primes.

        pre and suf becomes co-prime the first time when key_primes is empty
        the first time.

        O(NlogM), where M is the average value in nums.
        9215 ms, faster than 5.04%
        """
        if len(nums) == 1:
            return -1
        suf = Counter()
        factored_nums = [self.factor(n) for n in nums]
        for i in range(1, len(nums)):
            suf += factored_nums[i]
        key_primes = set()
        for k in factored_nums[0]:
            if k in suf:
                key_primes.add(k)
        if not key_primes:
            return 0
        for i in range(1, len(nums) - 1):
            for k, v in factored_nums[i].items():
                suf[k] -= v
                if suf[k]:
                    key_primes.add(k)
                else:
                    if k in key_primes:
                        key_primes.remove(k)
                    del suf[k]
            if not key_primes:
                return i
        return -1
        

sol = Solution()
tests = [
    ([4,7,8,15,3,5], 2),
    ([4,7,15,8,3,5], -1),
    ([158771,826499,157247,751291,968761,707717,150707,158771,470411,306167,87407,656923,324637,869927,707717,409081,434141,950329,878833,43451,585041,611707,954181,217901,58049,693733,662591,504593,244753,16901,332477,721381,499519,691763,365933,789731,243781,968761,721381,434141,84809,826171,519703,687179,587149,923603,530063,386521,167119,896803,358829,268501,740011,23899,143177,664151,169069,133853,41051,209659,260543,811651,767309,960593,817979,97007,183397,822299,501931,993241,772181,249497,706883,423847,692779,91499,804127,561839,462607,516947,74933,912809,343933,840821,892357,474503,439613,861871,291521,291521,780343,291521,223243,281159,780343], 39),
    ([1], -1),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findValidSplit(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
