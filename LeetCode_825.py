# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right, bisect_left
from collections import Counter


class Solution1:
    def numFriendRequests(self, ages: List[int]) -> int:
        """A few edge cases. One is to handle repeated ages. This solution uses
        a counter to obtain the number of repeats. If a person is old enough,
        he/she can send friend reques to anyone of the same age. Another edge
        case is the requirement that the target must be older than a / 2 + 7.
        This actually gives us a minimum age that is allowed to send friend
        request: 14 + 1 = 15. Thus, anyone younger or equal to 14 years old
        cannot send friend request.

        O(NlogN), 683 ms, 28% ranking.
        """
        counter = Counter(ages)
        ages.append(0)
        ages.sort()
        res = 0
        for i in range(len(ages) - 1, 0, -1):
            a = a
            if a <= 14:
                break
            res += counter[a] - 1
            idx1 = bisect_right(ages, a / 2 + 7)
            idx2 = bisect_left(ages, a) - 1
            res += (idx2 - idx1 + 1)
        return res


class Solution2:
    def numFriendRequests(self, ages: List[int]) -> int:
        """No binary search. Courtesy of lee215

        Ref: https://leetcode.com/problems/friends-of-appropriate-ages/discuss/127029/C%2B%2BJavaPython-Easy-and-Straight-Forward

        This is O(N^2), but it is much faster than binary search, because the
        size of the counter is very small (at most 120)
        381 ms, faster than 91.11%
        """
        counter = Counter(ages)
        res = 0
        for a in counter:
            for b in counter:
                if b > a / 2 + 7 and b <= a:
                    res += (counter[a] * counter[b]) if a != b else (counter[a] * (counter[a] - 1))
        return res


sol = Solution2()
tests = [
    ([16,16], 2),
    ([16,17,18], 2),
    ([20,30,100,110,120], 3),
    ([108,115,5,24,82], 3),
    ([8,85,24,85,69], 4),
]

for i, (ages, ans) in enumerate(tests):
    res = sol.numFriendRequests(ages)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
