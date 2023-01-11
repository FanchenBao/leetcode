# from pudb import set_trace; set_trace()
from typing import List, Tuple
import math


class Solution1:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        """First find bob's path to root. If bob and alice are only able to
        meet, if bob's path has odd number of nodes. Then the amount of the
        middle node must be halved. Furthermore, all the nodes that bob has
        traversed before the middle node must have their amount zeroed out.

        Then we traverse alice in all the paths to leaf. We use the updated
        amount to compute net income and return the max among them.

        O(N), 1641 ms, faster than 99.75%
        """
        N = len(amount)
        graph = [[] for _ in range(N)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        self.bob_path = None

        def bob_dfs(idx: int, par: int, path: List[int]) -> bool:
            path.append(idx)
            if idx == 0:
                self.bob_path = path[:]
                return True
            for nex in graph[idx]:
                if nex != par:
                    if bob_dfs(nex, idx, path):
                        return True
            path.pop()
            return False


        bob_dfs(bob, -1, [])
        if len(self.bob_path) % 2:
            i = len(self.bob_path) // 2
            amount[self.bob_path[i]] //= 2
        for i in range(len(self.bob_path) // 2):
            amount[self.bob_path[i]] = 0

        self.res = -math.inf

        def alice_dfs(idx: int, par: int, net_in: int) -> None:
            net_in += amount[idx]
            is_leaf = True
            for nex in graph[idx]:
                if nex != par:
                    is_leaf = False
                    alice_dfs(nex, idx, net_in)
            if is_leaf:
                self.res = max(self.res, net_in)

        alice_dfs(0, -1, 0)
        return self.res


class Solution2:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        """One pass?? Not really

        2730 ms, faster than 70.66%
        """
        N = len(amount)
        graph = [[] for _ in range(N)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        paths = []

        def dfs(idx: int, par: int, path: List[int]) -> None:
            path.append(idx)
            if idx == bob:
                l = len(path)
                if l % 2:
                    amount[path[l // 2]] //= 2
                for i in range(l - 1, (l - 1) // 2, -1):
                    amount[path[i]]= 0
            is_leaf = True
            for nex in graph[idx]:
                if nex != par:
                    is_leaf = False
                    dfs(nex, idx, path)
            if is_leaf:
                paths.append(path[:])
            path.pop()

        dfs(0, -1, [])
        return max(sum(amount[i] for i in path) for path in paths)


class Solution3:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        """True one pass. From https://leetcode.com/problems/most-profitable-path-in-a-tree/discuss/2807411/Python-One-DFS

        dp(idx, distance to root) = (
            max path sum in the subtree rooted at idx,
            distance between idx's parent and Bob
        )

        Distance between idx and Bob is set to larger or equal to n if idx is
        not an ancestor of Bob.

        O(N), 1710 ms, faster than 98.22% 
        """
        N = len(amount)
        graph = [[] for _ in range(N)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # d0 = distance from idx to 0
        # db = distance from idx to Bob
        # db >= n if idx is not an ancestor of Bob
        # note that the return value is the distance between idx's ancestor to
        # Bob
        def dfs(idx: int, par: int, d0) -> Tuple[int, int]:
            db = 0 if idx == bob else N
            sub_max = -math.inf
            for nex in graph[idx]:
                if nex != par:
                    cur, cur_db = dfs(nex, idx, d0 + 1)
                    sub_max = max(sub_max, cur)
                    db = min(db, cur_db)  # obtain idx's distance to Bob from its children
            if sub_max == -math.inf:  # leaf
                sub_max = 0  # a leaf node has sub tree max equal to 0
            res = sub_max
            if d0 == db:  # mid point
                res += amount[idx] // 2
            if d0 < db:  # alice is in a node NOT visited by bob
                res += amount[idx]
            return res, db + 1

        return dfs(0, -1, 0)[0]


sol = Solution3()
tests = [
    ([[0,1],[1,2],[1,3],[3,4]], 3, [-2,4,2,-4,6], 6),
    ([[0,1]], 1, [-7280,2350], -7280),
    ([[0,21],[0,6],[0,29],[1,3],[1,38],[2,32],[2,34],[2,27],[3,24],[3,8],[4,5],[4,21],[5,11],[5,28],[6,27],[7,23],[7,21],[8,12],[8,22],[8,36],[9,10],[10,17],[12,15],[13,24],[14,29],[16,25],[16,35],[16,39],[17,19],[17,39],[18,37],[18,26],[20,27],[26,38],[26,30],[29,30],[29,39],[30,31],[33,34]], 31, [562,5200,8954,-1176,3208,-140,940,9548,-662,-4974,-9054,-5868,-3888,404,-5184,418,3890,-9434,-8184,642,-5484,-4542,-372,-7818,-268,4512,-2648,-9016,8782,542,-8812,-7262,-9804,6622,-7030,8164,8354,-8176,5412,-5648], 15584),
]

for i, (edges, bob, amount, ans) in enumerate(tests):
    res = sol.mostProfitablePath(edges, bob, amount)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
