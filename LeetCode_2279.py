# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        """We can use greedy. Always fulfill the bag with the least number of
        rocks to add. Continue until we don't have any more rocks.

        O(N), 1178 ms, faster than 74.85%
        """
        s, c = 0, 0
        for d in sorted(c - r for c, r in zip(capacity, rocks)):
            s += d
            if s > additionalRocks:
                break
            c += 1
        return c


sol = Solution()
tests = [
    ([2,3,4,5], [1,2,4,4], 2, 3),
    ([10,2,2], [2,2,0], 100, 3),
]

for i, (capacity, rocks, additionalRocks, ans) in enumerate(tests):
    res = sol.maximumBags(capacity, rocks, additionalRocks)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
