# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def decodeAtIndex(self, S: str, K: int) -> str:
        """The Kth, or K - 1 th if we use index, letter can happen in two
        situation. One is that it is within a stretch of letters before any
        repetition of the said stretch. The other is that it is within a
        repeated region. In the first scenario, if we keep track of the current
        index of the string, we can return the K - 1 th letter when the index
        matches K - 1. In the second scenario, once K - 1 falls within a
        repeated range, we can use remainder to identify where the K - 1 th
        letter would have fallen if we had started over given the current
        repetition.

        O(?), 32 ms, 44% ranking.
        """

        def helper(k) -> str:
            i = -1
            for s in S:
                if 'a' <= s <= 'z':
                    i += 1
                    if k == i:  # target encountered when going through letter
                        return s
                else:  # s is a digit
                    repeat_len = i + 1
                    i = i + (int(s) - 1) * repeat_len  # new i after the repeat
                    if k <= i:
                        return helper(k % repeat_len)

        return helper(K - 1)


class Solution2:
    def decodeAtIndex(self, S: str, K: int) -> str:
        """Standard solution, non-recursive.

        The key idea is the same, that once we find a repeat length, we do
        K = K % repeat_len. However, the standard solution uses a very smart
        trick, in which the total lenght of the expanded string is computed
        and the original string is reversed. This way, once we hit a number, we
        know that the current length of the expanded string must be a multiple
        of the number. We can run length // int(s) to acquire the repeat length
        of the current repeat.

        O(N), 32 ms, 44% ranking.
        """
        size = 0
        for s in S:
            size = (size + 1) if s.isalpha() else size * int(s)
        for s in S[::-1]:
            K %= size
            if s.isalpha():
                if K == 0:
                    return s
                size -= 1
            else:
                size //= int(s)


sol = Solution2()
tests = [
    ('leet2code3', 1, 'l'),
    ('leet2code3', 2, 'e'),
    ('leet2code3', 3, 'e'),
    ('leet2code3', 4, 't'),
    ('leet2code3', 5, 'l'),
    ('leet2code3', 6, 'e'),
    ('leet2code3', 7, 'e'),
    ('leet2code3', 8, 't'),
    ('leet2code3', 9, 'c'),
    ('leet2code3', 10, 'o'),
    ('leet2code3', 11, 'd'),
    ('leet2code3', 12, 'e'),
    ('leet2code3', 13, 'l'),
    ('leet2code3', 14, 'e'),
    ('leet2code3', 15, 'e'),
    ('leet2code3', 16, 't'),
    ('leet2code3', 17, 'l'),
    ('leet2code3', 18, 'e'),
    ('leet2code3', 19, 'e'),
    ('leet2code3', 20, 't'),
    ('leet2code3', 21, 'c'),
    ('leet2code3', 22, 'o'),
    ('leet2code3', 23, 'd'),
    ('leet2code3', 24, 'e'),
    ('leet2code3', 25, 'l'),
    ('leet2code3', 26, 'e'),
    ('leet2code3', 27, 'e'),
    ('leet2code3', 28, 't'),
    ('leet2code3', 29, 'l'),
    ('leet2code3', 30, 'e'),
    ('leet2code3', 31, 'e'),
    ('leet2code3', 32, 't'),
    ('leet2code3', 33, 'c'),
    ('leet2code3', 34, 'o'),
    ('leet2code3', 35, 'd'),
    ('leet2code3', 36, 'e'),
    ('ha22', 1, 'h'),
    ('ha22', 2, 'a'),
    ('ha22', 3, 'h'),
    ('ha22', 4, 'a'),
    ('ha22', 5, 'h'),
    ('ha22', 6, 'a'),
    ('ha22', 7, 'h'),
    ('ha22', 8, 'a'),
    ('a2345678999999999999999', 1, 'a'),
    ('a2345678999999999999999', 10, 'a'),
    ('a2345678999999999999999', 100, 'a'),
    ('a2345678999999999999999', 1000, 'a'),
    ('a2345678999999999999999', 10000, 'a'),
    ('a2345678999999999999999', 100000, 'a'),
]

for i, (S, K, ans) in enumerate(tests):
    res = sol.decodeAtIndex(S, K)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
