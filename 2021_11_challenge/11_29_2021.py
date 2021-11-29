# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """LeetCode 721
        
        I tried to not use union find, but it didn't work out. With union and
        find, we can union the indices of the accounts. The only other issue is
        how to determine whether two accounts need to be unioned. This is
        achieved with a hashmap where each email address points to an index.
        Thus, if a new account's email address is in the hashmap, we know the
        new account can union with the index pointed to by the hashmap.

        O(MNlog(MN)), 352 ms, 21% ranking.

        UPDATE: the official solution offers a less convoluted way to implement
        the algo with union find. The major difference is doing away with set
        union. Since we already place all unique emials in hashmap, we can
        iterate the hashmap to obtain emails, instead of iterating accounts. The
        latter requires set union, whereas the former does not. Since we do not
        have to use set union when constructing the result, the runtime is
        reduced to 196 ms, 86% ranking.
        """
        dsu = DSU(len(accounts))
        hashmap = {}
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in hashmap:
                    dsu.union(hashmap[email], i)
                else:
                    hashmap[email] = i
        res = [['', []] for _ in accounts]
        for email, idx in hashmap.items():
            par = dsu.find(idx)
            if not res[par][0]:
                res[par][0] = accounts[par][0]
            res[par][1].append(email)
        return [[name, *sorted(emails)] for name, emails in res if name]


class Solution2:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """DFS solution from the official solution.

        Build an acyclic graph for each email address. For each account,
        arbitrarily choose the first email as the root node, and connect the
        rest email addresses to the root. The beauty of this is that if a new
        account has an email address shared with a previous account, the process
        of constructing the graph guarantees that the previous account's email
        address graph will be connected to the new account's email address graph
        and this process also eliminates duplicates.

        To obtain the result, we simply DFS each email address graph.

        O(MNlog(MN)), 196 ms.
        """
        graph = defaultdict(list)
        for acc in accounts:
            root_email = acc[1]
            for email in acc[2:]:
                graph[root_email].append(email)
                graph[email].append(root_email)

        visited = set()

        def dfs(node: str, merged: List[str]) -> None:
            if node in visited:
                return
            merged.append(node)
            visited.add(node)
            for nei in graph[node]:
                dfs(nei, merged)

        res = []
        for acc in accounts:
            name = acc[0]
            root_email = acc[1]
            # If a node has been visited, that means all the email addresses of
            # the same account has been accounted for already.
            if root_email not in visited:
                merged = []
                dfs(root_email, merged)
                res.append([name, *sorted(merged)])
        return res
            

sol = Solution2()
tests = [
    ([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]], [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]),
    ([["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]], [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]),
    ([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]], [["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]),
]

for i, (accounts, ans) in enumerate(tests):
    res = sol.accountsMerge(accounts)
    res.sort()
    ans.sort()
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
