# from pudb import set_trace; set_trace()
from collections import defaultdict
from typing import List
import math


class Solution1:
    def minimumOperations(self, num: str) -> int:
        """
        Divisible by 25 means the number must end in 25, 50, 75, or 00. If none
        of these pattern exists, we need to reduce num to 0. If there is a 0,
        then we remove all the other digits. If no zero exists, we remove the
        entire thing.

        O(N), 43 ms, faster than 47.02%
        """
        N = len(num)
        MAX = 1000

        def num_ops(pat: str) -> int:
            indices = []
            pi = len(pat) - 1
            for i in range(N - 1, -1, -1):
                if num[i] == pat[pi]:
                    indices.append(i)
                    pi -= 1
                    if pi < 0:
                        break
            if pi < 0:
                res = 0
                pre = N
                for idx in indices:
                    res += pre - idx - 1
                    pre = idx
                return res
            return MAX

        res = min(num_ops(pat) for pat in ["25", "50", "75", "00"])
        if res < MAX:
            return res
        if "0" in num:
            return N - 1
        return N


class Solution2:
    def minimumOperations(self, num: str) -> int:
        """
        Same method as Solution1 but most likely faster

        O(N) 39 ms, faster than 65.56%
        """
        N = len(num)
        MAX = 1000
        indices = defaultdict(list)
        for i in range(N - 1, -1, -1):
            indices[num[i]].append(i)

        def num_ops(pat: str) -> int:
            if len(indices[pat[1]]) > 0:
                idx2 = indices[pat[1]][0]
                for idx1 in indices[pat[0]]:
                    if idx1 < idx2:
                        return N - idx1 - 2
            return MAX

        res = min(num_ops(pat) for pat in ["25", "50", "75", "00"])
        if res < MAX:
            return res
        if "0" in num:
            return N - 1
        return N


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
