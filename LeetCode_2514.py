# from pudb import set_trace; set_trace()
from typing import List, Tuple
import math
from collections import Counter


class Solution1:
    def __init__(self) -> None:
        self.memo = {}

    def count_uniq_perm(self, k: Tuple[int]) -> int:
        if len(k) == 1:
            return 1
        if sum(k) == len(k):
            return math.factorial(len(k))
        if k in self.memo:
            return self.memo[k]
        klst = list(k)
        res = 0
        for i in range(len(k)):
            klst[i] -= 1
            next_k = sorted(klst, reverse=True)
            while not next_k[-1]:
                next_k.pop()
            res += self.count_uniq_perm(tuple(next_k))
            klst[i] += 1
        self.memo[k] = res
        return res

    def countAnagrams(self, s: str) -> int:
        """TLE"""
        res = 1
        for word in s.split(' '):
            c = Counter(word)
            res *= self.count_uniq_perm(tuple(sorted(c.values(), reverse=True)))
        return res


class Solution2:
    def __init__(self) -> None:
        self.memo = {}

    def count_uniq_perm(self, k: Tuple[int]) -> int:
        if len(k) == 1:
            return 1
        if sum(k) == len(k):
            return math.factorial(len(k))
        if k not in self.memo:
            self.memo[k] = math.comb(sum(k[:-1]) + 1, k[-1]) * self.count_uniq_perm(k[:-1])
        return self.memo[k]

    def countAnagrams(self, s: str) -> int:
        """TLE"""
        res = 1
        for word in s.split(' '):
            c = Counter(word)
            res *= self.count_uniq_perm(tuple(sorted(c.values(), reverse=True)))
        return res


sol = Solution2()
tests = [
    # ("too hot", 18),
    # ("aa", 1),
    # ("aaab", 4),
    ("aabb", 6),
    # ("aaabb", 10),
]

for i, (s, ans) in enumerate(tests):
    res = sol.countAnagrams(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
