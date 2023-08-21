# from pudb import set_trace; set_trace()
from typing import List, Optional, Dict
import math
from collections import defaultdict, Counter


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        """LeetCode 1203 (Fail)

        The key idea is to use Topological Sort to " arrange a set of nodes with
        directed edges in a linear order, such that for every directed edge
        (u, v), node u appears before node v in the ordering." (I am copying
        from the official solution). This step is crucial to create order.

        I did not get topological sort. What I did get is to find order within
        each group, and find order among all the groups. For items without a
        group (i.e. group[i] == -1), I create new negative groups such that they
        all belong to their own groups. This way, we can order them however we
        want.

        Combined the two ideas, we have the solution. First, we order all the
        items using topological sort.

        Then we order all the groups by finding the graph with regard to the
        groups.

        Finally, we find the order of all the items within each group, and then
        return the items according to the order of their respective group.

        O(N^2), 374 ms, faster than 81.36%
        """
        # set all negative-grouped items to their own group
        g = -1
        for i in range(n):
            if group[i] < 0:
                group[i] = g
                g -= 1
        # create between group order
        before_group = {}
        for i in range(n):
            if group[i] not in before_group:
                before_group[group[i]] = set()
            for bi in beforeItems[i]:
                if group[bi] != group[i]:
                    before_group[group[i]].add(group[bi])

        def create_order(before_items: Dict) -> List[int]:
            """Use topological sort to find order

            The keys in before_items are the item itself, the value is a list
            or set of items before the key item
            """
            graph = defaultdict(list)
            indegrees = Counter()
            for i, bis in before_items.items():
                for bi in bis:
                    graph[bi].append(i)
                    indegrees[i] += 1
            queue = [i for i in before_items if indegrees[i] == 0]
            res = []
            while queue:
                res.extend(queue)
                tmp = []
                for i in queue:
                    for ni in graph[i]:
                        indegrees[ni] -= 1
                        if indegrees[ni] == 0:
                            tmp.append(ni)
                queue = tmp
            # if all there is no cycle, the resulting order shall have the same
            # number of nodes as the total number of nodes
            return res if len(res) == len(before_items) else []

        ordered_items = create_order({i: beforeItems[i] for i in range(n)})
        if not ordered_items:
            return []
        ordered_groups = create_order(before_group)
        if not ordered_groups:
            return []
        # create groups where all the items inside a group are ordered
        groups = defaultdict(list)
        for i in ordered_items:
            groups[group[i]].append(i)
        res = []
        for g in ordered_groups:
            res.extend(groups[g])
        return res


sol = Solution()
tests = [
    (8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3,6],[],[],[]], [6,3,4,1,5,2,0,7]),
    (8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3],[],[4],[]], []),
]

for i, (n, m, group, beforeItems, ans) in enumerate(tests):
    res = sol.sortItems(n, m, group, beforeItems)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
