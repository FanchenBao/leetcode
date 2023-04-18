# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def factor(self, n: int, primes: List[int]) -> Counter:
        res = Counter()
        i = 0
        while n > 1:
            while n % primes[i] == 0:
                res[primes[i]] += 1
                n //= primes[i]
            i += 1
        return res

    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        counts = [self.factor(n, primes) for n in nums]
        num_square_subs = 0
        for i, count in enumerate(counts):
            if any(v > 1 for v in count.values()):
                # the current number has square factor
                num_square_subs = (num_square_subs + 2**i) % MOD
            else:
                num_can_pair = 0
                for j in range(i):
                    for k in count.keys():
                        if k in counts[j]:
                            num_can_pair += 1
                            break
                num_square_subs = (2 * num_square_subs + (2**num_can_pair - 1) * (2**(i - num_can_pair) - 1)) % MOD
            # print(i, num_square_subs)
        return (2**(len(nums)) - 1 - num_square_subs) % MOD


sol = Solution()
tests = [
    # ([3,4,4,5], 3),
    # ([1], 1),
    ([5,6,4,3,4], 5),
    # ([5,6,4,3,4,5,6,7,7,8,9,10,11,12,12,12,12,30,30,6,5,6,5], 203),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.squareFreeSubsets(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
