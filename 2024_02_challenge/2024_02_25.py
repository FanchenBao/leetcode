# from pudb import set_trace; set_trace()
from typing import List
import math


class DSU:
    def __init__(self, n: int) -> None:
        self.par = list(range(n))
        self.cnt = [1] * n  # the number of elements in each group

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> None:
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.cnt[px] >= self.cnt[py]:
            self.par[py] = px
            self.cnt[px] += self.cnt[py]
        else:
            self.par[px] = py
            self.cnt[py] += self.cnt[px]


class Solution:
    def factor(self, n: int) -> List[int]:
        res: List[int] = []
        while n and n % 2 == 0:
            if not res or res[-1] != 2:
                res.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            while n and n % f == 0:
                if not res or res[-1] != f:
                    res.append(f)
                n //= f
            f += 2
        if n != 1:
            res.append(n)
        return res

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        """
        LeetCode 2709

        Factor each number to find its prime factors. And then use
        Union Find to decide whether all the numbers in nums can form
        a connected graph.

        The slowest part of the algo is the factor function. We can speed it
        significantly if we hardcode all the prime numbers smaller or equal
        to 316 (316 because it is the biggest number whose square is not
        bigger than the max possible value in nums). This list is not that
        big. With the prime list, factor can run much much faster. From my
        own solution six months ago, with a list of prime numbers, the run
        time is more than twice as fast as today's solution.

        Update: use count to obtain the number of elements in each group in
        DSU.

        3204 ms, faster than 62.50%
        """
        dsu = DSU(len(nums) + 1)
        seeds = {}
        for i, n in enumerate(nums):
            for f in self.factor(n):
                if f not in seeds:
                    seeds[f] = i
                else:
                    dsu.union(seeds[f], i)
        return dsu.cnt[dsu.find(0)] == len(nums)


sol = Solution()
tests = [
    ([2, 3, 6], True),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.canTraverseAllPairs(nums)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
