# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import zip_longest


class Solution1:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """LeetCode 290

        Pay attention to all the edge cases.

        O(N), 23 ms, faster than 98.81%
        """
        pat_word_map = {}
        word_pat_map = {}
        for p, word in zip_longest(pattern, s.split(' ')):
            if p is None or word is None:
                return False
            if p not in pat_word_map and word not in word_pat_map:
                pat_word_map[p] = word
                word_pat_map[word] = p
            elif pat_word_map.get(p, '') != word or word_pat_map.get(word, '') != p:
                return False
        return True


class Solution2:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """Convert pattern and s to something that we can compare directly. The
        choice to convert to is index.
        """
        s_lst = s.split(' ')
        if len(pattern) != len(s_lst):
            return False
        return [pattern.index(p) for p in pattern] == [s_lst.index(w) for w in s_lst]


sol = Solution2()
tests = [
    ("abba", "dog cat cat dog", True),
    ("abba", "dog cat cat fish", False),
    ("aaaa", "dog cat cat dog", False),
    ("aaa", "aa aa aa aa", False),
    ("he", "unit", False),
]

for i, (pattern, s, ans) in enumerate(tests):
    res = sol.wordPattern(pattern, s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
