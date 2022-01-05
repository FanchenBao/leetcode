# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """LeetCode 1010
        
        Find the remainders for all time, and match the two remainders that add
        up to 60.

        O(N), 240 ms, 46% ranking
        """
        rems = Counter(t % 60 for t in time)
        res = 0
        for r in range(31):
            if r == 30 or r == 0:
                res += rems[r] * (rems[r] - 1) // 2
            else:
                res += rems[r] * rems[60 - r]
        return res


sol = Solution()
tests = [
    ([30,20,150,100,40], 3),
    ([60, 60, 60], 3),
]

for i, (time, ans) in enumerate(tests):
    res = sol.numPairsDivisibleBy60(time)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
