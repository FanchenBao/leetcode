# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution1:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """LeetCode 210

        We create two "adjacency list". One is for the graph, where prereq goes
        to the next course. The other records a set of prereqs to take a
        certain course. We DFS on the graph, but the condition for continuing
        the DFS is when a course's prereqs have all been fulfilled. After the
        DFS finishes, one last trick is to check whether any course has not
        been taken. The sign that a course has not been taken is that it still
        has prereqs not removed.

        O(N^2) for worst case. 104 ms, 44% ranking.
        """
        graph = {c: [] for c in range(numCourses)}
        prereqs = {c: set() for c in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            prereqs[course].add(prereq)
        res = []
        roots = [c for c, p in prereqs.items() if len(p) == 0]

        def dfs(cur: int, par: int) -> None:
            if par >= 0:
                prereqs[cur].remove(par)
            if len(prereqs[cur]) != 0:
                return
            res.append(cur)
            for nex in graph[cur]:
                dfs(nex, cur)

        for r in roots:
            dfs(r, -1)
        return res if all(len(p) == 0 for p in prereqs.values()) else []


class Solution2:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """This is a better version of graph traversal using BFS. Reference is
        my previous solution back in July 2020.

        This one is faster because we do not have to handle set.
        88 ms, 98% ranking.
        """
        # use one dict to handle both in and out edges
        graph = {'in': defaultdict(int), 'out': defaultdict(list)}
        for course, prereq in prerequisites:
            graph['in'][course] += 1
            graph['out'][prereq].append(course)
        queue = [c for c in range(numCourses) if not graph['in'][c]]
        res = []
        while queue:
            temp = []
            for c in queue:
                res.append(c)
                for nex in graph['out'][c]:
                    graph['in'][nex] -= 1
                    if graph['in'][nex] == 0:
                        temp.append(nex)
            queue = temp
        return res if sum(graph['in'][c] for c in range(numCourses)) == 0 else []


sol = Solution2()
tests = [
    (2, [[1,0]], [0, 1]),
    (4, [[1,0],[2,0],[3,1],[3,2]], [0,1,2,3]),
    (1, [], [0]),
    (3, [[1,0],[1,2],[0,1]], []),
]

for i, (numCourses, prerequisites, ans) in enumerate(tests):
    res = sol.findOrder(numCourses, prerequisites)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
