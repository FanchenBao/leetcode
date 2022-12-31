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
    def countAnagrams(self, s: str) -> int:
        """I did check the hints, but they are useless. I also opened the forum
        and checked the titles, but the only additional hint is that the solution
        is math-based, which I kind of knew already. Then it hit me.

        Given "aaabb", we have five spots to place 'a' uniquely. There are 5C3
        number of ways to do so. Once all 'a's are settled, we can fill 'b's
        in the remaining two empty spots. There is 2C2 number of ways to do so.
        Thus, overall, the number of unique permutation of "aaabb" is 5C3 * 2C2
        = 10.

        Given "aaaabbbcc", the number of unique permutation is 9C4 * 5C3 * 2C2.

        Thus, the rule is that for each repeated letter, we find the count of
        the currently available spots. Say there are r count of repeated letter
        and n count of available spots, we multiply nCr. Then we go for the
        next repeated letter and continue with the multiplication.

        Once the count of unique perm is found for each word, the final result
        is just to multiply all the counts.

        We can use modular multiplication to avoid large numbers. So the only
        benefit Python has is the built-in `math.comb`.

        340 ms, faster than 92.91% 
        """
        res = 1
        MOD = 10**9 + 7
        for word in s.split(' '):
            uniq_perm = 1
            n = len(word)
            for c in Counter(word).values():
                uniq_perm = (uniq_perm * (math.comb(n, c) % MOD)) % MOD
                n -= c
            res = (res * (uniq_perm % MOD)) % MOD
        return res


sol = Solution2()
tests = [
    ("too hot", 18),
    ("aa", 1),
    ("aaab", 4),
    ("aabb", 6),
    ("aaabb", 10),
    ('aaaabbbcc', 1260),
]

for i, (s, ans) in enumerate(tests):
    res = sol.countAnagrams(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
