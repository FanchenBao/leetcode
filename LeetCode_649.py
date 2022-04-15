# from pudb import set_trace; set_trace()
from typing import List
from itertools import groupby
from collections import deque


class Solution1:
    def predictPartyVictory(self, senate: str) -> str:
        """This solution is WRONG, but it passed OJ. This means the OJ has a
        weak set of test cases. The test case that fails this solution is

        "RDRDRDDRDRDRDRDRRDRDRDRDRDRDDDDRRDRDRDRDRDRDRDRRRRRDRDRDRDRDDDDDRDRDRDRDRDRDRDRRDRDRDRDRDRDRRDRDRDRDRDRDRDRDRRDRDRDRDRDRRD"

        I will report to LeetCode this issue
        """
        l = [[k, len(list(g))] for k, g in groupby(senate)]
        while len(l) > 1:
            temp = deque([l[0]])
            cur_act = l[0][1]
            for i in range(1, len(l)):
                if l[i][0] == temp[-1][0]:
                    temp[-1][1] += l[i][1]
                    cur_act += l[i][1]
                else:
                    if cur_act >= l[i][1]:
                        cur_act -= l[i][1]
                    else:
                        temp.append(l[i])
                        l[i][1] -= cur_act
                        cur_act = l[i][1]
            act = temp.pop()
            # If possible, always ban the enemy at the front, because whoever
            # is at the front has advantage (they can always ban other people
            # while they themselves won't get banned in this algorithm)
            if temp and temp[0][0] != act[0]:
                if temp[0][1] <= cur_act:
                    cur_act -= temp.popleft()[1]
                else:
                    temp[0][1] -= cur_act
                    cur_act = 0
            while temp and cur_act:
                if temp[-1][0] == act[0]:
                    act[1] += temp.pop()[1]
                else:
                    if cur_act >= temp[-1][1]:
                        cur_act -= temp.pop()[1]
                    else:
                        temp[-1][1] -= cur_act
                        cur_act = 0
            if temp and temp[-1][0] == act[0]:
                temp[-1][1] += act[1]
            else:
                temp.append(act)
            l = temp
        return 'Radiant' if l[0][0] == 'R' else 'Dire'


class Solution2:
    def predictPartyVictory(self, senate: str) -> str:
        """This solution comes from the discussion.

        Ref: https://leetcode.com/problems/dota2-senate/discuss/105858/JavaC%2B%2B-Very-simple-greedy-solution-with-explanation

        The idea is something I have thought about but wasn't able to implement
        easily. The rule is that each senate bans the first enemy to its right.
        When we reach the last senator, loop back to the front.

        The implementation is two queues.

        50 ms, 97% ranking.
        """
        n = len(senate)
        rs = deque(i for i, s in enumerate(senate) if s == 'R')
        ds = deque(i for i, s in enumerate(senate) if s == 'D')
        while len(rs) and len(ds):
            ri, di = rs.popleft(), ds.popleft()
            if ri < di:  # R can ban the next D
                rs.append(ri + n)  # genius move
            else:
                ds.append(di + n)
        return 'Radiant' if rs else 'Dire'


sol = Solution2()
tests = [
    ('RD', 'Radiant'),
    ('RDD', 'Dire'),
    ('RRDDD', 'Radiant'),
    ('RRDRDRDRDRDDRDRDRDDRRDRDRDRDRDRDRDRDRDRDRDRDDRDRDRRRDRDRDR', 'Radiant'),
    ('RRRR', 'Radiant'),
    ('DDDD', 'Dire'),
    ("RDDRRRRDRDDRDDDDRDRD", 'Dire'),
    ("RDRDRDDRDRDRDRDRRDRDRDRDRDRDDDDRRDRDRDRDRDRDRDRRRRRDRDRDRDRDDDDDRDRDRDRDRDRDRDRRDRDRDRDRDRDRRDRDRDRDRDRDRDRDRRDRDRDRDRDRRD", "Radiant"),
]

for i, (senate, ans) in enumerate(tests):
    res = sol.predictPartyVictory(senate)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
