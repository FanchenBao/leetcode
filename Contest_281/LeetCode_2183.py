# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter
import math


class Solution1:
    def countPairs(self, nums: List[int], k: int) -> int:
        counter = Counter()
        kcount = 0
        for n in nums:
            gcd = math.gcd(n, k)
            if gcd == k:
                kcount += 1
            elif gcd != 1:
                counter[gcd] += 1
        res = 0
        div_list, N = sorted(counter), len(counter)
        for i, d in enumerate(div_list):
            if (d * d) % k == 0:
                res += counter[d] * (counter[d] - 1) // 2
            for j in range(i + 1, N):
                if (d * div_list[j]) % k == 0:
                    res += counter[d] * counter[div_list[j]]
        return res + kcount * (len(nums) - kcount) + kcount * (kcount - 1) // 2


class Solution2:
    def countPairs(self, nums: List[int], k: int) -> int:
        """Same GCD idea but less verbose.

        Ref: https://leetcode.com/problems/count-array-pairs-divisible-by-k/discuss/1784721/Count-GCDs
        """
        counter = Counter()
        res = 0
        for n in nums:
            g1 = math.gcd(n, k)
            for g2, cnt in counter.items():
                res += 0 if g1 * g2 % k else cnt
            counter[g1] += 1
        return res


sol = Solution2()
tests = [
    ([1, 2, 3, 4, 5], 2, 7),
    ([1, 2, 3, 4], 5, 0),
    ([8,10,2,5,9,6,3,8,2], 6, 18),
    ([100,17,3,77,64,74,11,43,10,37], 20, 11),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.coutPairs(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
