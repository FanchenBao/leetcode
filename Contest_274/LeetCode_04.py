# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
import heapq


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        adj = {i: f for i, f in enumerate(favorite)}
        # anchors[a] = [{p: n}] 
        # for anchor a, it has one group of people that leads to a. For each
        # person in the group p, there are n people between p and the anchor
        anchors = defaultdict(list)
        self.res = 0

        def helper(head: int) -> None:
            pre, cur = -1, head
            pos, i = {}, 0
            while cur in adj:
                pos[cur] = i
                pre = cur
                cur = adj[cur]
                del adj[pre]
                i += 1
            total = i
            i -= 1  # i is the pos of the last node in the chain
            if cur in pos:
                if pos[cur] == i - 1:  # anchor found to be pre
                    anchors[pre].append({})
                    for node, j in pos.items():
                        anchors[pre][-1][node] = total - j
                else:  # circular
                    self.res = max(self.res, i - pos[cur] + 1)
            elif cur in anchors:  # cur is an anchor point
                anchors[cur].append({cur: 1})
                for node, j in pos.items():
                    anchors[cur][-1][node] = total - j + 1
            else:
                for a, groups in anchors.items():
                    for i, g in enumerate(groups):
                        if cur in g:  # cur can lead to anchor a with group g
                            for node, j in pos.items():
                                g[node] = total - j + g[cur]

        for i in range(len(favorite)):
            if i in adj:
                helper(i)
        sum_len = 0  # all paths in anchors can be concated
        for groups in anchors.values():
            if len(groups) == 1:
                sum_len += max(groups[0].values())
            else:
                longests = sorted([max(g.values()) for g in groups])
                sum_len += longests[-1] + longests[-2] - 1
        return max(self.res, sum_len)


sol = Solution()
tests = [
    ([2,2,1,2], 3),
    ([1,2,0], 3),
    ([3,0,1,4,1],4),
    ([1,0,0,2,1,4,7,8,9,6,7,10,8], 6),
    ([1,0,3,2,5,6,7,4,9,8,11,10,11,12,10], 11),
    ([7,0,7,13,11,6,8,5,9,8,9,14,15,7,11,6], 11),
]

for i, (favorite, ans) in enumerate(tests):
    res = sol.maximumInvitations(favorite)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
