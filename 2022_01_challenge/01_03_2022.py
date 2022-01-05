# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """LeetCode 997

        Town judge must be the person that is not in the first value of each
        trust element.

        Town judge must have n - 1 number of people trusting him/her.

        Thus, we use a counter to keep track of the number of people trusting
        potential town judges. And use a set to identify which people are not
        in the first value of each trust element. If there is one person that
        fits both requirement, he/she is the town judge.

        O(N), 712 ms, 91% ranking.
        """
        counter = Counter(t for _, t in trust)
        people = set(range(1, n + 1))
        for p, _ in trust:
            if p in people:
                people.remove(p)
        for p in people:  # potential town judges
            if counter[p] == n - 1:
                return p
        return -1


class Solution2:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """Inspired by https://leetcode.com/problems/find-the-town-judge/discuss/1663344/C%2B%2BJavaPython3Javascript-Everything-you-need-to-know-from-start-to-end-.

        Think of the town judge as the person with n - 1 indegrees. Since there
        are only one town judge, there should only one node with n - 1
        indegrees.

        Also very important is to decrement indegrees if a person trusts
        someone else. This prevents the case where a person with n - 1
        indegrees also trust other people. He/she shall not be the town judge.
        
        """
        indegrees = [0] * (n + 1)
        for a, b in trust:
            indegrees[a] -= 1
            indegrees[b] += 1
        for i in range(1, n + 1):
            if indegrees[i] == n - 1:
                return i
        return -1


sol = Solution2()
tests = [
    (2, [[1, 2]], 2),
    (3, [[1, 3], [2, 3]], 3),
    (3, [[1,3],[2,3],[3,1]], -1),
]

for i, (n, trust, ans) in enumerate(tests):
    res = sol.findJudge(n, trust)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
