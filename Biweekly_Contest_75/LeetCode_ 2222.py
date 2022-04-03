# from pudb import set_trace; set_trace()
from typing import List
from itertools import groupby
from collections import defaultdict


class Solution:
    def numberOfWays(self, s: str) -> int:
        """TLE
        """
        res = 0
        presum = [0, 0]
        s0, s1 = 0, 0
        for a, b in groupby(s):
            if a == '0':
                s0 += len(list(b))
                presum.append(s0)
            else:
                s1 += len(list(b))
                presum.append(s1)
        N = len(presum)
        if (N - 1) % 2:
            last_even_idx = N - 2
            last_odd_idx = N - 1
        else:
            last_even_idx = N - 1
            last_odd_idx = N - 2
        for i in range(2, N - 2):
            for j in range(i + 1, N, 2):
                res += (presum[i] - presum[i - 2]) * (presum[j] - presum[j - 2]) * ((presum[last_odd_idx] - presum[j - 1]) if i % 2 else (presum[last_even_idx] - presum[j - 1]))
        return res


class Solution:
    def numberOfWays(self, s: str) -> int:
        """This is my solution after reading three out of the four hints.

        I was stuck with the idea that this problem needs grouping. By grouping
        I mean count all the consecutive 0s and 1s as one 0 and one 1, with
        the number of repeats tagged along. I thought that was definitely the
        way to go, but it didn't work.

        In fact, this problem is quite straightforward. We know that the end
        product is 101 or 010. Thus, if, as we loop through s, any 0 we find,
        we can create a new way of producing 101 by counting the number of 1s
        to the left and right of this 0. Similarly, any 1 we find, we can
        create a new way of producing 010 by counting the number of 0s to the
        left and right of this 1. Thus, the problem becomes how to count the
        number of 1s and 0s in any given range. This is an easy problem to
        solve using prefix sum.

        O(N) time, O(N) space, 1381 ms

        UPDATE: we can do this in O(1) space. Brilliant!
        Without the need to build DP array, runtime reduces to 689 ms
        """
        total0 = s.count('0')
        total1 = len(s) - total0
        res, cnt0, cnt1 = 0, 0, 0
        for i, le in enumerate(s):
            if le == '1':
                res += cnt0 * (total0 - cnt0)
                cnt1 += 1
            else:
                res += cnt1 * (total1 - cnt1)
                cnt0 += 1
        return res

                
sol = Solution()
tests = [
    ('001101', 6),
    ('111000', 0),
    ("0001100100", 38),
]

for i, (s, ans) in enumerate(tests):
    res = sol.numberOfWays(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
