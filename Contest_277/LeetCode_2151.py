# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        res = 0
        n = len(statements)
        
        @lru_cache(maxsize=None)
        def check(good: int, bad: int, start: int) -> int:
            good |= (1 << start)
            queue = [start]
            while queue:
                temp = []
                for g in queue:
                    for j in range(n):
                        if statements[g][j] == 1:
                            if bad & (1 << j):
                                return -1
                            elif not good & (1 << j):
                                good |= (1 << j)
                                temp.append(j)
                        elif statements[g][j] == 0:
                            if good & (1 << j):
                                return -1
                            elif not bad & (1 << j):
                                bad |= (1 << j)
                queue = temp
            cur_state = good | bad
            res = 0
            for i in range(n):
                if not cur_state & (1 << i):
                    res = max(res, check(good, bad, i))
            return max(res, bin(good).count('1'))

        for i in range(n):
            res = max(res, check(0, 0, i))
        return res


sol = Solution()
tests = [
    ([[2,1,2],[1,2,2],[2,0,2]], 2),
    ([[2,0],[0,2]], 1),
]

for i, (statements, ans) in enumerate(tests):
    res = sol.maximumGood(statements)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
