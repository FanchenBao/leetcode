# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """Use two sets to keep track of the numbers in each array. For each new
        pair of a and b, if they are the same, we increment the count by 1.
        
        If they are the same, but one of them has been encountered by the other
        array whereas the other number has not, we increment the count by 1.

        If both have been encountered by the other arrays, we increment by 2.

        O(N), 142 ms, faster than 88.14%
        """
        sa, sb = set(), set()
        res = [0]
        for a, b in zip(A, B):
            if a == b or (a in sb and b not in sa) or (b in sa and a not in sb):
                res.append(res[-1] + 1)
            elif a != b and a in sb and b in sa:
                res.append(res[-1] + 2)
            else:
                res.append(res[-1])
            sa.add(a)
            sb.add(b)
        return res[1:]


class Solution2:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """Inspired by lee215 https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/discuss/3466962/JavaC%2B%2BPython-One-Pass

        The idea is that as we iterate through each pair of values in A and B,
        if the value has been seen before, that means it must exist in either
        A or B, which means we have come to a point where it exists in both.

        What this means is that we just need to count the moment when the value
        in A and B shows up the second time.

        O(N), 129 ms, faster than 99.06%
        """
        seen = set()
        res = []
        cur = 0
        for ab in zip(A, B):
            for v in ab:
                if v in seen:
                    cur += 1
                seen.add(v)
            res.append(cur)
        return res


sol = Solution2()
tests = [
    ([1,3,2,4], [3,1,2,4], [0,2,3,4]),
    ([2,3,1], [3,1,2], [0,1,3]),
]

for i, (A, B, ans) in enumerate(tests):
    res = sol.findThePrefixCommonArray(A, B)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
