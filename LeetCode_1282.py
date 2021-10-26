# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
from itertools import chain


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        """We use a dict to keep track of each group of a certain size. During
        iteration of groupSizes, if the current person can fit in the last
        group of dict[size], we add the person there. Otherwise, we create a
        new group within dict[size].

        O(N), 76 ms, 84% ranking.
        """
        groups = defaultdict(list)
        for i, g in enumerate(groupSizes):
            if groups[g] and len(groups[g][-1]) < g:
                groups[g][-1].append(i)
            else:
                groups[g].append([i])
        return list(chain(*(v for v in groups.values())))


sol = Solution()
tests = [
    ([3,3,3,3,3,1,3],[[5],[0,1,2],[3,4,6]]),
    ([2,1,3,3,3,2],[[1],[0,5],[2,3,4]]),
]

for i, (groupSizes, ans) in enumerate(tests):
    res = sol.groupThePeople(groupSizes)
    if sorted(res, key=lambda item: len(item)) == sorted(ans, key=lambda item: len(item)):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
