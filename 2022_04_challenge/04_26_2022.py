# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
import heapq
import math


class DSU:
    """Disjoint Set Union.

    It supports union and find in log(N) time. It has rank and path compression.
    Shamelessly copied from:

    https://leetcode.com/problems/swim-in-rising-water/discuss/1284843/Python-2-solutions%3A-Union-FindHeap-explained

    Update 06/25/2021: Improved functionality by returning boolean value in
    self.union function. Reference:

    https://leetcode.com/problems/redundant-connection/solution/
    """

    def __init__(self, N: int):
        self.par = list(range(N))
        self.rnk = [0] * N

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        xr, yr = self.find(x), self.find(y)
        if xr != yr:
            if self.rnk[xr] < self.rnk[yr]:
                self.par[xr] = yr
            elif self.rnk[xr] > self.rnk[yr]:
                self.par[yr] = xr
            else:
                self.par[yr] = xr
                self.rnk[xr] += 1
            return True
        return False  # x, y already in the same union


class Solution1:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """LeetCode 1584

        Never done a minimum spanning tree before. So it is understandable
        that I cannot solve this.

        This is the Kruskal's Algo
        """
        dists = []
        N = len(points)
        for i in range(N):
            for j in range(i + 1, N):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dists.append((d, i, j))
        dists.sort()

        unionfind = DSU(N)
        res = 0
        num_edges = N - 1
        for d, i, j in dists:
            if unionfind.union(i, j):
                res += d
                num_edges -= 1
                if not num_edges:
                    break
        return res


class Solution2:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """Prim's algo.

        No need to pre-compute adjacency list

        1268 ms, faster than 89.21%
        """
        N = len(points)
        heap = []
        for j in range(1, N):
            heapq.heappush(heap, (abs(points[0][0] - points[j][0]) + abs(points[0][1] - points[j][1]), 0, j))
        num_edges = N - 1
        res = 0
        included = set([0])
        while num_edges:
            while heap[0][1] in included and heap[0][2] in included:
                heapq.heappop(heap)
            d, i, j = heapq.heappop(heap)
            res += d
            a = i if i not in included else j
            included.add(a)
            for j in range(N):
                if j not in included:
                    heapq.heappush(heap, (abs(points[a][0] - points[j][0]) + abs(points[a][1] - points[j][1]), a, j))
            num_edges -= 1
        return res


class Solution3:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """Optimized Prim.

        Each time after a new node is added to the MST, we check the distance
        between the new node to all the non-tree node and see if their distance
        is smaller than the current record of the non-tree node to some tree
        nodes. If it is smaller, we update the record. In other words, we keep
        an array min_dist, where min_dist[i] is the min dist from node i to the
        MST already formed.

        722 ms, faster than 99.75% 
        """
        N = len(points)
        min_dist = [math.inf] * N
        min_dist[0] = 0
        included = set([0])
        pre = 0  # most recent node added to MST
        res = 0
        while len(included) < N:
            min_d, i = math.inf, -1  # find min distance among the non-tree node to MST
            for j in range(N):
                if j not in included:
                    d = abs(points[pre][0] - points[j][0]) + abs(points[pre][1] - points[j][1])
                    if d < min_dist[j]:  # j to pre has smallest dist than j to some other node in MST
                        min_dist[j] = d
                    if min_dist[j] < min_d:
                        min_d = min_dist[j]
                        i = j
            res += min_d
            included.add(i)
            pre = i
        return res


sol = Solution3()
tests = [
    ([[0,0],[2,2],[3,10],[5,2],[7,0]], 20),
    ([[3,12],[-2,5],[-4,1]], 18),
    ([[0,0]], 0),
    ([[2,-3],[-17,-8],[13,8],[-17,-15]], 53),
]

for i, (points, ans) in enumerate(tests):
    res = sol.minCostConnectPoints(points)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
