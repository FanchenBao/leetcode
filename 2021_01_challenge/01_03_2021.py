# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def countArrangement(self, n: int) -> int:
        """The key is to build a base dict that specifies what number is
        available at each position. For instance, at position 4, the numbers
        available are 1, 2, 4. At position 12, the numbers available are 1, 2,
        3, 4, 6, 12.

        Once the base dict is ready, the rest is just a simple DFS. I include
        in this solution two ways to do DFS. One way uses a set to record the
        numbers already picked, while the other uses bit manipulation.

        156 ms, 81% ranking using set
        192 ms, 78% ranking using bit manipulation

        A few words on the official solution. Similar idea as mine, but it
        has a larger search space and check whether a number is valid during
        DFS recursion. In my solution, the valid numbers are precomputed.
        """
        base = {}
        for i in range(2, n + 1):
            base[i] = [i * j for j in range(1, n // i + 1)]
            for j in range(1, i):
                if i % j == 0:
                    base[i].append(j)
        self.res = 0

        # def dfs(cur_n, picked):
        #     if cur_n > n:
        #         self.res += 1
        #     else:
        #         for op in base[cur_n]:
        #             if not (1 << op) & picked:
        #                 picked |= 1 << op
        #                 dfs(cur_n + 1, picked)
        #                 picked ^= 1 << op

        # dfs(2, 0)

        def dfs(cur_n, picked):
            if cur_n > n:
                self.res += 1
            else:
                for op in base[cur_n]:
                    if op not in picked:
                        picked.add(op)
                        dfs(cur_n + 1, picked)
                        picked.remove(op)

        dfs(2, set())
        return self.res


sol = Solution()
tests = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 8),
    (5, 10),
    (6, 36),
    (7, 41),
    (8, 132),
    (9, 250),
    (10, 700),
    (11, 750),
    (12, 4010),
    (13, 4237),
    (14, 10680),
    (15, 24679),
]

for i, (n, ans) in enumerate(tests):
    res = sol.countArrangement(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
