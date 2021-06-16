# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter
from functools import lru_cache


class Solution1:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """LeetCode 473

        The problem is harder than I had expected. It is easy to filter out
        all the trivial cases and obtain the side of the final square. Then
        the problem becomes to judge whether some combinations of the values in
        matchsticks can form four sums that equal to side.

        The current solution is backtracking. Basically we start from any value
        in matchsticks, and see if we can successfully contruct the square. If
        not, we backtrack on all of our previous decisions and try a new route.

        I don't know the time complexity for this. But we have runtime very
        slow, 3544 ms, 6% ranking.
        """
        # Trivial cases
        if len(matchsticks) < 4:
            return False
        total = sum(matchsticks)
        if total % 4:
            return False
        side = total // 4
        if max(matchsticks) > side:
            return False

        # Non-trivial case
        counter = Counter(matchsticks)

        def backtrack(cur_side, side_completed) -> bool:
            print(cur_side, side_completed, counter)
            if cur_side == 0:
                side_completed += 1
                if side_completed == 4:
                    return True
                if backtrack(side, side_completed):
                    return True
                return False
            for k, v in counter.items():
                if v > 0 and k <= cur_side:
                    counter[k] -= 1
                    if backtrack(cur_side - k, side_completed):
                        return True
                    counter[k] += 1
            return False

        return backtrack(side, 0)


class Solution2:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """Memoization in backtracking

        I am very proud of myself to have noticed that we can use bitmap to
        represent the state of which match stick has been used. This way, we can
        easily use lru_cache to memoize the scenarios that have been encountered
        before. The give-away is the max length of the matchsticks array being 15.

        O(N*2^N) where N is the length of matchsticks. But since N <= 15, the run
        time is very fast. 132 ms, 73% ranking.

        Update: from the official solution, we learned that as long as three
        sides have been fulfilled, we can immediately return True. So that
        shall help us save some more time (124 ms). Also, there are other
        solutions in the discussion that only use state as the argument of the
        backtracking. This one in particular is quite brilliant:

        https://leetcode.com/problems/matchsticks-to-square/discuss/1273708/Python-dp-on-subsets-explained
        """
        # Trivial cases
        N = len(matchsticks)
        if N < 4:
            return False
        total = sum(matchsticks)
        if total % 4:
            return False
        side = total // 4
        if max(matchsticks) > side:
            return False

        # Non-trivial case
        @lru_cache(maxsize=None)
        def backtrack(cur_side, side_completed, state) -> bool:
            if cur_side == 0:
                side_completed += 1
                if side_completed == 3 or backtrack(side, side_completed, state):
                    return True
                return False
            for i in range(N):
                if state & (1 << i) and matchsticks[i] <= cur_side:
                    if backtrack(cur_side - matchsticks[i], side_completed, state ^ (1 << i)):
                        return True
            return False

        return backtrack(side, 0, (1 << N) - 1)


sol = Solution2()
tests = [
    ([1, 1, 2, 2, 2], True),
    ([3, 3, 3, 3, 4], False),
    ([1, 2, 3, 4, 2, 3, 5], True),
    ([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3], True),
]

for i, (matchsticks, ans) in enumerate(tests):
    res = sol.makesquare(matchsticks)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
