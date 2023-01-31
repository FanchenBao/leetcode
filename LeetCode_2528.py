# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate
from bisect import bisect_left



class Solution1:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        """TLE
        """
        N = len(stations)
        prestations = list(accumulate(stations))
        powers = []
        for i in range(N):
            lo, hi = i - r - 1, min(i + r, N - 1)
            powers.append([prestations[hi] - (prestations[lo] if lo >= 0 else 0), i])
        
        powers.sort()
        presum = list(accumulate(p for p, _ in powers))
        lo, hi = powers[0][0], powers[-1][0] + k + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mid - powers[0][0] > k:
                hi = mid
            else:
                idx = bisect_left(powers, mid, key=lambda tup: tup[0])
                if mid * idx - presum[idx - 1] > k * (2 * r + 1):
                    hi = mid
                else:
                    idx_power = sorted([[p, i] for p, i in powers[:idx]], key=lambda tup: tup[1])
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
                        continue
                    hi = mid
        return lo - 1


class Solution2:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        N = len(stations)
        prestations = list(accumulate(stations))
        powers = []
        for i in range(N):
            lo, hi = i - r - 1, min(i + r, N - 1)
            powers.append(prestations[hi] - (prestations[lo] if lo >= 0 else 0))
        
        min_power = min(powers)
        lo, hi = min_power, max(powers) + k + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mid - min_power > k:
                hi = mid
            else:
                allowed = k
                low_powers = [(i, p) for i, p in enumerate(powers) if p < mid]
                i = 0
                # print(lo, hi, mid, low_powers)
                while i < len(low_powers):
                    cur_min = math.inf
                    lim = min(N - 1, low_powers[i][0] + 2 * r)
                    while i < len(low_powers) and low_powers[i][0] <= lim:
                        cur_min = min(cur_min, low_powers[i][1])
                        i += 1
                    allowed -= mid - cur_min
                    if allowed < 0:
                        break
                else:
                    lo = mid + 1
                    # print(lo, hi)
                    continue
                hi = mid
            # print(lo, hi)
        # print(lo, hi)
        return lo - 1


sol = Solution2()
tests = [
    # ([1,2,4,5,0], 1, 2, 5),
    # ([4,4,4,4], 0, 3, 4),
    # ([2,10,12,3], 0, 14, 9),
    # ([48,16,29,41,2,43,23], 5, 40, 194),
    # ([37,80,31,64,41,7,58,40,49], 0, 7, 14),
    ([57,70,35,30,29,13,17,88,89,49], 1, 90, 138),
]

for i, (stations, r, k, ans) in enumerate(tests):
    res = sol.maxPower(stations, r, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
