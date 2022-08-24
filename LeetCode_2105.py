# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        """Weird problem. Just follow the instruction.

        1061 ms, faster than 77.33%
        """
        res = 0
        i, j = 0, len(plants) - 1
        a, b = capacityA, capacityB
        while i < j:
            if a < plants[i]:
                a = capacityA
                res += 1
            a -= plants[i]
            i += 1
            if b < plants[j]:
                b = capacityB
                res += 1
            b -= plants[j]
            j -= 1
        if i == j and ((a >= b and a < plants[i]) or (a < b and b < plants[j])):
            res += 1
        return res


sol = Solution()
tests = [
    ([2,2,3,3], 5, 5, 1),
    ([2,2,3,3], 3, 4, 2),
    ([5], 10, 8, 0),
]

for i, (plants, capacityA, capacityB, ans) in enumerate(tests):
    res = sol.minimumRefill(plants, capacityA, capacityB)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
