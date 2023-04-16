# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import groupby


class Solution1:
    def minOperations(self, n: int) -> int:
        """Pure analysis.

        First of all, turn n into binary form.

        If we have an isolated consecutive 1s where isolated means that there
        are at least two 0s flanking the 1s. Then the minimum moves to remove
        all the 1s is 1 if there is only one 1, or 2 if there are more than one
        1s. We arrive at 2 because we can always add 1 to the last position,
        which will cancel out all the 1s and produce an additional at the front.
        Thus, the minimum moves to remove is 2.

        If we have consecutive 1s separated by a single 0, then the minimum
        moves can either be the total number of 1s, or total number of piles of
        1s plus 1. This is because we can always add 1 to the last 1 of the last
        pile. And the newly created 1 can attach to the previous pile, and we
        can perform the same operation again. This results in the total number
        of moves to be the number of piles plus one.

        I use groupby to obtain the size of each pile of 0s or 1s, and analyze
        from there.

        O(logN), 34 ms, faster than 51.92%
        """
        num_piles = num_ones = 0
        res = 0
        for k, g in groupby(bin(n)[2:]):
            s = len(list(g))
            if k == '1':
                num_piles += 1
                num_ones += s
            elif s > 1:
                if num_piles == 1:
                    res += min(num_ones, 2)
                else:
                    res += min(num_ones, num_piles + 1)
                num_piles = num_ones = 0

        if num_piles == 1:
            res += min(num_ones, 2)
        elif num_piles > 0:
            res += min(num_ones, num_piles + 1)
        return res


class Solution2:
    def minOperations(self, n: int) -> int:
        """Same idea but better implementation, from lee215
        Ref: https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/discuss/3203994/JavaC%2B%2BPython-1-line-Solution

        27 ms, faster than 89.57%
        """
        res = 0
        while n > 0:
            if n % 2 == 0:  # get rid of any trailing zeros
                n >>= 1
            elif n & 2:  # n ends with '11', always add 1
                n += 1
                res += 1
            else:  # n ends with '01', remove that 1 by itself
                res += 1
                n >>= 2
        return res


class Solution3:
    def minOperations(self, n: int) -> int:
        """magic solution
        
        The proof, alledgedly is here: https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/discuss/3381484/detailed-explanation-of-why-bit-count-n-3n
        But I haven't gone through it yet.
        """
        return bin(n ^ (n * 3)).count('1')



sol = Solution3()
tests = [
    (39, 3),
    (54, 3),
]

for i, (n, ans) in enumerate(tests):
    res = sol.minOperations(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
