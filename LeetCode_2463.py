# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        ini_st = tuple(c for _, c in factory)
        M, N = len(robot), len(factory)
        dp = [set([(0, ini_st)]) for _ in range(N + 1)]
        dp[0] = set([(math.inf, ini_st)])
        for i in range(M):
            tmp = [set([(math.inf, ini_st)])]
            for j in range(1, N + 1):
                tmp.append(set())
                # op1, ith robot uses the previous 0, ..., j - 1 machines
                for d1, st1 in tmp[j - 1]:
                    if d1 < math.inf:
                        tmp[-1].add((d1, st1))
                # op2, ith robot uses jth machine, the other robots use 0, ..., j - 1 machines
                for d2, st2 in dp[j - 1]:
                    if st2[j - 1] > 0 and d2 < math.inf:
                        st = list(st2)
                        st[j - 1] -= 1
                        tmp[-1].add((d2 + abs(robot[i] - factory[j - 1][0]), tuple(st)))
                # op3, the other robots use 0, ..., j machines. ith robot must
                # try each one to locate a best shot
                for d3, st3, in dp[j]:
                    if d3 < math.inf:
                        for k in range(j):
                            if st3[k] > 0:
                                st = list(st3)
                                st[k] -= 1
                                tmp[-1].add((d3 + abs(robot[i] - factory[k][0]), tuple(st)))
            dp = tmp
            # print(dp)
        res = math.inf
        for g in dp:
            for d, _ in g:
                res = min(res, d)
        return res


sol = Solution()
tests = [
    # ([0,4,6], [[2,2],[6,2]], 4),
    # ([1,-1], [[-2,1],[2,1]], 2),
    # ([79215383,708490359,-779179404,713376652,-368850098,573013032,195489859,121470584,916616893,327266713,950673412,410723622,538863648,170740409,753199490], [[-284344805,4],[349360740,6],[-360820857,2],[-493544411,13],[-28182860,4],[-117519725,13],[-294274103,9]], 5121930465),
    # ([79,70,-79,72,-38,57,19,12,93,33,92,40,53,17,73], [[-24,4],[34,6],[-36,2],[-41,13],[-28,4],[-11,13],[-29,9]], 623),
    # ([-9, -7, -6, 3, -20], [[1, 2], [-15, 1], [-17, 5]], 28),
]

for i, (robot, factory, ans) in enumerate(tests):
    res = sol.minimumTotalDistance(robot, factory)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
