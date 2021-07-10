# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def __init__(self):
        self.MOD = 10**9 + 7

    def compute(self, ch, i, pre, prepre, s) -> int:
        """pre represents the number of decoding if the ch does NOT combine.

        prepre represents the number of deecoding if the ch combines
        """
        if ch == '0':
            res = prepre * 2 if s[i - 1] == '*' else prepre
        elif '1' <= ch <= '6':
            if s[i - 1] in {'1', '2'}:
                res = pre + prepre
            elif s[i - 1] == '*':
                res = pre + prepre * 2
            else:
                res = pre
        else:  # '7' <= ch <= '9'
            if s[i - 1] in {'1', '*'}:
                res = pre + prepre
            else:
                res = pre
        return res % self.MOD

    def numDecodings(self, s: str) -> int:
        """LeetCode 639

        This is DP, but with pretty intricate logic. We keep track on the
        total number of decoding possible with the given string ending at each
        index. Then we compute the number of decoding for the next digit. The
        complicated part is when the previous digit is a '*', or the previous
        previous digit is a '*'. For a digit, there is only one answer for the
        total number of decoding. For a '*', we need to record two answers, one
        is for digits 1 to 6, and the other 7 to 9.

        For each digit, we can either decode it by itself, which means the total
        number of decoding is equal to the total decoding of the previous char.
        Or, we can decode it by combination with the previous char, if and only
        if the previous char is 1 or 2. Then we need to look for the total
        number of decoding with the previous previous char. If the current char
        is '*', we basically have to go through 1 to 9. However, 1 to 6 gives
        the same answer (because they can both be self and combine with both 1
        and 2), and 7 to 9 also gives the same answer (because they can both be
        self and combine with 1).

        Continue with this logic until the end, and we have the answer.

        ONE MORE TRICK: keep modulo throughout the algorithm. This significantly
        reduces time, most likely because arithmetic of gigantic number is very
        slow.

        O(N), 740 ms, 33% ranking.

        UPDATE: simplify the code following the official solution here:

        https://leetcode.com/problems/decode-ways-ii/solution/

        We do not have to use array to record the total decoding of '*' situation.
        Using a single value suffices.

        344 ms, 82% ranking.
        """
        prepre = 1
        pre = 9 if s[0] == '*' else (0 if s[0] == '0' else 1)
        for i in range(1, len(s)):
            if s[i] == '0' and s[i - 1] not in {'1', '2', '*'}:
                return 0
            if s[i] == '*':
                cur = (self.compute('1', i, pre, prepre, s) * 6 + self.compute('7', i, pre, prepre, s) * 3) % self.MOD
            else:
                cur = self.compute(s[i], i, pre, prepre, s)
            prepre, pre = pre, cur
        return pre


sol = Solution()
tests = [
    ('*', 9),
    ('1*', 18),
    ('2*', 15),
    ('*4', 11),
    ('**4', 114),
    ('30', 0),
    ('0', 0),
]

for i, (s, ans) in enumerate(tests):
    res = sol.numDecodings(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
