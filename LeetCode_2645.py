# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def addMinimum(self, word: str) -> int:
        """Greedy. Try for form "abc" as eagerly as possible. Only three
        two-letter combinations might produce interesting result: ab, ac, and bc
        For ab, we have to check if abc is possible. Otherwise, we add one
        letter. For both ac and bc, we add one letter.

        For all other two-letter or one-letter combinations, we always have to
        add two letter with regard to the first letter.

        O(N), 48 ms, faster than 44.77%
        """
        i = 0
        N = len(word)
        res = 0
        while i < N:
            w = word[i:i + 2]
            if w == 'ab':
                if i + 2 < N and word[i + 2] == 'c':
                    i += 3
                else:
                    res += 1
                    i += 2
            elif w == 'ac' or w == 'bc':
                res += 1
                i += 2
            else:
                res += 2
                i += 1
        return res


class Solution2:
    def addMinimum(self, word: str) -> int:
        """Inspired by https://leetcode.com/problems/minimum-additions-to-make-valid-string/discuss/3421831/JavaC%2B%2BPython-Easy-and-Concise-with-Explanation

        Each strictly increasing subsequence corresponds to an eventual abc.
        Thus, the problem turns into counting the total number of strictly
        increasing subsequences.
        """
        pre = 'z'
        num_inc = 0
        for w in word:
            if w <= pre:
                num_inc += 1
            pre = w
        return num_inc * 3 - len(word)


sol = Solution2()
tests = [
    ('b', 2),
    ('aaa', 6),
    ('abc', 0),
    ("bacacbabc", 6),
]

for i, (word, ans) in enumerate(tests):
    res = sol.addMinimum(word)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
