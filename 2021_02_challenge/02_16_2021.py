# from pudb import set_trace; set_trace()
from typing import List
from itertools import chain, product


class Solution1:
    def letterCasePermutation(self, S: str) -> List[str]:
        """Straightforward solution. Use recursion. We hold the first letter,
        and recursively call the same function on the remaining string. Once
        the remaining string is done, we append left the case permutation of the
        first letter.

        This is the most explicit algo.

        O(2^N) worst case (i.e. the string has no numbers). 56 ms, 74% ranking.
        """
        if len(S) == 1:
            if S.isnumeric():
                return [S]
            if S.isalpha():
                return [S.lower(), S.upper()]
        res = []
        for r in self.letterCasePermutation(S[1:]):
            if S[0].isalpha():
                res += [S[0].lower() + r, S[0].upper() + r]
            else:
                res.append(S[0] + r)
        return res


class Solution2:
    def letterCasePermutation(self, S: str) -> List[str]:
        """Smart ass one-liner"""
        return ([S.lower(), S.upper()] if S.isalpha() else [S]) if len(S) == 1 else list(chain(*[[S[0].lower() + r, S[0].upper() + r] if S[0].isalpha() else [S[0] + r] for r in self.letterCasePermutation(S[1:])]))


class Solution3:
    def letterCasePermutation(self, S: str) -> List[str]:
        """Iterative solution, inspired by:
        https://leetcode.com/problems/letter-case-permutation/discuss/115509/Python-simple-solution-(7-lines)
        """
        res = ['']
        for le in S:
            res = list(chain(*[[r + le.lower(), r + le.upper()] for r in res])) if le.isalpha() else [r + le for r in res]
        return res


class Solution4:
    def letterCasePermutation(self, S: str) -> List[str]:
        """Use product. Very smart solution. Note that a numeric letter's
        upper() and lower() is the numeric itself.

        Reference:
        https://leetcode.com/problems/letter-case-permutation/discuss/1068063/Python-Honest-backtracking-%2B-oneliner-explained
        https://leetcode.com/problems/letter-case-permutation/discuss/115544/Python-Easy-2-line-solution
        """
        return map(''.join, product(*[set([le.upper(), le.lower()]) for le in S]))


sol = Solution4()
tests = [
    ('a1b2', ['a1b2', 'a1B2', 'A1b2', 'A1B2']),
    ('3z4', ['3z4', '3Z4']),
    ('12345', ['12345']),
    ('0', '0'),
    ('po', ['po', 'pO', 'Po', 'PO']),
]

for i, (S, ans) in enumerate(tests):
    res = sol.letterCasePermutation(S)
    if set(res) == set(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
