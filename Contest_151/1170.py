#! /usr/bin/env python3
from typing import List

# from collections import Counter
from bisect import bisect_right

# from pprint import pprint as pp
"""08/26/2019

Solution1:
Use Counter to implement function f, use binary search to count the number of
words with f(word) value larger than f(query). Clocked in at 132 ms, 63%

Update: I read the discussion and realized that function f() can be easily
implemented via built-int function string.count() and min(). This drastically
reduces run time to 76ms, 98%.
"""


class Solution1:
    def numSmallerByFrequency(
        self, queries: List[str], words: List[str]
    ) -> List[int]:
        words_count = sorted([w.count(min(w)) for w in words])
        return [
            len(words_count) - bisect_right(words_count, q.count(min(q)))
            for q in queries
        ]

    # def f(self, s: str) -> int:
    #     count = Counter(s)
    #     for cha in range(97, 123):
    #         if chr(cha) in count:
    #             return count[chr(cha)]
    #     return 0


sol = Solution1()
queries = ["bbb", "cc"]
words = ["a", "aa", "aaa", "aaaa"]
print(sol.numSmallerByFrequency(queries, words))
