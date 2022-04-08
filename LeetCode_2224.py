# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        """Greedy

        O(1), 48 ms, 43% ranking.
        """
        cuh, cum = int(current[:2]), int(current[3:])
        coh, com = int(correct[:2]), int(correct[3:])
        if cum > com:
            com += 60
            coh -= 1
        r = (coh - cuh) * 60 + com - cum
        res = 0
        for t in [60, 15, 5, 1]:
            q, r = divmod(r, t)
            res += q
        return res

        
sol = Solution()
tests = [
    ('02:30', '04:35', 3),
    ('11:00', '11:01', 1),
    ('11:00', '11:00', 0),
    ('01:50', '02:10', 2),
]

for i, (current, correct, ans) in enumerate(tests):
    res = sol.convertTime(current, correct)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
