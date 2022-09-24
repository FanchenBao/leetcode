# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        """The idea is to use bit map to represent the current state of the
        cards that have not been taken. For the DP, we use (state, tgt) as the
        overall state, which tries to find whether we can use the cards
        remaining in state to reach the tgt.

        There are two rounds. First, we pick one card, and shove the remaining
        three cards to the next recursion. The possible next targts are
        tgt - v, v - tgt, tgt * v, tgt / v, and v / tgt. However, we must skip
        tgt / v and v / tgt when tgt == 0, because it is not possible to reach
        0 via multiplication given non-zero values.

        Second, we pick two cards, produce all possible values from the two
        cards, and shove the remaining two cards to the next recursion.
        Similarly, we must skip tgt / v1v2 and v1v2 / tgt when tgt * v1v2 == 0
        because the only situation where tgt == 0 and we have two cards to pick
        is when there are only two cards left. In that case, the only way to
        reach zero is via v1 - v2, not multiplication. Also, we have to skip
        v1v2 == 0, because when that happens, it is impossible to do
        multiplication with v1v2 to reach a tgt that is not zero. Therefore,
        for all multiplication, division operations, tgt * v1v2 cannot be zero.

        1679 ms, faster than 5.02%
        """
        lru_cache(maxsize=None)
        def dp(state: int, tgt: float) -> bool:
            if not state:
                return math.isclose(tgt, 0)
            # first round, keep one value, and try the rest
            for i in range(4):
                if state & (1 << i):
                    v = cards[3 - i]
                    next_state = state ^ (1 << i)
                    if any([
                        dp(next_state, tgt - v),
                        tgt != 0 and dp(next_state, tgt / v),
                        dp(next_state, tgt + v),
                        dp(next_state, v - tgt),
                        tgt != 0 and dp(next_state, v / tgt),
                    ]):
                        return True
            # second round, keep two values, and try the rest
            for i in range(4):
                for j in range(i + 1, 4):
                    if (state & (1 << i)) and (state & (1 << j)):
                        v1, v2 = cards[3 - i], cards[3 - j]
                        next_state = state ^ (1 << i) ^ (1 << j)
                        for v1v2 in set([v1 - v2, v2 - v1, v1 / v2, v2 / v1, v1 + v2, v1 * v2]):
                            if any([
                                dp(next_state, tgt - v1v2),
                                v1v2 * tgt != 0 and dp(next_state, tgt / v1v2),
                                dp(next_state, tgt + v1v2),
                                dp(next_state, v1v2 - tgt),
                                v1v2 * tgt != 0 and dp(next_state, v1v2 / tgt),
                            ]):
                                return True
            return False

        return dp(15, 24)

        

sol = Solution()
tests = [
    ([4,1,8,7], True),
    ([1,2,1,2], False),
    ([7, 8, 6, 8], False),
    ([9, 6, 5, 5], False),
]

for i, (cards, ans) in enumerate(tests):
    res = sol.judgePoint24(cards)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
