# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """LeetCode 1657

        Operation 1 indicates that if word1 and word2 are anagrams, they can be
        converted.

        Operation 2 indicates that if word1 and word2 share the same letters and
        the same pattern in count for all the letters, they can be converted
        into anagrams.

        Thus, the check is for the two words to have the same length, share the
        same letters, and have the same pattern on letter count.

        O(N), 516 ms, faster than 29.60%

        UPDATE: dict's keys can be compared directly, and the length check can
        be accomplished using the counter value check

        141 ms, faster than 97.60%
        """
        c1, c2 = Counter(word1), Counter(word2)
        return c1.keys() == c2.keys() and sorted(c1.values()) == sorted(c2.values())


sol = Solution()
tests = [
    ("abc", "bca", True),
    ("a", "aa", False),
    ("cabbba", "abbccc", True),
]

for i, (word1, word2, ans) in enumerate(tests):
    res = sol.closeStrings(word1, word2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
