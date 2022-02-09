# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:
        """Nothing special here. Just follow the instructions.

        62 ms, 18% ranking.
        """
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(d) * int(d) for d in str(n))
        return n == 1

        
sol = Solution()
tests = [
    (19, True),
    (2, False),
]

for i, (n, ans) in enumerate(tests):
    res = sol.isHappy(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
