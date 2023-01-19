# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        ini_st = [c for _, c in factory]
        M, N = len(robot), len(factory)
        dp = [[0, ini_st] for _ in range(N + 1)]
        dp[0][0] = math.inf
        for i in range(1, M + 1):
            tmp = [[math.inf, ini_st[:]]]
            for j in range(1, N + 1):
                # op1, ith robot uses the previous 0, ..., j - 1 machines
                d1, st1 = tmp[j - 1]
                # op2, ith robot uses jth machine, the other robots use 0, ..., j - 1 machines
                d2, st2 = dp[j - 1]
                if st2[j - 1] > 0:
                    d2 += abs(robot[i - 1] - factory[j - 1][0])
                else:
                    d2 = math.inf
                # op3, the other robots use 0, ..., j machines. ith robot must
                # try each one to locate a best shot
                d3, st3 = dp[j]
                tar_j = -1
                cur_dist = math.inf
                for k in range(j - 1, -1, -1):
                    d = abs(robot[i - 1] - factory[k][0]) if st3[k] > 0 else math.inf
                    if d <= cur_dist:
                        cur_dist = d
                        tar_j = k
                    elif d != math.inf:
                        break
                d3 += cur_dist
                if d1 <= d2 and d1 <= d3:
                    tmp.append([d1, st1[:]])
                elif d2 == d3 and d2 < d1:
                    if j - 1 >= tar_j:
                        st = st2[:]
                        st[j - 1] -= 1
                        tmp.append([d2, st])
                    else:
                        st = st3[:]
                        st[tar_j] -= 1
                        tmp.append([d3, st])
                elif d2 < d3 and d2 < d1:
                    st = st2[:]
                    st[j - 1] -= 1
                    tmp.append([d2, st])
                elif d3 < d2 and d3 < d1:
                    st = st3[:]
                    st[tar_j] -= 1
                    tmp.append([d3, st])
            dp = tmp
        return dp[-1][0]


sol = Solution()
tests = [
    ([0,4,6], [[2,2],[6,2]], 4),
    ([1,-1], [[-2,1],[2,1]], 2),
    ([79215383,708490359,-779179404,713376652,-368850098,573013032,195489859,121470584,916616893,327266713,950673412,410723622,538863648,170740409,753199490], [[-284344805,4],[349360740,6],[-360820857,2],[-493544411,13],[-28182860,4],[-117519725,13],[-294274103,9]], 5121930465),
]

for i, (robot, factory, ans) in enumerate(tests):
    res = sol.minimumTotalDistance(robot, factory)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
