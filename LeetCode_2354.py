# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter, defaultdict
from itertools import accumulate
from bisect import bisect_left


class Solution1:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        """The breakthrough is the realization that the total number of set bits
        from (num1 & num2) + (num1 | num2) is the same as the sum of the set
        bits in num1 and num2. This is because any set bit that overlaps in the
        OR can be regained in AND, whereas any set bit that does not overlap
        and hence is canceled in AND can be regained in OR.

        With this insight, we can build a counter with the key being the number
        of set bits. We count the number of unique values in nums that have
        the designated number of set bits. Then we sort the keys. For any key
        s, we binary search on k - s. All the numbers that have set bits larger
        or equal to k - s can be paired with s. To reduce computation time, we use
        prefix sum to make range sum calculation O(1). Then the number of
        choices is the count of s multiplied by the count of all the other
        unique numbers that have number of set bits larger or equal to k - s.

        Note that, since there is no requirement for a number to occur more
        than once in the original nums for it to pair with itself, when k - s
        is equal to s, the rule of counting is the same as when k - s != s.

        O(N), 961 ms, faster than 80.99%
        Note that len(sorted_setbit) is at most 32, because it represents the
        posibilities of different count of set bits.
        """
        counter = Counter(bin(n).count('1') for n in set(nums))
        sorted_setbit = sorted(counter)
        presum = list(accumulate(counter[s] for s in sorted_setbit))
        res = 0
        for s in sorted_setbit:
            idx = bisect_left(sorted_setbit, k - s)
            if idx < len(sorted_setbit):
                # this also handles the situation where sorted_setbit[idx] == s
                res += (presum[-1] - int(idx > 0) * presum[idx - 1]) * counter[s]
        return res


class Solution2:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        """From lee215. Same idea as Solution1, but since the length of counter
        is at most 32, we don't have to bother with binary search.

        Ref: https://leetcode.com/problems/number-of-excellent-pairs/discuss/2324984/JavaC%2B%2BPython-Inclusion-Exclusion-Principle

        O(N), 1871 ms, faster than 42.98%
        """
        c = Counter(bin(n).count('1') for n in set(nums))
        return sum(c[c1] * c[c2] for c1 in c for c2 in c if c1 + c2 >= k)
        

sol = Solution2()
tests = [
    ([1,2,3,1], 3, 5),
    ([5,1,1], 10, 0),
    ([6, 10, 7, 10, 10], 3, 9),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.countExcellentPairs(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
