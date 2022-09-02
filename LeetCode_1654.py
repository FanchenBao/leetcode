# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        mat = [[0]]
        while mat[-1][-1] != x:
            mat.append([mat[-1][0] + a])
            while mat[-1][-1] != x and mat[-1][-1] >= 0:
                mat[-1].append(mat[-1][-1] - b)
            if mat[-1][-1] < 0:
                mat[-1].pop()
        num_vert_move, num_hori_move = len(mat) - 1, len(mat[-1]) - 1
        if num_hori_move > num_vert_move:
            return -1
        
        def dfs(i: int, j: int, is_pre_hori: bool, num_hori_remain: int) -> bool:
            if num_hori_remain < 0 or i == len(mat) or j == len(mat[i]) or mat[i][j] in forbidden:
                return False
            if mat[i][j] == x:
                return True
            if is_pre_hori:
                if dfs(i + 1, j, False, num_hori_remain):
                    return True
                return False  # cannot do two horizontal in a row
            # go horizontal first
            if dfs(i, j + 1, True, num_hori_remain - 1):
                return True
            # go vertical
            if dfs(i + 1, j, False, num_hori_remain):
                return True
            return False

        for row in mat:
            print(row)
        print(num_vert_move + num_hori_move)
        return num_vert_move + num_hori_move if dfs(0, 0, False, num_hori_move) else -1


sol = Solution()
tests = [
    # ([14,4,18,1,15], 3, 15, 9, 3),
    # ([8,3,16,6,12,20], 15, 13, 11, -1),
    # ([1,6,2,14,5,17,4], 16, 9, 7, 2),
    # ([128,178,147,165,63,11,150,20,158,144,136],61,170,135,6),
    # ([162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98],29,98,80,121),
    # ([54,143,27,147,40,199,32,6,47,10,85,142,137,90,163,87,118,176,194,9,21,149,200,120,43,157,84,73,165,56,45,179,124,8,185,105,97,132,112,164,145,197,182,107,133,152,159,7,193,1,42,175,16,67,173,148,62,103,51,158,79,178,146,93,127,129,140,192,89,113,34,187,78,116,91,138,181,153,141,36,170,196,126,110,162,108], 11, 64, 52, 32),
    # ([5,2,10,12,18], 8, 6, 16, 2),
    ([1401,832,1344,173,1529,1905,1732,277,1490,650,1577,1886,185,1728,1827,1924,1723,1034,1839,1722,1673,1198,1667,538,911,1221,1201,1313,251,752,40,1378,1515,1789,1580,1422,907,1536,294,1677,1807,1419,1893,654,1176,812,1094,1942,876,777,1850,1382,760,347,112,1510,1278,1607,1491,429,1902,1891,647,1560,1569,196,539,836,290,1348,479,90,1922,111,1411,1286,1362,36,293,1349,667,430,96,1038,793,1339,792,1512,822,269,1535,1052,233,1835,1603,577,936,1684,1402,1739,865,1664,295,977,1265,535,1803,713,1298,1537,135,1370,748,448,254,1798,66,1915,439,883,1606,796], 19, 18, 1540, 120),
]

for i, (forbidden, a, b, x, ans) in enumerate(tests):
    res = sol.minimumJumps(forbidden, a, b, x)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
