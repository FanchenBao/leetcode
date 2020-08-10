#! /usr/bin/env python3
from typing import List
from random import randint

"""08/16/2019

Solution1:
Basic DP solution, with O(n^3) complexity. It feels like a more mathematical
approach is available, as this solution clocked in at 728 ms (37%) while the
best solution only took less than 100 ms.

Solution2:
Improvement on Solution1. No need to iterate through all possible options for
j - 1 dices. For each dp[i][j], we know that its value is the sum of possibilites
when j - 1 dices take i - 1, i - 2, ..., i - min(i, f). We also know that
dp[i - 1][j] is the sum of possibilities when j - 1 dices take i - 2, i - 3,
..., i - min(i, f), i - 1 - min(i - 1, f). Thus we have
dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] - dp[i - min(i - 1, f) - 1][j - 1]

Proof:
When f > i - 1 and f >= i, i - min(i, f) and i - 1 - min(i - 1, f) are both 0,
and we know all values on row 0 is 0, so the expression above is correct.
When f <= i - 1 and f < i, i - min(i, f) = i - f, i - 1 - min(i - 1, f) =
i - f - 1, so the expression above is correct as well.

Solution2 clocked at 172 ms and 89%.
"""


class Solution1:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # row: target value, col: number of dices
        dp: List[List[int]] = [[0] * (d + 1) for _ in range(target + 1)]
        for i in range(1, f + 1):
            if i <= target:
                dp[i][1] = 1
            else:
                break
        for j in range(2, d + 1):
            for i in range(1, target + 1):
                # max and min value the other j - 1 dices can take
                max_val, min_val = i - 1, i - min(i, f)
                dp[i][j] = sum(
                    dp[k][j - 1] for k in range(min_val, max_val + 1)
                )
        return dp[target][d] % (10 ** 9 + 7)


class Solution2:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # row: target value, col: number of dices
        dp: List[List[int]] = [[0] * (d + 1) for _ in range(target + 1)]
        for i in range(1, f + 1):
            if i <= target:
                dp[i][1] = 1
            else:
                break
        for j in range(2, d + 1):
            for i in range(j, target + 1):
                dp[i][j] = (
                    dp[i - 1][j - 1]
                    + dp[i - 1][j]
                    - dp[i - min(i - 1, f) - 1][j - 1]
                )
        # for row in dp:
        #     print(row)
        return dp[target][d] % (10 ** 9 + 7)


def test():
    sol = Solution1()
    # test case 1
    d, f, target = 1, 6, 3
    if sol.numRollsToTarget(d, f, target) == 1:
        print(f"Test case 1: Pass")
    else:
        print(
            f"Test case 1: Fail, wrong answer {sol.numRollsToTarget(d, f, target)}"
        )

    # test case 2
    d, f, target = 2, 6, 7
    if sol.numRollsToTarget(d, f, target) == 6:
        print(f"Test case 2: Pass")
    else:
        print(
            f"Test case 2: Fail, wrong answer {sol.numRollsToTarget(d, f, target)}"
        )

    # test case 3
    d, f, target = 2, 5, 10
    if sol.numRollsToTarget(d, f, target) == 1:
        print(f"Test case 3: Pass")
    else:
        print(
            f"Test case 3: Fail, wrong answer {sol.numRollsToTarget(d, f, target)}"
        )

    # test case 4
    d, f, target = 1, 2, 3
    if sol.numRollsToTarget(d, f, target) == 0:
        print(f"Test case 4: Pass")
    else:
        print(
            f"Test case 4: Fail, wrong answer {sol.numRollsToTarget(d, f, target)}"
        )

    # test case 5
    d, f, target = 30, 30, 500
    if sol.numRollsToTarget(d, f, target) == 222616187:
        print(f"Test case 5: Pass")
    else:
        print(
            f"Test case 5: Fail, wrong answer {sol.numRollsToTarget(d, f, target)}"
        )


def compare_sol():
    T = 100
    for _ in range(T):
        d, f = 30, 30
        target = randint(1, d * f)
        sol1 = Solution1()
        sol2 = Solution2()
        if sol1.numRollsToTarget(d, f, target) != sol2.numRollsToTarget(
            d, f, target
        ):
            print(d, f, target)


def individual_test():
    d, f, target = 3, 6, 8
    sol1 = Solution1()
    print(sol1.numRollsToTarget(d, f, target))
    sol2 = Solution2()
    print(sol2.numRollsToTarget(d, f, target))


# test()
# individual_test()
compare_sol()
