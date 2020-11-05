# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        """63% ranking. This is an easy question. All chips on even (or odd)
        positions can move to one even (or odd) position without any cost. Then
        we just need to move the all-even (or all-odd) coins to the all-odd
        (or all-even) position. Since these two positions can be arbitrarily
        decided, we can make them adjacent. This makes the final cost the
        smaller of the number of chips on the all-even and all-odd positions.
        """
        odd_sum = even_sum = 0
        for p in position:
            if p % 2:
                odd_sum += 1
            else:
                even_sum += 1
        return min(odd_sum, even_sum)


sol = Solution()
tests = [
    ([1, 2, 3], 1),
    ([2, 2, 2, 3, 3], 2),
    ([1, 1000000000], 1),
]

for i, (position, ans) in enumerate(tests):
    res = sol.minCostToMoveChips(position)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
