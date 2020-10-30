# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """82% ranking

        Find the pos of all seats taken.

        find the middle point between two taken seats. If there are even number
        of seats in between, take the one to the left of the middle. The max
        mininum distance is the middle seat index minus the left seat index.

        Add the scenario for taking a seat before the first or after the last
        person.

        Find the max of these three scenarios.
        """
        sit_pos = [i for i, v in enumerate(seats) if v]
        inter_dists = [(p2 - p1) // 2 for p1, p2 in zip(sit_pos, sit_pos[1:])]
        return max(inter_dists + [sit_pos[0], len(seats) - sit_pos[-1] - 1])


sol = Solution()
tests = [
    ([1, 0, 0, 0, 1, 0, 1], 2),
    ([1, 0, 0, 0], 3),
    ([0, 1], 1),
    ([1, 0, 0, 1], 1),
    ([1, 1, 0, 1, 1], 1),
]

for i, (seats, ans) in enumerate(tests):
    res = sol.maxDistToClosest(seats)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
