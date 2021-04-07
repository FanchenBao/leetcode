# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    def halvesAreAlike(self, s: str) -> bool:
        """LeetCode 1704

        Use counter to tally the number of letters on the first and second
        half. Sum the total number of vowels on the first and second half, and
        check whether they are equal.

        O(N), 28 ms, 94% ranking.
        """
        ca = Counter(s[:len(s) // 2])
        cb = Counter(s[len(s) // 2:])
        return sum(ca[v] for v in self.vowels) == sum(cb[v] for v in self.vowels)


sol = Solution()
tests = [
    ('book', True),
    ('textbook', False),
    ('MerryChristmas', False),
    ('AbCdEfGh', True),
]

for i, (s, ans) in enumerate(tests):
    res = sol.halvesAreAlike(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
