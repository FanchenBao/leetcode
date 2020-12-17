# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter, defaultdict


class Solution1:
    def two_sums(self, counterA, counterB) -> Counter:
        res_counter = defaultdict(int)
        for ka, va in counterA.items():
            for kb, vb in counterB.items():
                res_counter[ka + kb] += va * vb
        return res_counter

    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """Treat this as a two two-sum problems. We compute all possible two
        sums between A and B. And do the same with C and D. Then we compute
        the two sums between resAB and resCD. It is important that we split
        the work load this way, as each would be just 500 * 500 number of
        operations. If we stack this any higher, say do a resABC, then the
        number of computation would sky rocket and we will hit TLE.

        O(N^2), 328 ms, 36% ranking.
        """
        resAB = self.two_sums(Counter(A), Counter(B))
        resCD = self.two_sums(Counter(C), Counter(D))
        return sum(resCD.get(-k, 0) * v for k, v in resAB.items())


class Solution2:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """A smarter solution, credit to Stefan Pochmann

        O(N^2), 248 ms, 94% ranking.
        """
        resAB = Counter(a + b for a in A for b in B)
        return sum(resAB[-c - d] for c in C for d in D)


# sol = Solution()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
