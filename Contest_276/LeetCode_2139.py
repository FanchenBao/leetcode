# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target > 1:
            if target % 2:
                target -= 1
            elif maxDoubles:
                target //= 2
                maxDoubles -= 1
            else:
                return res + target - 1
            res += 1
        return res


sol = Solution()
tests = [
    (5, 0, 4),
    (19, 2, 7),
    (10, 4, 4),
]

for i, (target, maxDoubles, ans) in enumerate(tests):
    res = sol.minMoves(target, maxDoubles)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
