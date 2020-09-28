# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter
from functools import reduce


class Solution1:
    def findTheDifference(self, s: str, t: str) -> str:
        """Very simple question"""
        cs, ct = Counter(s), Counter(t)
        for k in ct.keys():
            if k not in cs or ct[k] != cs[k]:
                return k


class Solution2:
    def findTheDifference(self, s: str, t: str) -> str:
        """A better solution using counter.
        The documentation of Counter is worth reading. It is more powerful than
        I have expected.

        https://docs.python.org/3.8/library/collections.html#collections.Counter
        """
        return (Counter(t) - Counter(s)).popitem()[0]


class Solution3:
    def findTheDifference(self, s: str, t: str) -> str:
        """One more smart solution: use XOR
        
        When XOR is applied to between two same values, the result is zero. So
        we can do XOR on each letter of s + t. All the matching letters will
        cancel out, regardless of their positions. The remaining value is the
        odd one out.
        """
        return chr(reduce(lambda x, y: x ^ ord(y), s + t, 0))