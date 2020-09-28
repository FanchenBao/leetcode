# from pudb import set_trace; set_trace()
from typing import List
from functools import reduce
from math import isclose
from collections import Counter, defaultdict


class Solution1:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """56% ranking
        
        I initially misunderstood the question. I thought the letters in the
        equation can be split into individual tokens, e.g. ab / bc = 1 would
        mean a / c = 1. However, this is not the case. In this question, 'ab'
        and 'cd' are tokens unrelated to tokens 'a', 'b', and 'c'. This
        definitely simplified the question. While I lamented that the question
        could've been more fun had the letters in the equations capable of
        being split into individual tokens, I realized that the real difficulty
        lie in solving the given equations and identifying when the equations
        were solvable and when not. For that matter, I had to add a tag system
        to ensure that the values I arbitrarily assign to the tokens were
        valid.
        """
        sols = {}  # each unknown token is associated with a value and a tag
        solved = False
        while not solved:  # solve the given equations
            solved = True
            for (x1, x2), val in zip(equations, values):
                if x1 in sols and x2 not in sols:
                    sols[x2] = (sols[x1][0] / val, sols[x1][1])
                elif x1 not in sols and x2 in sols:
                    sols[x1] = (sols[x2][0] * val, sols[x2][1])
                elif x1 not in sols and x2 not in sols:
                    sols[x1], sols[x2] = (val, x2), (1, x2)
                else:
                    if not isclose(sols[x1][0] / sols[x2][0], val, rel_tol=1e-5) or sols[x1][1] != sols[x2][1]:
                        # either values are incorrect or tags do not match
                        solved = False
                        sols[x1] = (val * sols[x2][0], sols[x2][1])  # new value and tag
                        for k in list(sols.keys()):  # solve the equation again
                            if k not in {x1, x2}:
                                del sols[k]
                        break
        res = []
        for q1, q2 in queries:
            v1, tag1 = sols.get(q1, (-1, ''))
            v2, tag2 = sols.get(q2, (-1, ''))
            if v1 < 0 or v2 < 0 or tag1 != tag2:
                res.append(-1)
            else:
                res.append(v1 / v2)
        return res


class Solution2:
    def dfs(self, graph, cur_token, target, visited, pre_res) -> float:
        if target in graph[cur_token]:
            return pre_res * graph[cur_token][target]
        for next_token, weight in graph[cur_token].items():
            if next_token not in visited:
                visited.add(next_token)
                res = self.dfs(graph, next_token, target, visited, pre_res * weight)
                visited.remove(next_token)
                if res >= 0:
                    return res
        return -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """Graph with DFS"""
        graph = defaultdict(dict)
        for (x1, x2), val in zip(equations, values):
            graph[x1][x2] = val
            graph[x2][x1] = 1 / val
        return [self.dfs(graph, q1, q2, set(), 1) for q1, q2 in queries]


class UnionNode:
    def __init__(self):
        self.parent = None
        self.val = -1


class Solution3:
    def union(self, u1: UnionNode, u2: UnionNode, union_map, val):
        """Treat u2 as the new parent. point everything to u2, and modify
        values of each UnionNode along the way
        """
        p1, p2 = self.find(u1), self.find(u2)
        ratio = val * u2.val / u1.val
        for node in union_map.values():
            if self.find(node) == p1:
                node.val *= ratio
        p1.parent = p2

    def find(self, u: UnionNode) -> UnionNode:
        if u.parent == u:
            return u
        u.parent = self.find(u.parent)
        return u.parent

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """Graph with Union Find

        Reference: https://leetcode.com/explore/featured/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3474/discuss/88170/0ms-C++-Union-Find-Solution-EASY-to-UNDERSTAND
        """
        union_map = {}
        for (x1, x2), val in zip(equations, values):
            if x1 not in union_map and x2 not in union_map:
                union_map[x1] = UnionNode()
                union_map[x2] = UnionNode()
                union_map[x1].val = val
                union_map[x1].parent = union_map[x2]
                union_map[x2].val = 1
                union_map[x2].parent = union_map[x2]
            elif x1 not in union_map:
                union_map[x1] = UnionNode()
                union_map[x1].parent = union_map[x2]
                union_map[x1].val = val * union_map[x2].val
            elif x2 not in union_map:
                union_map[x2] = UnionNode()
                union_map[x2].parent = union_map[x1]
                union_map[x2].val = union_map[x1].val / val
            else:
                self.union(union_map[x1], union_map[x2], union_map, val)
        res = []

        for q1, q2 in queries:
            if q1 not in union_map or q2 not in union_map or self.find(union_map[q1]) != self.find(union_map[q2]):
                res.append(-1)
            else:
                res.append(union_map[q1].val / union_map[q2].val)
        return res




sol = Solution3()
tests = [
    # ([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]], [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]),
    # ([["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0], [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]], [3.75000, 0.40000, 5.00000, 0.20000]),
    # ([["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]], [0.50000, 2.00000, -1.00000, -1.00000]),
    # ([["a", "aa"]], [9.0], [["aa", "a"], ["aa", "aa"]], [0.11111, 1.00000]),
    # ([["a", "b"], ["e", "f"], ["b", "e"]], [3.4, 1.4, 2.3], [["b", "a"], ["a", "f"], ["f", "f"], ["e", "e"], ["c", "c"], ["a", "c"], ["f", "e"]], [0.29412,10.94800,1.00000,1.00000,-1.00000,-1.00000,0.71429]),
    # ([["a", "b"], ["c", "d"]], [1.0, 1.0], [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]], [-1.00000, -1.00000, 1.00000, 1.00000]),
    ([["a", "b"], ["b", "c"], ["a", "c"]], [2.0, 3.0, 6.0], [["a", "c"]], []),
]

for i, (equations, values, queries, ans) in enumerate(tests):
    res = sol.calcEquation(equations, values, queries)
    vdt = [isclose(r, a, rel_tol=1e-5) for r, a, in zip(res, ans)]
    if all(vdt):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
