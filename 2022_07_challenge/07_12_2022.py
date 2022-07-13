# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter
from functools import lru_cache


class Solution1:

    def find_ways_to_make(self, counter: Counter, target: int) -> List[Counter]:
        sticks = [k for k, v in counter.items() for _ in range(v)]
        sticks.sort()
        res = []

        def knapsack(idx: int, tgt: int, knap: List[int]) -> None:
            if tgt == 0:
                res.append(Counter(knap))
            elif tgt > 0 and idx < len(sticks):
                knap.append(sticks[idx])  # take the current
                knapsack(idx + 1, tgt - sticks[idx], knap)
                knap.pop()
                knapsack(idx + 1, tgt, knap)  # do not take the current

        knapsack(0, target, [])
        return res

    def makesquare(self, matchsticks: List[int]) -> bool:
        """LeetCode 473

        My current solution is very convoluted. We use a backtrack for the main
        solver, and a knapsack for a helping solver. The main solver goes from
        the largest stick to the smallest. For each stick, we find how many
        more lengths are needed to make a side. Then we use knapsack to find
        different ways of using smaller sticks to make the difference. Then we
        try each way to see whether the main solver can return True. If none of
        the ways lead to a True, return False.

        O(N*2^N), 355 ms, faster than 78.44%
        """
        s = sum(matchsticks)
        side, r = divmod(s, 4)
        if r:
            return False
        counter = Counter(matchsticks)
        uniqs = sorted(counter, reverse=True)
        if uniqs[-1] > side:
            return False

        def helper(idx: int, counter: Counter) -> bool:
            if sum(counter.values()) == 0:
                return True
            while not counter[uniqs[idx]]:
                idx -= 1
            cur = uniqs[idx]
            counter[cur] -= 1
            if cur == side:
                return helper(idx, counter)
            for cc in self.find_ways_to_make(counter, side - cur):
                if helper(idx, counter - cc):
                    return True
            return False

        return helper(0, counter)


class Solution2:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """Backtracking with bitmask

        609 ms, faster than 69.39%
        """
        s = sum(matchsticks)
        N = len(matchsticks)
        side, r = divmod(s, 4)
        if r:
            return False
        if max(matchsticks) > side:
            return False

        @lru_cache(maxsize=None)
        def helper(state: int, num_sides_complete: int, tgt: int) -> bool:
            if tgt == 0:
                tgt = side
                num_sides_complete += 1
            if num_sides_complete == 3:
                return True
            for i in range(N, -1, -1):
                if (1 << i) & state and matchsticks[i] <= tgt:  # additional check
                    if helper(state ^ (1 << i), num_sides_complete, tgt - matchsticks[i]):
                        return True
            return False

        return helper((1 << N) - 1, 0, side)


sol = Solution2()
tests = [
    ([1,1,2,2,2], True),
    ([3,3,3,3,4], False),
    ([5,5,5,5,4,4,4,4,3,3,3,3], True),
]

for i, (matchsticks, ans) in enumerate(tests):
    res = sol.makesquare(matchsticks)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
