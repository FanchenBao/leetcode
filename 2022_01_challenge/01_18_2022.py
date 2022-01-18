# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """LeetCode 605

        Very poor performance. Got wrong answer three times before passing the
        OJ. Last time I did this problem, which was 2020-12-05, I was able to
        pass in my first try. That said, the method used back then was not as
        bold as the one used here. The idea here is that given n empty spots
        between two planted spots, the max number of plants available is
        (n - 1) // 2. Given m empty spots from the beginning or towards the end
        i.e. only one side is blocked by a planted spot, the max number of
        plants available is n // 2. If there are no planted spots, i.e. there
        is no ones in the array, the max number of plants available is
        (n + 1) // 2.

        The tricky part for me is to identify the three conditions and evaluate
        them accordingly.

        The smart solution from more than a year ago was greedy, which says
        the best strategy to plant given two empty spaces is to always plant on
        the left. But I don't want to do the greedy today.

        O(N), 190 ms, 36% ranking.
        """
        pos = [i for i, f in enumerate(flowerbed) if f]
        if not pos:
            total = (len(flowerbed) + 1) // 2
        else:
            total = sum((r - l - 2) // 2 for l, r in zip(pos, pos[1:])) + pos[0] // 2 + (len(flowerbed) - pos[-1] - 1) // 2
        return n <= total 


sol = Solution()
tests = [
    ([1], 1, False),
    ([0], 1, True),
    ([1, 0, 0, 0, 1], 1, True),
    ([1, 0, 0, 0, 1], 2, False),
    ([1, 0, 0, 0, 0, 1], 2, False),
    ([0,0,1,0,1], 1, True),
]

for i, (flowerbed, n, ans) in enumerate(tests):
    res = sol.canPlaceFlowers(flowerbed, n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
