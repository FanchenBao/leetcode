# from pudb import set_trace; set_trace()
from typing import List, Tuple, Set
import math
from functools import lru_cache
from itertools import permutations


class Solution1:
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

        UPDATE: forgot to put '@' in front of lru_cache. Dumbass! After using
        lru_cache, run time decreases to 952 ms, faster than 5.61%
        """
        @lru_cache(maxsize=None)
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


class Solution2:
    def judgePoint24(self, cards: List[int]) -> bool:
        """This solution first permute all the cards. For each permutation, we
        find out all possible results. If 24 is in one of them, we return True.

        To find all possible results, we use a DP function that takes a tuple
        of values. The tupel represents that current cards under consideration,
        where the order matters. If we only have one or two cards, the possible
        outcome can be easily computed. If we have three or four cards, we can
        proceed like this:

        * isolate one card, and find all possible outcome of the remaining
        cards. Then for each outcome, we can compute four additional outcomes
        between it and the isolated card.

        * isolate two cards. Find all possible outcomes of the first two cards
        and all possible outcome of the remaining cards. Then for each outcome
        of the first two cards, and each outcome of the remaining cards, we can
        compute all additional outcomes.

        * isolate three cards, if possible. Find all possible outcomes of the
        first three cards, and then for each outcome, find all the outcome
        with the remaining one card

        Since we cache all the input tuples, the total number of computation is
        quite reasonable.

        95 ms, faster than 85.83% 
        """

        @lru_cache(maxsize=None)
        def dp(curr_cards: Tuple[int, ...]) -> Set[int]:
            if len(curr_cards) == 1:
                return curr_cards
            if len(curr_cards) == 2:
                v1, v2 = curr_cards
                return set([v1 + v2, v1 * v2, v1 - v2, v1 / v2])
            res = set()
            if len(curr_cards) == 4:
                for r in dp(curr_cards[:3]):
                    res.add(r + curr_cards[3])
                    res.add(r - curr_cards[3])
                    res.add(r * curr_cards[3])
                    res.add(r / curr_cards[3])
            for r in dp(curr_cards[1:]):
                res.add(curr_cards[0] + r)
                res.add(curr_cards[0] - r)
                res.add(curr_cards[0] * r)
                r != 0 and res.add(curr_cards[0] / r)
            for r1 in dp(curr_cards[:2]):
                for r2 in dp(curr_cards[2:]):
                    res.add(r1 + r2)
                    res.add(r1 - r2)
                    res.add(r1 * r2)
                    r2 != 0 and res.add(r1 / r2)
            return res

        for cards_arr in permutations(cards):
            for r in dp(tuple(cards_arr)):
                if math.isclose(r, 24):
                    return True
        return False


class Solution3:
    def judgePoint24(self, cards: List[int]) -> bool:
        """This is from Mr. Pochmann's solution.

        https://leetcode.com/problems/24-game/discuss/107675/Short-Python

        If we take the first two and produce an outcome, then we combine the
        outcome with the remaining two. In the next round of recursion, we will
        have three values. And since we permute these values, we will cover all
        operations: 1 <-> 3, 2 <-> 2, and 3 <-> 1

        Say c is the outcome of the first two cards. The next round is a
        permutation of c, v3, v4.

        (c, v3), v4 => 1 <-> 3 or 3 <-> 1 situation
        (c, v4), v3 => 1 <-> 3 or 3 <-> 1 situation
        (v3, v4), c => 2 <-> 2 situation
        """
        if len(cards) == 1:
            return math.isclose(cards[0], 24)
        for v1, v2, *rest in permutations(cards):
            for r in [v1 + v2, v1 - v2, v1 * v2, 0 if v2 == 0 else v1 / v2]:
                if self.judgePoint24([r, *rest]):
                    return True
        return False


sol = Solution3()
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
