# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        """My idea is to always pour water from the big jug to the small jug.
        Record the state after each pour and see if the target capacity can be
        reached at any state. This process will definitely circle back to the
        original state. And that's when we quit the check.

        O((M // N + 1) * (M % N + 1)), 512 ms, 44% ranking.
        """
        seen = set()
        j1, j2 = min(jug1Capacity, jug2Capacity), max(jug1Capacity, jug2Capacity)
        if targetCapacity > j1 + j2:
            return False
        p1, p2 = 0, 0  # current state of how much water each jug holds
        while not (p1, p2) in seen:
            seen.add((p1, p2))
            if p2 > 0:
                if p1 == j1:
                    p1, p2 = (j1, p2 - j1) if p2 >= j1 else (p2, 0)
                else:
                    mm = j1 - p1  # max moveable to j1
                    p1, p2 = (j1, p2 - mm) if p2 >= mm else (p1 + p2, 0)
            elif p2 == 0:
                p2 = j2
            if targetCapacity in [p1, p2, p1 + p2]:
                return True
        return False     


class Solution2:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        """This is the GCD solution.

        Ref: https://leetcode.com/problems/water-and-jug-problem/discuss/159226/python-O(n)-time-O(1)-space...gcd-based-solution-with-explanation

        32 ms, 77% ranking.

        IF target is possible, then t = a * j1 + b * j2. According to Bézout
        Identity (https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity),
        any value of the form a * j1 + b * j2 must be a multiple of gcd(j1, j2).
        Thus, we can check whether t divides gcd(j1, j2) to know whether it is
        feasible to create t from j1 and j2.
        """
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        if targetCapacity in [jug1Capacity, jug2Capacity, jug1Capacity + jug2Capacity]:
            return True
        return targetCapacity % math.gcd(jug1Capacity, jug2Capacity) == 0



sol = Solution2()
tests = [
    (3, 5, 4, True),
    (2, 6, 5, False),
    (1, 2, 3, True),
]

for i, (j1, j2, tgt, ans) in enumerate(tests):
    res = sol.canMeasureWater(j1, j2, tgt)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
