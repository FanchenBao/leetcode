# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        """I had one wrong answer. The check for whether a player loses exactly
        once shall happen on the set of all losers. And this check must happen
        before the set of all losers is updated.

        O(N), 2217 ms, 84% ranking.
        """
        losers, loseonce, winners = set(), set(), set()
        for w, l in matches:
            if l not in losers:
                loseonce.add(l)
            elif l in loseonce:
                loseonce.remove(l)
            losers.add(l)
            winners.add(w)
        return [sorted(winners - losers), sorted(loseonce)]


sol = Solution()
tests = [
    ([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]], [[1,2,10],[4,5,7,8]]),
    ([[2,3],[1,3],[5,4],[6,4]], [[1,2,5,6],[]]),
    ([[1,5],[2,5],[2,8],[2,9],[3,8],[4,7],[4,9],[5,7],[6,8]], [[1,2,3,4,6],[]]),
]

for i, (matches, ans) in enumerate(tests):
    res = sol.findWinners(matches)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
