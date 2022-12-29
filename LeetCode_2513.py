# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        """I was correct that the idea should be binary search, but the initial
        implementation was not correct. The current implementation breaks down
        the number of values that we can take from 1 to mid into four categories

        1. cannot be taken by either d1 or d2 (non_d1d2)
        2. can be taken by d1 but not by d2 (non_d2)
        3. can be taken by d2 but not by d1 (non_d1)
        4. can be taken by both (both)

        These counts can be computed by using division and LCM of d1 and d2.

        To maximize the use of the availables, we want all the values not
        divisible by d1 come from non_d2, and both if necessary. If that is
        possible, we can continue check if the remaining availables are able to
        supply uniqueCnt2.

        Similarly, we can handle all the values not divisible by d2 first, and
        see if the remaining availables are able to supply uniqueCnt1.

        Then we can build binary search on top of this. The max high is double
        of uniqueCnt1 + uniqueCnt2, which happens when d1 = d2 = 2.

        At each step, we check if going with d1 first or d2 first works. As long
        as one of them works, we can shrink. If neither works, we expand.

        O(log(C1 + C2)), 30 ms, faster than 74.35%
        """
        lcm = divisor1 * divisor2 // math.gcd(divisor1, divisor2)
        lo, hi = 1, 2 * (uniqueCnt1 + uniqueCnt2) + 1
        while lo < hi:
            mid = (lo + hi) // 2
            non_d1d2 = mid // lcm
            non_d1 = mid // divisor1 - non_d1d2
            non_d2 = mid // divisor2 - non_d1d2
            both = mid - non_d1d2 - non_d1 - non_d2
            # fill up d1 first, check whether there is enough for d2
            cap_d1 = non_d2 + both
            cap_d2 = non_d1 + both - max(uniqueCnt1 - non_d2, 0)
            is_good_1 = cap_d1 >= uniqueCnt1 and cap_d2 >= uniqueCnt2
            # fill up d2 first, check whether there is enough for d1
            cap_d2 = non_d1 + both
            cap_d1 = non_d2 + both - max(uniqueCnt2 - non_d1, 0)
            is_good_2 = cap_d1 >= uniqueCnt1 and cap_d2 >= uniqueCnt2
            if is_good_1 or is_good_2:
                hi = mid
            else:
                lo = mid + 1
        return lo


class Solution2:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        """Better binary search implementation

        Ref: https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/discuss/2946508/Python-LCM-and-binary-search-(explained)-%2B-BONUS-ONE-LINER

        O(log(C1 + C2), 29 ms, faster than 79.20%
        """
        lcm = divisor1 * divisor2 // math.gcd(divisor1, divisor2)
        lo, hi = 1, 2 * (uniqueCnt1 + uniqueCnt2) + 1
        while lo < hi:
            mid = (lo + hi) // 2
            cap_d1 = mid - mid // divisor1
            cap_d2 = mid - mid // divisor2
            cap_d1d2 = mid - mid // lcm
            if cap_d1 >= uniqueCnt1 and cap_d2 >= uniqueCnt2 and cap_d1d2 >= uniqueCnt1 + uniqueCnt2:
                hi = mid
            else:
                lo = mid + 1
        return lo


class Solution3:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        """Find the max value if we only consider d1 and c1. Max value if we
        only consider d2 and c2. Max value if we consider both d1 and d2, c1 and
        c2. Take the max among the three.

        Ref: https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/discuss/2947014/Formula
        """
        
        def get_max(d: int, c: int) -> int:
            """The smallest max value if we want to take c number of values not divisible by d"""
            q, r = divmod(c, d - 1)
            return c + q - int(r == 0)

        return max([
            get_max(divisor1, uniqueCnt1),
            get_max(divisor2, uniqueCnt2),
            get_max(divisor1 * divisor2 // math.gcd(divisor1, divisor2), uniqueCnt1 + uniqueCnt2)
        ])


sol = Solution3()
tests = [
    (2, 7, 1, 3, 4),
    (3, 5, 2, 1, 3),
    (2, 4, 8, 2, 15),
    (16, 14, 12, 8, 20),
]

for i, (divisor1, divisor2, uniqueCnt1, uniqueCnt2, ans) in enumerate(tests):
    res = sol.minimizeSet(divisor1, divisor2, uniqueCnt1, uniqueCnt2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
