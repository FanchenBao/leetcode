# from pudb import set_trace; set_trace()
from typing import List
import math

class DSU:
    def __init__(self, N: int) -> None:
        self.par = list(range(N))
        self.cnt = [1] * N  # number of elements in each group

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.cnt[px] >= self.cnt[py]:
                self.par[py] = px
                self.cnt[px] += self.cnt[py]
            else:
                self.par[px] = py
                self.cnt[py] += self.cnt[px]
            return True
        return False


class Solution:
    def __init__(self) -> None:
        self.primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,307, 311, 313}
    
    def factor(self, n: int) -> List[int]:
        if n in self.primes:
            return [n]
        res = []
        for p in self.primes:
            has_p = False
            while n > 1 and n % p == 0:
                has_p = True
                n //= p
            if has_p:
                res.append(p)
            if n <= 1:
                break
        if n > 1:
            res.append(n)
        return res

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        """Feels like cheating, because we simply pulled down all the primes
        smaller than 316, and use that to factor each number in nums. Once we
        do that, we use union find to group all the indices that share at least
        one prime factors.
        
        There are a bunch of edge cases. First of all, if the size of nums is
        one, the problem defauls the answer to True.

        If 1 exists in nums, it is not possible to connect with it..

        We shall always remove the duplicates.

        O(N * O(Union-Find)), 948 ms, faster than 86.82%

        UPDATE: use count of the size of each group, instead of ranking, to
        implement Union-Find. This way, we can immediately obtain the size of
        the final connected graph. Courtesy of: https://leetcode.com/problems/greatest-common-divisor-traversal/discuss/3568567/Union-Find-in-C%2B%2B-Java-and-Python

        898 ms, faster than 87.98%
        """
        if len(nums) == 1:
            return True
        uniq_nums = set(nums)
        if 1 in uniq_nums:
            return False
        factor_dict = {}
        dsu = DSU(len(uniq_nums))
        for i, n in enumerate(uniq_nums):
            for f in self.factor(n):
                if f not in factor_dict:
                    factor_dict[f] = i
                else:
                    dsu.union(factor_dict[f], i)
        return dsu.cnt[dsu.find(0)] == len(uniq_nums)

        

sol = Solution()
tests = [
    ([2,3,6], True),
    ([3,9,5], False),
    ([4,3,12,8], True),
    ([10007, 20014], True),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.canTraverseAllPairs(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
