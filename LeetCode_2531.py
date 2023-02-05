# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def prep_counter(self, cc: Counter, o: str, i: str) -> Counter:
        cc[o] -= 1
        cc[i] += 1
        if cc[o] == 0:
            del cc[o]
        return cc

    def isItPossible(self, word1: str, word2: str) -> bool:
        """Since the max number of unique letters is 26. We can create two
        counters out of word1 and word2, and then brute force it. This method
        also uses the laziest implementation where we make a copy of the
        counter each time.

        O(26 * 26 * 26), 174 ms, faster than 45.39%

        UPDATE: revert the operation, so that we don't have to make copies
        O(26 * 26), 142 ms, faster than 62.95%
        """
        c1, c2 = Counter(word1), Counter(word2)
        for a1 in list(c1.keys()):
            for a2 in list(c2.keys()):
                self.prep_counter(c1, a1, a2)
                self.prep_counter(c2, a2, a1)
                if len(c1) == len(c2):
                    return True
                # revert
                self.prep_counter(c1, a2, a1)
                self.prep_counter(c2, a1, a2)
        return False
        

sol = Solution()
tests = [
    ("abcc", "aab", True),
]

for i, (word1, word2, ans) in enumerate(tests):
    res = sol.isItPossible(word1, word2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
