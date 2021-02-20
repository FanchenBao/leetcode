# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    data = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
    }

    def romanToInt(self, s: str) -> int:
        """LeetCode 13

        We use a trick to instantiate the data only once, which contains all
        the Roman letter mapping to numbers. Then we iterate through all letters
        in s, first checking whether a pair matches a double letter key. If it
        does, we increment result by the double letter key. If not, we increment
        via single letter key.

        O(N), the trick allows us to run for 52 ms. Without the trick, i.e.,
        having the data declared each time romanToInt is called, we would run at
        72 ms. 52 ms is 46% ranking.

        UPDATE: a key finding from this post (https://leetcode.com/problems/roman-to-integer/discuss/6529/My-solution-for-this-question-but-I-don't-know-is-there-any-easier-way/243924)
        gave me idea that we can simply use splicing to avoid check for i + 1 <
        len(s), because no matter how big i + 1 is, as long as it is out of
        range, splicing will not throw exception. It will just set the end range
        to the end of the string. So by using splicing, we avoid one extra
        comparison, and we also avoid explicit string cancatenation.

        The latest method clocked in at 36 ms, 98% ranking.
        """
        res, i = 0, 0
        while i < len(s):
            if (k := s[i:i + 2]) in self.data:
                res += self.data[k]
                i += 1
            else:
                res += self.data[s[i]]
            i += 1
        return res


class Solution2:
    data = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        """This is a cleaner solution, going from back to front and making
        decision whether to add or substract in real-time.

        Reference: https://leetcode.com/problems/roman-to-integer/discuss/6542/4-lines-in-Python
        """
        res, p = 0, 'I'
        for i in range(len(s) - 1, -1, -1):
            res, p = res - self.data[s[i]] if self.data[s[i]] < self.data[p] else res + self.data[s[i]], s[i]
        return res


sol = Solution2()
tests = [
    ('III', 3),
    ('IV', 4),
    ('VI', 6),
    ('IX', 9),
    ('XI', 11),
    ('LVIII', 58),
    ('MCMXCIV', 1994),
]

for i, (s, ans) in enumerate(tests):
    res = sol.romanToInt(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
