# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        """No need to dynamic programming or sliding window. It is straigt-
        forward programming. The key insight is that each consecutive number of
        cards that contain a pair must have the pair at the start and end of
        the cards to make it minimum length. Hence, all we need to do is to
        find the smallest difference among consecutive pairs of indices that
        belong to the same element.

        O(N), 1140 ms, faster than 58.98%
        """
        indices = defaultdict(list)
        res = len(cards) + 1
        for i, c in enumerate(cards):
            indices[c].append(i)
        for ids in indices.values():
            if len(ids) > 1:
                res = min(res, min(ids[i] - ids[i - 1] + 1 for i in range(1, len(ids))))
        return res if res < len(cards) + 1 else -1


sol = Solution()
tests = [
    ([3,4,2,3,4,7], 4),
    ([1,0,5,3], -1),   
]

for i, (cards, ans) in enumerate(tests):
    res = sol.minimumCardPickup(cards)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
