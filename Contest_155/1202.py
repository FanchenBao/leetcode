#! /usr/bin/env python3
from typing import List, Dict, Set
from collections import defaultdict
from random import randint

"""10/08/2019

Solution1:

This solution works, but times out. The idea is that if any pairs share one
common position, then the letters at those three positions can freely move
around. With this observation, the problem turns into merging the given pairs
as much as possible (the result of such merging is called "island"), sort the
letters in the island, and put the sorted island back together.

However, this method is slow on the merging algorithm (too much recursion). I
need to find a faster algorithm to do the merging.


Solution2:

Tried a different way to produce island_sets, but still timed out (without even
having to try on OJ).


Solution3:

Differen way to do dfs compared to Solution1, in which I do not make any set
operations during dfs; instead, I simply create a long path to include all pos
that are inter-connected on an island. Each recursive call of dfs has only O(1)
complexity of extending the path, so it is faster than Solution1.

This solution passed OJ, clocking in at 908 ms, 42.74%


UPDATE: 10/11/2019

Solution4:

The problem is perfectly fit for a disjoint set union-find algorithm. Since
any two pairs that share a common index can have all three indices freely
interchange with each other, we just need to unionize all indices that are
connected to each other. From a disjoint set data structure point of view, we
need to find the least number of disjoint roots that connect to all the indices.
Then, for each such root, we list all the letters that connect to it. The letters
under each root can interchange position with each other. So we can sort them.
Finally, we loop through the indices, find the root for each index, and pull out
the smallest letter currently under the root.

This solution is heavily inspired by
https://leetcode.com/problems/smallest-string-with-swaps/discuss/387524/Short-Python-Union-find-solution-w-Explanation

The design of the disjoint set data structure is heavily inspired by
https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/

This solution is clean, neat, and beautiful. It passed OJ, clocking in at
968 ms, 22%.
"""


class Solution1:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        pairs = sorted(
            [[a, b] if a < b else [b, a] for a, b in pairs], key=lambda x: x[0]
        )
        pairs_dict: Dict[int, Set[int]] = defaultdict(set)
        for p in pairs:
            pairs_dict[p[0]].add(p[1])
            pairs_dict[p[1]].add(p[0])
        island_sets: List[Set[int]] = []

        def find_island(pos: int) -> Set[int]:
            k, pos_set = pos, pairs_dict[pos]
            del pairs_dict[k]
            island = pos_set.union({k})
            for p in pos_set:
                if p in pairs_dict:
                    island = island.union(find_island(p))
            return island

        while pairs_dict:
            island_sets.append(find_island(next(iter(pairs_dict))))

        res_lst: List[str] = list(s)
        for island in island_sets:
            island_pos = sorted(list(island))
            island_str: List[str] = []
            for pos in island_pos:
                island_str.append(s[pos])
            island_str.sort()
            for pos, le in zip(island_pos, island_str):
                res_lst[pos] = le
        return "".join(res_lst)


class Solution2:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        island_sets: List[Set[int]] = []
        while pairs:
            p_set = set(pairs.pop())
            temp = []
            for island in island_sets:
                if island.intersection(p_set):
                    p_set = island.union(p_set)
                else:
                    temp.append(island)
            temp.append(p_set)
            island_sets = temp

        res_lst: List[str] = list(s)
        for island in island_sets:
            island_pos = sorted(list(island))
            island_str: List[str] = []
            for pos in island_pos:
                island_str.append(s[pos])
            island_str.sort()
            for pos, le in zip(island_pos, island_str):
                res_lst[pos] = le
        return "".join(res_lst)


class Solution3:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # construct the dict that reflects all connections
        pairs_dict: Dict[int, Set[int]] = defaultdict(set)
        for a, b in pairs:
            if a != b:
                pairs_dict[a].add(b)
                pairs_dict[b].add(a)

        def dfs(pos: int, curr: List[int]) -> None:
            target_set = pairs_dict[pos]
            del pairs_dict[pos]  # remove pos from pairs_dict to avoid cycles
            for p in target_set:
                curr.append(p)  # record path
                if p in pairs_dict:
                    if pos in pairs_dict[p]:  # avoid cycles
                        pairs_dict[p].remove(pos)
                    dfs(p, curr)

        island_sets: List[Set[int]] = []
        while pairs_dict:
            # pick any pos to start with
            curr: List[int] = [next(iter(pairs_dict))]
            # get all pos that are connected to the pos that we start with
            dfs(curr[0], curr)
            island_sets.append(set(curr))  # record this island

        res_lst: List[str] = list(s)
        for island in island_sets:
            # get all pos in island from low to high
            island_pos = sorted(list(island))
            island_str: List[str] = []
            # acquire the letters at the pos indicated by island
            for pos in island_pos:
                island_str.append(s[pos])
            # letters on island can freely change position. Sort it.
            island_str.sort()
            for pos, le in zip(island_pos, island_str):
                res_lst[pos] = le  # put the letters back
        return "".join(res_lst)


class Subset:
    """ parent is the representation of a subset """

    def __init__(self, parent: int, rank: int):
        self.parent: int = parent
        self.rank: int = rank


class Solution4:
    def find(self, subsets: List[Subset], node: int) -> int:
        """
        Find the parent of a given node, also do path compression along
        the way.
        Args:
            subsets:    A list of Subsets, index is the node.
            node:       An index representing the node in subsets
        Returns:
            The parent (after path compression) of the given node
        Raises:
            None
        """
        if subsets[node].parent != node:  # this node has a parent
            subsets[node].parent = self.find(subsets, subsets[node].parent)
        return subsets[node].parent

    def union(self, subsets: List[Subset], node1: int, node2: int) -> None:
        """
        node1 and node2 are connected. They are unionized by assigning the
        highest ranked parent of the two nodes to the other node. E.g. if
        node1's parent is higher ranked than node2, then we assign node1's
        parent to node2, vice versa.
        Args:
            subsets:    A list of Subsets, index is the node.
            node1:      One of the two nodes on a connection
            node1:      The other node on a connection
        Returns:
            None
        Raises:
            None
        """
        parent1: int = self.find(subsets, node1)
        parent2: int = self.find(subsets, node2)
        if subsets[parent1].rank > subsets[parent2].rank:
            subsets[parent2].parent = parent1
        elif subsets[parent1].rank < subsets[parent2].rank:
            subsets[parent1].parent = parent2
        else:  # two parents have the same rank, assign either one as parent
            subsets[parent2].parent = parent1
            subsets[parent1].rank += 1

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        subsets: List[Subset] = [Subset(i, 0) for i in range(len(s))]
        for n1, n2 in pairs:
            self.union(subsets, n1, n2)
        # record all letters pointing to the same parent. These letters are
        # interchangeable.
        parent_dict: Dict[int, List[str]] = defaultdict(list)
        for i, subset in enumerate(subsets):
            parent_dict[self.find(subsets, i)].append(s[i])
        for v in parent_dict.values():
            v.sort(reverse=True)
        res: List[str] = []
        for i in range(len(s)):
            res.append(parent_dict[self.find(subsets, i)].pop())
        return "".join(res)


def unit_test(Solution):
    sol = Solution()
    # Test 1
    s = "cba"
    pairs = [[0, 1], [1, 2]]
    res = sol.smallestStringWithSwaps(s, pairs)
    if res == "abc":
        print("Test 1 PASS")
    else:
        print(f"Test 1 Fail. Wrong answer: {res}")

    # Test 2
    s = "dcab"
    pairs = [[0, 3], [1, 2], [0, 2]]
    res = sol.smallestStringWithSwaps(s, pairs)
    if res == "abcd":
        print("Test 2 PASS")
    else:
        print(f"Test 2 Fail. Wrong answer: {res}")

    # Test 3
    s = "dcab"
    pairs = [[0, 3], [1, 2]]
    res = sol.smallestStringWithSwaps(s, pairs)
    if res == "bacd":
        print("Test 3 PASS")
    else:
        print(f"Test 3 Fail. Wrong answer: {res}")

    # Test 5
    s = "fqtvkfkt"
    pairs = [[2, 4], [5, 7], [1, 0], [0, 0], [4, 7], [0, 3], [4, 1], [1, 3]]
    res = sol.smallestStringWithSwaps(s, pairs)
    if res == "ffkqttkv":
        print("Test 5 PASS")
    else:
        print(f"Test 5 Fail. Wrong answer: {res}")


def random_case(LEN):
    s = "".join([chr(randint(97, 122)) for _ in range(LEN)])
    pairs = [[randint(0, LEN - 1), randint(0, LEN - 1)] for _ in range(LEN)]
    return s, pairs


def random_test(Solution, LEN):
    sol = Solution()
    s, pairs = random_case(LEN)
    # print(f'"{s}"')
    # print(pairs)
    print(sol.smallestStringWithSwaps(s, pairs))


def single_test(Solution):
    sol = Solution()
    s = "nddsdvuvegaidutafwwtdycadhnssivsyxvbrybbmjmtlodvhl"
    pairs = [
        [16, 1],
        [26, 46],
        [46, 17],
        [42, 3],
        [0, 10],
        [9, 22],
        [20, 18],
        [11, 41],
        [19, 4],
        [43, 34],
        [46, 46],
        [31, 18],
        [21, 29],
        [19, 21],
        [25, 18],
        [9, 1],
        [0, 18],
        [37, 17],
        [29, 38],
        [30, 17],
        [12, 12],
        [25, 43],
        [6, 40],
        [21, 36],
        [40, 6],
        [21, 30],
        [34, 16],
        [28, 16],
        [39, 40],
        [45, 12],
        [39, 1],
        [8, 16],
        [26, 24],
        [6, 18],
        [21, 38],
        [28, 8],
        [34, 13],
        [22, 3],
        [22, 17],
        [22, 9],
        [2, 45],
        [18, 21],
        [23, 14],
        [32, 27],
        [15, 34],
        [28, 12],
        [21, 13],
        [38, 27],
        [9, 0],
        [31, 28],
    ]
    print(sol.smallestStringWithSwaps(s, pairs))


def compare_sol(S1, S2, T, LEN):
    sol1 = S1()
    sol2 = S2()
    s, pairs = random_case(LEN)
    for _ in range(T):
        res1 = sol1.smallestStringWithSwaps(s, pairs)
        res2 = sol2.smallestStringWithSwaps(s, pairs)
        if res1 != res2:
            print(s)
            print(pairs)
            print(f"{sol1}: {res1}")
            print(f"{sol2}: {res2}")


# unit_test(Solution4)
# random_test(Solution4, 10000)
single_test(Solution4)
# compare_sol(Solution3, Solution4, 1000, 1000)
