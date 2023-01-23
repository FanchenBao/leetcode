# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution1:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """LeetCode 997

        Unbelievable. Got it wrong three times before scrambling together a
        passable solution. What the hell!

        O(N), 1041 ms, faster than 38.11%

        UPDATE: a more generic solution without having to explicitly considering
        the edge case.

        804 ms, faster than 48.09%
        """
        trustee_counter = Counter()
        truster = set()
        for a, b in trust:
            truster.add(a)
            trustee_counter[b] += 1
        judge = []
        for i in range(1, n + 1):
            if trustee_counter[i] == n - 1 and i not in truster:
                judge.append(i)
        if len(judge) != 1:
            return -1
        return judge[0]


class Solution2:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """Use indegrees. The town judge has indegree of n - 1. Also, for a
        truster, its indegree must decrement by 1

        O(N), 777 ms, faster than 61.95%
        """
        indegrees = [0] * (n + 1)
        for a, b in trust:
            indegrees[b] += 1
            indegrees[a] -= 1
        for i in range(1, n + 1):
            if indegrees[i] == n - 1:
                return i
        return -1



sol = Solution2()
tests = [
    (4, [[1,3],[1,4],[2,3],[2,4],[4,3]], 3),
    (3, [[1,2],[2,3]], -1),
    (1, [], 1),
]

for i, (n, trust, ans) in enumerate(tests):
    res = sol.findJudge(n, trust)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
