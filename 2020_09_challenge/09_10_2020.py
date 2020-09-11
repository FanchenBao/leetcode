# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def getHint(self, secret: str, guess: str) -> str:
        """Naive approach. Pass OJ"""
        cs = Counter(secret)
        cg = Counter(guess)
        A, B = 0, 0
        for s, g in zip(secret, guess):
            if s == g:
                cs[s] -= 1
                cg[g] -= 1
                A += 1
        for g in cg.keys():
            if g in cs:
                B += min(cs[g], cg[g])
        return f'{A}A{B}B'


class Solution2:
    def getHint(self, secret: str, guess: str) -> str:
        """Similar approach, but cleaner solution"""
        cs, cg = Counter(secret), Counter(guess)
        A = sum(s == g for s, g in zip(secret, guess))
        B_plus_A = sum(min(cs.get(g, 0), cg[g]) for g in cg.keys())
        return f'{A}A{B_plus_A - A}B'