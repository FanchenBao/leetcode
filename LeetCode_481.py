# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def magicalString(self, n: int) -> int:
        """This one is not hard. Basically, we just extend the magical string
        until there are n elements. Then we count the number of ones in it.

        O(N), 130 ms, 75% ranking.

        UDPATE: The trick to flip between 1 and 2 is to use the last element
        and XOR it with 3.

        Ref: https://leetcode.com/problems/magical-string/discuss/96408/Short-C%2B%2B
        """
        s = [1, 2, 2]
        i = 2
        while len(s) < n:
            s.extend([s[-1] ^ 3] * s[i])
            i += 1
        return s[:n].count(1)


sol = Solution()
tests = [
    (6, 3),
    (1, 1),
    (7, 4),
    (8, 4),
    (9, 4),
    (10, 5),
    (11, 5),
    (12, 5),
    (13, 6),
    (14, 7),
    (15, 7),
    (16, 8),
    (17, 9),
]

for i, (n, ans) in enumerate(tests):
    res = sol.magicalString(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
