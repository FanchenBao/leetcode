# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        """LeetCode 423

        The logic:

        zero if we have z, that means we have 0
        two if we have w, that means we have 2
        six  if we have x, that means we haev 6
        seven after removing all sixes, if we have s, that means we have 7
        five after removing all sevens, if we have v, that means we have 5
        four after removing all fives, if we have f, that means we have 4
        three after removing all fours, if we have r, that means we have 3
        eight after removing all threes, if we have h, that means we have 8
        nine after removing all eights, if we have i, that means we have 9
        The remaning is ones

        Seems more like a brain-teaser to me.

        O(N), 48 ms, 76% ranking.
        """
        res = ''
        counter = Counter(s)
        order = [
            ('zero', 'z', '0'),
            ('two', 'w', '2'),
            ('six', 'x', '6'),
            ('seven', 's', '7'),
            ('five', 'v', '5'),
            ('four', 'f', '4'),
            ('three', 'r', '3'),
            ('eight', 'h', '8'),
            ('nine', 'i', '9'),
            ('one', 'o', '1'),
        ]
        for word, label, dig in order:
            c = counter[label]
            res += dig * c
            for le in word:
                counter[le] -= c
        return ''.join(sorted(res))


sol = Solution()
tests = [
    ('owoztneoer', '012'),
    ('fviefuro', '45'),
]

for i, (s, ans) in enumerate(tests):
    res = sol.originalDigits(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
