# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        """It is not a difficult problem IF the numbers chosen are replaceable.
        Now that it is not replaceable, I couldn't figure out a nice math
        scheme to work it out. The only other option is to brute force it.
        Basically, have the first person pick a number, and see what the result
        is when the second person picks all possible remaining numbers. If each
        choice the second person makes leads to the first person winning, then
        we have a strategy where the first person can force a win. Otherwise,
        the first person needs to choose another value.

        A naive way is to use a bucket list to record which value has been
        taken and which hasn't. This leads to TLE, as there are duplication in
        the state. Fortunately, there are at most 20 numbers to pick, and by
        reading the hint, I realized that we can use a bitmap to represent the
        current state of the remaining integers. Thus, we can use two integers
        to represent the state of the game: rem -> the remaining desired total
        and ava -> the available integers left as a bit map. We can memoize
        on these and make the solution faster.

        6136 ms, 14% ranking.

        UPDATE: from reading the discussion, I learn that the time complexity
        is O(2^n), where n = maxChoosableInteger. This basically means we
        compute each possible integer selection state at most once.

        The discussion also makes me realize that ava alone is enough as the
        state, because the remaining numbers to reach can be computed from
        ava. Thus, our state is a single integer.

        Also, I learned that if sum of the choosable integers is equal
        to the total, then first person always wins if maxChoosableInteger is
        odd.
        """
        if desiredTotal <= maxChoosableInteger:
            return True
        if desiredTotal == maxChoosableInteger + 1:
            return False
        s = (1 + maxChoosableInteger) * maxChoosableInteger // 2 
        if s < desiredTotal:
            return False
        if s == desiredTotal:
            return maxChoosableInteger % 2 == 1

        @lru_cache(maxsize=None)
        def dfs(ava: int, rem: int) -> bool:
            for i in range(1, maxChoosableInteger + 1):
                if (1 << i - 1) & ava:  # first person pick
                    if i >= rem:
                        return True
                    new_ava = ava ^ (1 << i - 1)
                    for j in range(1, maxChoosableInteger + 1):
                        if (1 << (j - 1)) & new_ava:  # second pick
                            if j >= rem - i or not dfs(new_ava ^ (1 << j - 1), rem - i - j):
                                # second person wins
                                break
                    else:
                        return True
            return False

        return dfs((1 << maxChoosableInteger) - 1, desiredTotal)


sol = Solution()
tests = [
    (10, 11, False),
    (10, 0, True),
    (10, 1, True),
    (1, 3, False),
    (2, 5, False),
    (3, 7, False),
    (4, 9, False),
    (5, 11, False),
    (6, 13, True),
    (7, 15, False),
    (8, 17, True),
    (9, 19, False),
    (10, 21, True),
    (18, 79, True),
]

for i, (maxChoosableInteger, desiredTotal, ans) in enumerate(tests):
    res = sol.canIWin(maxChoosableInteger, desiredTotal)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
