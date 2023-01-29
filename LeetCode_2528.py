# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate
from bisect import bisect_left


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        N = len(stations)
        lo, hi = 0, r
        powers = [[sum(stations[lo:hi + 1]), 0]]
        hi += 1
        while lo < N - 1 - r:
            powers.append([powers[-1][0] + (stations[hi] if hi < N else 0), powers[-1][1] + 1])
            if hi - lo > 2 * r or hi == N:
                powers[-1][0] -= stations[lo]
                lo += 1
            if hi < N:
                hi += 1
        powers.sort()
        presum = list(accumulate(p for p, _ in powers))
        lo, hi = powers[0][0], powers[-1][0] + k + 1
        while lo < hi:
            # print(powers)
            mid = (lo + hi) // 2
            # print(mid)
            if mid - powers[0][0] > k:
                hi = mid
            else:
                idx = bisect_left(powers, mid, key=lambda tup: tup[0])
                if mid * idx - presum[idx - 1] > k * (2 * r + 1):
                    hi = mid
                else:
                    idx_power = sorted(powers[:idx], key=lambda tup: tup[1])
                    allowed = k
                    for i, (p, j) in enumerate(idx_power):
                        if mid <= p:
                            continue
                        needed = mid - p
                        if needed > allowed:
                            break
                        allowed -= needed
                        for ii in range(i + 1, len(idx_power)):
                            if idx_power[ii][1] - j <= 2 * r:
                                idx_power[ii][0] += needed
                            else:
                                break
                    else:
                        lo = mid + 1
                        # print(lo, hi)
                        continue
                    hi = mid
            # print(lo, hi)
        # print(lo, hi)
        return lo - 1


sol = Solution()
tests = [
    # ([1,2,4,5,0], 1, 2, 5),
    # ([4,4,4,4], 0, 3, 4),
    # ([2,10,12,3], 0, 14, 9),
    ([48,16,29,41,2,43,23], 5, 40, 194),
]

for i, (stations, r, k, ans) in enumerate(tests):
    res = sol.maxPower(stations, r, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
