# from pudb import set_trace; set_trace()
from typing import List, Set


class Solution:
    def find_children(self, node: int, dig: int, visited: Set[int], temp: List[int]) -> None:
        mod = 10**dig
        chg = mod // 10
        to_chg = node % mod
        # wheel going forward
        cand1 = node - to_chg + ((to_chg + chg) % mod)
        # wheel going backward
        cand2 = node - to_chg + ((to_chg + mod - chg) % mod)
        if cand1 not in visited:
            visited.add(cand1)
            temp.append(cand1)
        if cand2 not in visited:
            visited.add(cand2)
            temp.append(cand2)

    def openLock(self, deadends: List[str], target: str) -> int:
        """LeetCode 752

        We treat each possible combination as a node in a graph. From each
        node, there are eight children, obtained by turning the wheel on each
        digit either forward or backward. We start from 0000, perform a BFS,
        and return the depth when the target is found.

        The tricky part is to find all eight children. In order to represent
        the node as something hashable and easy to manipulate, we turn each node
        into an integer representation of the original str version. Then we
        check the digit at each position. If it is a 0, it has to be
        treated separately, because from 0 going backwards we end up with 9.

        Technically, complexity is O(1), because we visit each node only once,
        and there are only 9999 nodes. 372 ms, 95% ranking.
        """
        visited = set(int(d) for d in deadends)
        t_node = int(target)
        if t_node == 0:
            return 0
        if 0 in visited:
            return -1
        steps = 0
        queue = [0]
        visited.add(0)
        while queue:
            temp = []
            for node in queue:
                for dig in range(1, 5):
                    self.find_children(node, dig, visited, temp)
                if t_node in visited:
                    return steps + 1
            steps += 1
            queue = temp
        return -1


sol = Solution()
tests = [
    (['0201', '0101', '0102', '1212', '2002'], '0202', 6),
    (['8888'], '0009', 1),
    (['8887', '8889', '8878', '8898', '8788', '8988', '7888', '9888'], '8888', -1),
    (['0000'], '8888', -1),
    (['0000'], '0000', 0),
]

for i, (deadends, target, ans) in enumerate(tests):
    res = sol.openLock(deadends, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
