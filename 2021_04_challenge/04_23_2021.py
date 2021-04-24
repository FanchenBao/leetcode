# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def countBinarySubstrings(self, s: str) -> int:
        """LeetCode 696

        The idea is to count consecutive zeros and ones. Each time a new zero
        or one is counted, we can determine whether this addition can be made
        into a valid substring. The criterion for this is that the number of
        the current consecutive zeros (or ones) is smaller or equal to the
        number of the immediately previous conseutive ones (or zeros). We simply
        add all of the valid instances together.

        O(N), 208 ms, 21% ranking.
        """
        con_zero, con_one, res = 0, 0, 0
        for i, le in enumerate(s):
            if le == '0':
                if i - 1 >= 0 and s[i - 1] == '1':
                    con_zero = 0
                con_zero += 1
                res += con_zero <= con_one
            else:
                if i - 1 >= 0 and s[i - 1] == '0':
                    con_one = 0
                con_one += 1
                res += con_one <= con_zero
        return res


class Solution2:
    def countBinarySubstrings(self, s: str) -> int:
        """Update res not on each iteration, but on when we switch from zero to
        one or one to zero.

        224 ms
        """
        con_zero, con_one, res = 0, 0, 0
        for i, le in enumerate(s):
            if le == '0':
                if i - 1 >= 0 and s[i - 1] == '1':
                    res += min(con_one, con_zero)
                    con_zero = 0
                con_zero += 1
            else:
                if i - 1 >= 0 and s[i - 1] == '0':
                    res += min(con_one, con_zero)
                    con_one = 0
                con_one += 1
        return res + min(con_one, con_zero)


class Solution3:
    def countBinarySubstrings(self, s: str) -> int:
        """Better implementation of Solution2.

        The trick is to not differentiate between 0 and 1. Instead, we simply
        compare adjacent letters. When they are different, we know that a change
        has happened. Also, we use pre and cur to record the consecutive zeros
        or ones that happen before and right now.

        152 ms
        """
        pre, cur, res = 0, 1, 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                res += min(pre, cur)
                pre, cur = cur, 1
            else:
                cur += 1
        return res + min(pre, cur)


class Solution4:
    def countBinarySubstrings(self, s: str) -> int:
        """From lee215, amazingly smart solution:

        https://leetcode.com/problems/count-binary-substrings/discuss/108625/JavaC%2B%2BPython-Easy-and-Concise-with-Explanation

        It's the same idea but by adding gaps between transitions of 0 and 1,
        the implementation is vastly simplified

        128 ms
        """
        gapped = s.replace('01', '0 1').replace('10', '1 0')
        con_len = [len(g) for g in gapped.split()]
        return sum(min(l1, l2) for l1, l2 in zip(con_len, con_len[1:]))


sol = Solution4()
tests = [
    ('00110011', 6),
    ('10101', 4),
]

for i, (s, ans) in enumerate(tests):
    res = sol.countBinarySubstrings(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
