# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        """LeetCode 2136

        There will always be a plant to be planted the last. And its growTime
        will determine the total time needed for bloom. To reduce that, it is
        favorable to plant something with as short growTime as possible at the
        end. Meanwhile, we also don't want to waste time by just waiting for
        some growTime without planting anything. This means it is favorable to
        plant something that takes a long time to grow at the beginning. Thus,
        we have the first sort logic: sort growTime in reverse.

        If two growTimes are the same, we have a choice of which to plant first.
        Based on the previous principle of not wasting time, it is favorable
        to plant something with shorter plantTime first. This way, the longer
        plant time can coincide with the growTime of the previous plant. Hence,
        we have the second sort logic: sort plantTime ascending.

        After sorting, we just plant consecutively, and we have the answer.

        O(NlogN), 5173 ms, faster than 7.41%
        """
        res = 0
        plant_days = 0
        for p, g in sorted([(p, g) for p, g in zip(plantTime, growTime)], key=lambda tup: (-tup[1], tup[0])):
            plant_days += p
            res = max(res, plant_days + g + 1)
        return res - 1


class Solution2:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        """The hints give a new insight. We only need to sort growTime. If
        two flowers have the same growTime yet different plantTime, it doesn't
        matter which one to plant first. This is because the plant time in
        total would be the same regardless of order, and then the growTime of
        the last platned flower is also the same. Thus, we don't have to sort
        plantTime.

        Much faster, because we reduce the amount of sorting necessary.
        1732 ms, faster than 98.39% 

        UPDATE: the official solution provides a very nice proof of the greedy
        solution.
        """
        res = 0
        plant_days = 0
        for g, p in sorted([(g, p) for p, g in zip(plantTime, growTime)], reverse=True):
            plant_days += p
            res = max(res, plant_days + g + 1)
        return res - 1


sol = Solution2()
tests = [
    ([1,4,3], [2,3,1], 9),
    ([1,2,3,2], [2,1,2,1], 9),
    ([1], [1], 2)
]

for i, (plantTime, growTime, ans) in enumerate(tests):
    res = sol.earliestFullBloom(plantTime, growTime)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
