# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """LeetCode 849

        Find all the seats that are taken. The best place to sit is always
        between each consecutive pair of the taken seats. The tricky part is
        to consider the situation where there are empty seats starting or
        ending the row.

        O(N), 128 ms, 89% ranking.
        """
        ids = [i for i, s in enumerate(seats) if s]
        pot = [(r - l) // 2 for l, r in zip(ids, ids[1:])]
        return max(pot + [ids[0], len(seats) - 1 - ids[-1]])


sol = Solution()
tests = [
    ([1,0,0,0,1,0,1], 2),
    ([1,0,0,0], 3),
    ([0,1], 1),
    ([0,0,0,1], 3),
]

for i, (seats, ans) in enumerate(tests):
    res = sol.maxDistToClosest(seats)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
