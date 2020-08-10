#! /usr/bin/env python3
from typing import List, Dict
from collections import Counter

"""08/22/2019

Easy problem.
"""


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res: int = 0
        char_count: Dict[str, int] = Counter(chars)
        for word in words:
            word_count: Dict[str, int] = Counter(word)
            for k, v in word_count.items():
                if v > char_count[k]:
                    break
            else:
                res += len(word)
        return res


sol = Solution()
words = ["hello", "world", "leetcode"]
chars = "welldonehoneyr"
print(sol.countCharacters(words, chars))
