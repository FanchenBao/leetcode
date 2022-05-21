# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right, bisect_left
from collections import defaultdict
from itertools import accumulate


class Solution1:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        """I checked the first hint, which is very very important. It points
        to a very smart way to model this problem. The number of flowers
        blooming at a certain time is the number of flowers already started
        blooming minus the number of flowers already terminated blooming. This
        means we only need to do two rounds of binary search, one on the starts
        and the other the ends. Then we are done.

        O(NlogN), 1429 ms, faster than 60.57%
        """
        los = sorted(s for s, e in flowers)
        his = sorted(e for s, e in flowers)
        return [bisect_right(los, p) - bisect_left(his, p) for p in persons]


class Solution2:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        """This solution is the second one offered by lee215

        https://leetcode.com/problems/number-of-flowers-in-full-bloom/discuss/1977099/C%2B%2BPython-Binary-Search-and-Sweep-Line

        We track the change in the number of flowers blooming at each time
        point. Then we obtain prefix sum, which is the number of blooming
        flowers from one time point to the next. We then binary search the
        time points to know the number of blooming flowers.
        """
        diff = defaultdict(int)
        for s, e in flowers:
            diff[s] += 1
            diff[e + 1] -= 1
        timepoints = sorted(diff)
        num_flowers = list(accumulate(diff[t] for t in timepoints))
        return [num_flowers[bisect_right(timepoints, p) - 1] for p in persons]



sol = Solution2()
tests = [
    ([[1,6],[3,7],[9,12],[4,13]], [2,3,7,11], [1, 2, 2, 2]),
    ([[1,10],[3,3]], [3,3,2], [2,2,1]),
]

for i, (flowers, persons, ans) in enumerate(tests):
    res = sol.fullBloomFlowers(flowers, persons)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
