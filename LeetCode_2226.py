# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_left


class Solution1:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        """I was correct to use binary search for this problem. Where I got
        stuck was that I was using the smallest value in candies as the lower
        bound. This is wrong. Lower bound should be 0, and higher bound should
        be total number of candies divided by k.

        The one tricky part is that after the binary search is over, we have to
        check lo one more time, because the search ends with lo incremented by
        one, and the new lo has never been checked. It is possible that the
        new lo can satisfy the requirements as well.

        O(NlogN), 1336 ms, 87% ranking.
        """
        candies.sort()
        total, N = sum(candies), len(candies)
        lo, hi = 0, total // k
        while lo < hi:
            mid = (lo + hi) // 2
            if mid * k > total:
                hi = mid
            else:
                idx = bisect_left(candies, mid)
                if not mid or sum(candies[i] // mid for i in range(idx, N)) >= k:
                    lo = mid + 1
                else:
                    hi = mid
        idx = bisect_left(candies, lo)
        if not lo or sum(candies[i] // lo for i in range(idx, N)) >= k:
            return lo
        return lo - 1


class Solution2:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        """Solution by lee215

        https://leetcode.com/problems/maximum-candies-allocated-to-k-children/discuss/1908888/JavaC%2B%2BPython-Binary-Search-with-Explanation
        """
        candies.sort()
        lo, hi = 0, sum(candies) // k
        while lo < hi:
            mid = (lo + hi + 1) // 2  # according to lee215, this is to find the last valid element
            if sum(c // mid for c in candies) >= k:
                lo = mid  # since mid is already biased to the right, we don't bias lo anymore
            else:
                hi = mid - 1
        return lo
        

sol = Solution2()
tests = [
    ([5, 8, 6], 3, 5),
    ([2, 5], 11, 0),
    ([43,4,5,65,7,89,9,87,6,5,4,3], 23, 11),
    ([4,7,5], 4, 3),
    ([4, 5], 3, 2),
    ([4, 5], 5, 1),
    ([9,10,1,2,10,9,9,10,2,2], 3, 10),
]

for i, (candies, k, ans) in enumerate(tests):
    res = sol.maximumCandies(candies, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
