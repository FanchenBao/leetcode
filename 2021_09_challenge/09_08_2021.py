# from pudb import set_trace; set_trace()
from typing import List
from itertools import accumulate


class Solution1:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        """LeetCode 848

        We perform prefix sum backwards on shifts, and then apply each shift
        to each letter in s.

        O(N), 812 ms. 59% ranking
        """
        res = ''
        for i, shift in enumerate(accumulate(shifts[::-1]), 1):
            res += chr((ord(s[-i]) - 97 + shift) % 26 + 97)
        return res[::-1]


class Solution2:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        """I thought by taking mod at each prefix sum can avoid large numbers
        and thus reducing run time, but it turns out not so.
        """
        N = len(s)
        res = [0] * N
        for i in range(N - 1, -1, -1):
            if i != N - 1:
                shifts[i] = (shifts[i] + shifts[i + 1]) % 26
            res[i] = (ord(s[i]) - 97 + shifts[i]) % 26 + 97
        return ''.join(chr(r) for r in res)


class Solution3:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = [ord(a) for a in s]
        N = len(s)
        for i in range(N - 1, - 1, -1):
            if i == N - 1:
                res[i] = (res[i] - 97 + shifts[i]) % 26 + 97
            else:
                res[i] = (res[i + 1] + res[i] - ord(s[i + 1]) - 97 + shifts[i]) % 26 + 97
        return ''.join(chr(r) for r in res)


class Solution4:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        """Oneliner
        """
        return ''.join(chr((ord(s[-i]) - 97 + shift) % 26 + 97) for i, shift in enumerate(accumulate(shifts[::-1]), 1))[::-1]


sol = Solution4()
tests = [
    ('abc', [3, 5, 9], 'rpl'),
    ('aaa', [1, 2, 3], 'gfd'),
]

for i, (s, shifts, ans) in enumerate(tests):
    res = sol.shiftingLetters(s, shifts)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
