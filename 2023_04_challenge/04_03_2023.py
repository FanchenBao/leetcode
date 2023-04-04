# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """LeetCode 881

        Greedy. Sort people. The idea is that the pair must have as close a
        total weight to limit as possible. This means for each low weight person
        he must pair with as heavy a high weight person as possible.

        Using two pointers, we can move the right pointer down until people[lo]
        + people[hi] <= limit. That is a valid pair. Then we move lo and hi
        both towards the center. If the sum is larger than limit, then the high
        weight person must take the boat by himself.

        O(NlogN), 459 ms, faster than 71.16%
        """
        people.sort()
        lo, hi = 0, len(people) - 1
        res = 0
        while lo < hi:
            if people[lo] + people[hi] > limit:
                res += 1
            else:
                res += 1
                lo += 1
            hi -= 1
        if lo == hi:
            res += 1
        return res


class Solution2:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """Simplified implementation
        """
        people.sort()
        lo, hi = 0, len(people) - 1
        res = 0
        while lo <= hi:
            if people[lo] + people[hi] <= limit:
                lo += 1
            res += 1
            hi -= 1
        return res


sol = Solution2()
tests = [
    ([1,2], 3, 1),
    ([3,2,2,1], 3, 3),
    ([3,5,3,4], 5, 4),
]

for i, (people, limit, ans) in enumerate(tests):
    res = sol.numRescueBoats(people, limit)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
