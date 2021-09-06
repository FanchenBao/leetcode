# from pudb import set_trace; set_trace()
from typing import List
from operator import sub


class Solution1:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        """LeetCode 1629

        A simple zip and sort shall surfice.

        O(NlogN), but technically we can do without sorting to find the longest
        key press. That said, since N is no longer than 1000, we can do O(NlogN)

        56 ms, 72% ranking

        UPDATE: we can use max(), it compares in the same manner as sort. With
        max, we reduce time complexity to O(N), 44 ms, 98% ranking.
        """
        return max((t1 - t2, keysPressed[i]) for i, (t1, t2) in enumerate(zip(releaseTimes, [0] + releaseTimes)))[1]


class Solution2:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        """From Mr. Pochmann

        Ref: https://leetcode.com/problems/slowest-key/discuss/985258/1-line-Python
        """
        return max(zip(map(sub, releaseTimes, [0] + releaseTimes), keysPressed))[1]


sol = Solution2()
tests = [
    ([9, 29, 49, 50], 'cbcd', 'c'),
    ([12, 23, 36, 46, 62], 'spuda', 'a'),
]

for i, (releaseTimes, keysPressed, ans) in enumerate(tests):
    res = sol.slowestKey(releaseTimes, keysPressed)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
