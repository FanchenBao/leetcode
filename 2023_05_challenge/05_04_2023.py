# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import deque


class Solution1:
    def predictPartyVictory(self, senate: str) -> str:
        """LeetCode 649

        Greedy. Each round, the senator bans the next closest senator of the
        opposite party.

        O(N^2), 91 ms, faster than 32.11%
        """
        N = len(senate)
        count_r = senate.count('R')
        count_d = N - count_r
        lst = list(senate)
        r = d = 0
        while count_r and count_d:
            while lst[d % N] != 'D':
                d += 1
            while lst[r % N] != 'R':
                r += 1
            if r < d:
                lst[d % N] = ''
                count_d -= 1
                r += 1
            else:
                lst[r % N] = ''
                count_r -= 1
                d += 1
        return 'Radiant' if count_r else 'Dire'


class Solution2:
    def predictPartyVictory(self, senate: str) -> str:
        """Using deque to implement the wrap-around. Very genius solution from
        the discussion.

        O(N^2), 71 ms, faster than 47.40%
        """
        N = len(senate)
        rd = deque(i for i, s in enumerate(senate) if s == 'R')
        dd = deque(i for i, s in enumerate(senate) if s == 'D')
        while rd and dd:
            ri = rd.popleft()
            di = dd.popleft()
            if ri < di:
                rd.append(ri + N)
            else:
                dd.append(di + N)
        return 'Radiant' if rd else 'Dire'


sol = Solution2()
tests = [
    ("RD", "Radiant"),
    ("RDD", "Dire"),
    ('RDRDDR', 'Radiant'),
    ('RDDDRDRR', 'Dire'),
]

for i, (senate, ans) in enumerate(tests):
    res = sol.predictPartyVictory(senate)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
