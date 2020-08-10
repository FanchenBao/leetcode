#! /usr/bin/env python3
from typing import List, Set, Tuple

# from collections import deque
from random import randint

# from time import time
"""09/21/2019

Solution1:
For any given server, follow its connection to the next server. If this path
cannot lead to a loop that goes back to the current server or any of its ancestor,
then the connection between the current and next servers is critical. I use DFS
to recursively perform the above-mentioned procedure. Some optimization is carried
out, such as shrinking the search space by removing the connections visited at
each step. However, this method times out (too many recursions). Most likely
a non-recursive method is needed.


UPDATE 09/25/2019
Solution2:
I wasn't able to find other methods to reduce time complexity, so I referred to
the discussion.

https://leetcode.com/problems/critical-connections-in-a-network/discuss/382638/No-TarjanDFS-detailed-explanation-O(orEor)-solution-(I-like-this-question)

It turned out my original solution was not wrong. Indeed, DFS
is needed. However, the reason for my time out was due to returning a set at
each recursion call. Given tons of recursion calls, the overhead of copying a
set at each return results in TLE.

The genious of the solution in the discussion (not the Tarjan one) is that we
don't need to return all the loop_start we can reach from a certain node. For
example, if a certain node can reach two loop_start a and b, and a is more
upstream than b in the path, then we can ignore b and only return a. In order to
determine which node is more upstream, we need to attach rank to each node we
have visited in a route. This is where the discussion solution differs from my
original one. My original solution does not take into consideration ranking, thus
I need to record all the loop_start a node can hit. But now, with ranking, I
only need to record the smallest rank a node can reach, i.e. returning an int
instead of a set. This drastically decreases the runtime.

In Solution2, I also used the discussion answer's idea of removing connection in
a loop, instead of adding the disconnection once it is encountered. Solution2
passed OJ (though it reported too many recursions on my macbook), clocking in at
2804 ms, 17%


Solution3:
This solution is a combination of Solution1 and Solution2. Basically the
structure of Solution2, but instead of removing loop connections, I add the
disconnect. This solution clocked in at 2648 ms, 44%.


UPDATE: 09/28/2019
Solution4:
It is the standard Tarjan algorithm, heavily inspired by this post:
https://leetcode.com/problems/critical-connections-in-a-network/discuss/382526/Tarjan-Algorithm-(DFS)-Python-Solution-with-explanation

The basic idea is the same as the other solutions, except this time, the code
is much cleaner and algorithm much easier to parse. We are dfs all nodes, and
along the way, we record the ranking (visiting order) of each node, and the
smallest rank the current node can reach eventually. These two data are recorded
during dfs, and analyzed after dfs is done. For any connection n1 -> n2, if the
min rank n2 can reach is larger than the rank of n1, then n1 -> n2 must be a
disconnection. We can loop through the given connections and pick out those
disconnection easily.

Brilliant solution. It clocks in at 2376 ms, 99.26%
"""


class Solution1:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        connects: List[Set[int]] = [set() for _ in range(n)]
        # each index represents a server, and the set associated with it contains
        # the servers that the index server directly connects to.
        for a, b in connections:
            connects[a].add(b)
            connects[b].add(a)
        cc: List[List[int]] = []  # record the critical connections
        seen: Set[int] = set()  # record the servers seen so far
        for i in range(n):
            self.helper(i, connects, seen, cc)
        return cc

    def helper(
        self,
        curr_node: int,
        connects: List[Set[int]],
        seen: Set[int],
        cc: List[List[int]],
    ):
        if curr_node in seen:  # loop found, return the start of the loop
            return {curr_node}
        else:
            seen.add(curr_node)
            loop_start: Set[
                int
            ] = set()  # ancestor servers to which the current server can loop back
            while len(connects[curr_node]):
                next_node: int = connects[
                    curr_node
                ].pop()  # remove next server from connects, so that it won't be visited again
                connects[next_node].remove(curr_node)
                loop_start_next = self.helper(next_node, connects, seen, cc)
                if (
                    not loop_start_next
                ):  # if next server cannot form a loop involving current server, this is critical connection
                    cc.append([curr_node, next_node])
                loop_start = loop_start.union(loop_start_next)
            if curr_node in loop_start:  # a loop is complete
                loop_start.remove(curr_node)
            seen.remove(curr_node)
            return loop_start


class Solution2:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        connects: List[Set[int]] = [set() for _ in range(n)]
        # each index represents a server, and the set associated with it contains
        # the servers that the index server directly connects to.
        for a, b in connections:
            connects[a].add(b)
            connects[b].add(a)
        # connections_set makes removal of connection easier
        connections_set: Set[Tuple[int, int]] = set(
            (a, b) if a < b else (b, a) for a, b in connections
        )
        seen: List[int] = [
            -1
        ] * n  # record the servers seen so far, with its rank. -1: node not visited yet
        for i in range(n):
            self.helper(i, 0, connects, seen, connections_set, n, n)
        return [list(c) for c in connections_set]

    def helper(
        self,
        curr_node: int,
        curr_rank: int,
        connects: List[Set[int]],
        seen: List[int],
        connections_set: Set[Tuple[int, int]],
        loop_start: int,
        n: int,
    ) -> int:
        if seen[curr_node] >= 0:  # loop found, return the start of the loop
            return min(loop_start, seen[curr_node])
        else:
            seen[curr_node] = curr_rank
            min_loop_start: int = n
            while len(
                connects[curr_node]
            ):  # there are still more routes to go
                next_node: int = connects[
                    curr_node
                ].pop()  # remove next server from connects, so that it won't be visited again
                connects[next_node].remove(curr_node)
                tmp = self.helper(
                    next_node,
                    curr_rank + 1,
                    connects,
                    seen,
                    connections_set,
                    loop_start,
                    n,
                )
                if tmp <= curr_rank:  # remove connections in a loop
                    connections_set.remove(
                        (curr_node, next_node)
                        if curr_node < next_node
                        else (next_node, curr_node)
                    )
                # back to the start of loop, any node upstream is not in the current loop
                min_loop_start = (
                    n if tmp == curr_rank else min(min_loop_start, tmp)
                )
            seen[curr_node] = -1
            return min_loop_start


class Solution3:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        connects: List[Set[int]] = [set() for _ in range(n)]
        # each index represents a server, and the set associated with it contains
        # the servers that the index server directly connects to.
        for a, b in connections:
            connects[a].add(b)
            connects[b].add(a)
        cc: List[List[int]] = []  # record the critical connections
        seen: List[int] = [
            -1
        ] * n  # record the servers seen so far, with its rank. -1: node not visited yet
        for i in range(n):
            self.helper(i, 0, connects, seen, cc, n)
        return cc

    def helper(
        self,
        curr_node: int,
        curr_rank: int,
        connects: List[Set[int]],
        seen: List[int],
        cc: List[List[int]],
        loop_start: int,
    ) -> int:
        if seen[curr_node] >= 0:  # loop found, return the start of the loop
            return min(loop_start, seen[curr_node])
        else:
            seen[curr_node] = curr_rank
            min_loop_start: int = len(
                seen
            )  # use len(seen), or n, to mark disconnect
            while len(
                connects[curr_node]
            ):  # there are still more routes to go
                next_node: int = connects[
                    curr_node
                ].pop()  # remove next server from connects, so that it won't be visited again
                connects[next_node].remove(curr_node)
                tmp = self.helper(
                    next_node, curr_rank + 1, connects, seen, cc, loop_start
                )
                if tmp == len(seen):  # disconnect found
                    cc.append([curr_node, next_node])
                # back to the start of loop, any node upstream is not in the current loop
                min_loop_start = (
                    len(seen) if tmp == curr_rank else min(min_loop_start, tmp)
                )
            seen[curr_node] = -1
            return min_loop_start


class Solution4:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        graph: List[List[int]] = [
            list() for _ in range(n)
        ]  # create data structure for the graph for dfs
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        ranks: List[int] = [
            0
        ] * n  # record the ranks (visiting order) for each node
        min_ends: List[int] = [0] * n  # the smallest rank a node can reach

        def dfs(pre_node: int, curr_node: int, curr_rank: int) -> int:
            """ from each node, visit all nodes it leads to and return the min rank the current node can reach """
            if ranks[curr_node]:  # loop found
                return ranks[curr_node]
            elif min_ends[curr_node]:  # curr_node has been visited before
                return min_ends[curr_node]
            else:
                ranks[curr_node] = curr_rank  # record current rank
                min_ends[
                    curr_node
                ] = (
                    curr_rank
                )  # default smallest rank a node can reach is itself
                for next_node in graph[curr_node]:
                    if next_node != pre_node:  # don't go backwards
                        min_ends[curr_node] = min(
                            min_ends[curr_node],
                            dfs(curr_node, next_node, curr_rank + 1),
                        )
                return min_ends[curr_node]

        dfs(-1, 0, 1)  # -1 is a dummy value for the pre_node of node 0
        res: List[List[int]] = []
        for n1, n2 in connections:
            # If n1 -> n2, then disconnect happens when n2 cannot lead to a rank smaller or equal to rank of n1.
            # Same with the situation of n2 -> n1
            if min_ends[n2] > ranks[n1] or min_ends[n1] > ranks[n2]:
                res.append([n1, n2])
        return res


def random_connections(n):
    """ Note that the connections created here might not be accurate test
        cases, because there is no guarantee that the connections can connect
        all servers together. That is, the following connections can be returned:
        [[1, 2], [0, 3]], yet it does not satisfy the requirement for testcase,
        which dictates that any server can reach any other servers directly or
        indirectly.
    """
    res = set()
    for _ in range(n):
        c1 = randint(0, n - 1)
        c2 = randint(0, n - 1)
        while c2 == c1:
            c2 = randint(0, n - 1)
        res.add((c1, c2) if c1 < c2 else (c2, c1))
    return [list(s) for s in res]


def single_test(Solution):
    n = 4
    connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
    sol = Solution()
    print(sol.criticalConnections(n, connections))


def random_tets(Solution):
    n = 10000
    connections = random_connections(n)
    sol = Solution()
    # print(n)
    # print(connections)
    print(sol.criticalConnections(n, connections))


# random_tets(Solution2)
single_test(Solution4)
