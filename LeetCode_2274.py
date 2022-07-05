# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        """Not a difficult problem, but I got too cocky and overlooked quite a
        few details.

        O(NlogN), 1113 ms, faster than 34.41% 
        """
        special.sort()
        res = 0
        for i in range(1, len(special)):
            res = max(res, special[i] - special[i - 1] - 1)
        return max(res, special[0] - bottom, top - special[-1])


sol = Solution()
tests = [
    (2, 9, [4,6], 3),
    (6, 8, [7,6,8], 0),
    (1, 50, [12,24,38,48], 13),
    (6, 39, [38], 32),
]

for i, (bottom, top, special, ans) in enumerate(tests):
    res = sol.maxConsecutive(bottom, top, special)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
