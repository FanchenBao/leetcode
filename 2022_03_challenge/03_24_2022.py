# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """LeetCode 881

        Greedy. Sort people, and try to pair the heaviest with the lightest
        at all times. If pairing is not possible, the heavy person must take
        a boat by him/herself.

        O(NlogN), 561 ms, 60% ranking.
        """
        people.sort()
        res = 0
        lo, hi = 0, len(people) - 1
        while lo <= hi:
            if people[hi] + people[lo] <= limit:
                lo += 1
            res += 1
            hi -= 1
        return res
        

sol = Solution()
tests = [
    ([1, 2], 3, 1),
    ([3, 2, 2, 1], 3, 3),
    ([3, 5, 3, 4], 5, 4),
]

for i, (people, limit, ans) in enumerate(tests):
    res = sol.numRescueBoats(people, limit)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
