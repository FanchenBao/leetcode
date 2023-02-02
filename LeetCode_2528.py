# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate
from bisect import bisect_left
from collections import deque


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
        """We know this is a binary search problem from the start, but the
        implementation has still evaded for a quite a while.

        First, we need to obtain the current power level for each station. I
        tried to use a sliding window for this, but it was kind of complicated.
        Thus, I opted for a simpler prefix sum.

        Then, we do the binary search. The trick is to find a way to check
        whether the current power level can be reached given r and k.

        A simple case is when the lowest powered station requires much more
        power than k. We can immediately consider this case impossible.

        Otherwise, we need to go station by station that is currently lower
        than the desired power level. An implementation of sliding window and
        dynamically updated how much power is allowed to add to the current
        station thanks to the powers added in its previous neighbors wihtin the
        r range.

        The rest is formality for binary search.

        O(Nlog(sum of stations + k)), 4459 ms, faster than 49.77%
        """
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
                added_power = deque()
                # total_added is the total power added so far. We use this to
                # check against k.
                # allowed_to_add is the power allowed to be added for the
                # current station. allowed_to_add is updated dynamically,
                # because when the current station falls outside the range, any
                # added power at the beginning of added_power deque must be
                # removed from allowed_to_add.
                total_added = allowed_to_add = 0
                for i, p in ((i, p) for i, p in enumerate(powers) if p < mid):
                    while added_power and i - added_power[0][0] > 2 * r:
                        # current station is outside the influence of the first
                        # station in the dequa that gets additional power,
                        # thus it cannot take the additional power from the
                        # first station
                        _, pp = added_power.popleft()
                        allowed_to_add -= pp
                    to_add = max(0, mid - p - allowed_to_add)
                    total_added += to_add
                    if total_added > k:
                        break
                    allowed_to_add += to_add
                    added_power.append((i, to_add))
                else:
                    lo = mid + 1
                    continue
                hi = mid
        return lo - 1


sol = Solution2()
tests = [
    ([1,2,4,5,0], 1, 2, 5),
    ([4,4,4,4], 0, 3, 4),
    ([2,10,12,3], 0, 14, 9),
    ([48,16,29,41,2,43,23], 5, 40, 194),
    ([37,80,31,64,41,7,58,40,49], 0, 7, 14),
    ([57,70,35,30,29,13,17,88,89,49], 1, 90, 138),
]

for i, (stations, r, k, ans) in enumerate(tests):
    res = sol.maxPower(stations, r, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
