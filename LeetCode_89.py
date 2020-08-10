#! /usr/bin/env python3
from typing import List
from time import time

beg = time()
"""
07/16/2019

Not a difficult one, as long as you get the trick of how to construct grey
code. The basic idea is that in order to create 2n digits of grey code, we
just need all the n-digit grey code, reverse them, then add an extra 1 at its
top. The implementation of this is not particularly hard.

The smartass() method came from the fastest implementation that I just couldn't
help but admiring. So elegantly it reflects the operation of putting extra 1
to the top.
"""


class Solution:
    def grayCode(self, n: int) -> List[int]:
        """ create grayCode by iterating through the already-created grayCode
            backwards and add power of 2 to it
        """
        res = [0]
        for i in range(n):
            for j in range(2 ** i - 1, -1, -1):
                res.append(res[j] + 2 ** i)
        return res

    def smartass(self, n: int) -> List[int]:
        res: List[int] = [0]
        for i in range(n):
            res += [x | (1 << i) for x in res[::-1]]
        return res


sol = Solution()
print(sol.smartass(10))

print("\nTime: {}".format(time() - beg))
