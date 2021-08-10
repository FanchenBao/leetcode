# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """LeetCode 415

        I have to go through a couple wrong answers because I failed to
        recognize the edge cases. And after thinking it over, it turns out that
        left padding 0s is the easiest way to handle all edge cases. So
        basically we left padd 0 to the longest length of num1 and num2, then
        begin adding each digit from right to left with a carry. When all the
        digits are done, we must check the carry again to determine whether
        there needs to be an extra value.

        O(N), 44 ms, 57% ranking.
        """
        max_len = max(len(num1), len(num2))
        num1, num2 = num1.zfill(max_len), num2.zfill(max_len)
        res = []
        c = 0
        for n1, n2 in zip(num1[::-1], num2[::-1]):
            c, r = divmod(int(n1) + int(n2) + c, 10)
            res.append(str(r))
        if c:
            res.append(str(c))
        return ''.join(res)[::-1]


sol = Solution()
tests = [
    ('11', '123', '134'),
    ('456', '77', '533'),
    ('0', '0', '0'),
    ('1', '9', '10'),
    ('9', '99', '108')
]

for i, (num1, num2, ans) in enumerate(tests):
    res = sol.addStrings(num1, num2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
