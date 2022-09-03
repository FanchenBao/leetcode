# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        """Very difficult one. I had the intuition correct, that by using BFS,
        we can always find the solution when x is reachable. The difficulty is
        when x is not reachable. Since we can always add a, there is no end
        to BFS. Thus, the key to the problem is to find the upper bound for
        BFS. If no solution is found within the upper bound, we can say x is
        not reachable.

        To determine the upper bound, we have to use the Bezout's Identity,
        which stipulates that given any integers u and v, a * v + b * v = n *
        gcd(a, b). In addition, we need some ingenuity, which is detailed in
        this post: https://leetcode.com/problems/minimum-jumps-to-reach-home/discuss/978357/C%2B%2B-bidirectional-BFS-solution-with-proof-for-search-upper-bound

        I am going to describe here my understanding of finding the upper bound.

        We know that if a >= b, we basically cannot go left. Thus, the upper
        bound is x itself. This means if we go beyond x, there is no way we
        can go back. So whenever we go beyond x, we know x is not reachable.

        If a < b, we can go right and left. Now we can definitely go beyond x.
        Furthermore, to verify all possibilities, we have to go beyond
        max(forbidden), because the forbidden values add another layer of
        complexity. We must go beyond that to hit all possibilities associated
        with the forbidden value. Thus, the upper bound must be beyond max(x,
        max(forbidden)).

        Given Bezout's Identity, let p = n * gcd(a, b) that is the smallest
        value bigger than max(x, max(forbidden)). p is the left most point that
        we can reach beyond max(x, max(forbidden)). Notice that there is no
        more forbidden value to the right of p. Therefore, we don't have to
        worry about the added complexity of forbidden values now.

        Let's say we are at p right now. The first move we can make that will
        land us in the new territory is p + a. Since a is a multiple of
        gcd(a, b), there are other points we can reach between p and p + a,
        such as:

        p + gcd(a, b), p + 2 * gcd(a, b), ..., p - gcd(a, b) + a

        Note that all these positions can only be reached by a left jump.
        Therefore, the upper bound must be p - gcd(a, b) + a + b.

        One might ask, why can't we go beyond p - gcd(a, b) + a + b? We
        certainly can, but going beyond p - gcd(a, b) + a + b won't help us to
        reach x if we don't go left. And if we go left, eventually we will end
        up at one of the positions in [p, p + a] again, and when that happens,
        we have already taken more steps than visiting the positions in
        [p, p + a] for the first time.

        Therefore, the upper bound must be p - gcd(a, b) + a + b.

        Since p = n * gcd(a, b) is the smallest multiple of gcd(a, b) that is
        larger than max(x, max(forbidden)), we have
        p - gcd(a, b) <= max(x, max(forbidden)). Thus, p - gcd(a, b) + a + b <=
        max(x, max(forbidden)) + a + b.

        Therefore, it is perfectly okay for us to set the upper bound to be
        max(x, max(forbidden)) + a + b

        Once we have the upper bound, we can use BFS to find the solution.

        O(max(x, max(forbidden)) + a + b), 264 ms, faster than 31.58%
        """
        upper_bound = max(x, max(forbidden)) + a + b
        forbidden = set(forbidden)
        queue = set([(0, False)])
        steps = 0
        visited = set()
        while queue:
            temp = set()
            for pos, is_pre_left in queue:
                visited.add(pos)
                if pos == x:
                    return steps
                if pos + a <= upper_bound and pos + a not in forbidden and pos + a not in visited:
                    temp.add((pos + a, False))
                if pos - b >= 0 and pos - b not in forbidden and pos - b not in visited and not is_pre_left:
                    temp.add((pos - b, True))
            if temp:
                steps += 1
            queue = temp
        return -1


class Solution2:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        """Same logic as Solution1, but implemented using Bi-directional BFS.

        The implementation is quite challenging. Runtime doesn't seem to be
        worth the effort.

        262 ms, faster than 32.07%
        """
        upper_bound = max(x, max(forbidden)) + a + b
        forbidden = set(forbidden)
        queue_src = set([(0, False)])
        queue_des = set([(x, False)])
        steps_src = steps_des = 0
        visited_src = {}  # key is pos, value is (step, is_pre_left)
        visited_des = {}  # key is pos, value is (step, is_next_left)
        while queue_src or queue_des:
            if queue_src:
                temp_src = set()
                for pos, is_pre_left in queue_src:
                    visited_src[pos] = (steps_src, is_pre_left)
                    if pos in visited_des and not (is_pre_left and visited_des[pos][1]):
                        return visited_src[pos][0] + visited_des[pos][0]
                    if pos + a <= upper_bound and pos + a not in forbidden and pos + a not in visited_src:
                        temp_src.add((pos + a, False))
                    if pos - b >= 0 and pos - b not in forbidden and pos - b not in visited_src and not is_pre_left:
                        temp_src.add((pos - b, True))
                if temp_src:
                    steps_src += 1
                queue_src = temp_src
            if queue_des:
                temp_des = set()
                for pos, is_next_left in queue_des:
                    visited_des[pos] = (steps_des, is_next_left)
                    if pos in visited_src and not (is_next_left and visited_src[pos][1]):
                        return visited_src[pos][0] + visited_des[pos][0]
                    if pos + b <= upper_bound and pos + b not in forbidden and pos + b not in visited_des and not is_next_left:
                        temp_des.add((pos + b, True))
                    if pos - a >= 0 and pos - a not in forbidden and pos - a not in visited_des:
                        temp_des.add((pos - a, False))
                if temp_des:
                    steps_des += 1
                queue_des = temp_des
        return -1


sol = Solution2()
tests = [
    ([14,4,18,1,15], 3, 15, 9, 3),
    ([8,3,16,6,12,20], 15, 13, 11, -1),
    ([1,6,2,14,5,17,4], 16, 9, 7, 2),
    ([128,178,147,165,63,11,150,20,158,144,136],61,170,135,6),
    ([162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98],29,98,80,121),
    ([54,143,27,147,40,199,32,6,47,10,85,142,137,90,163,87,118,176,194,9,21,149,200,120,43,157,84,73,165,56,45,179,124,8,185,105,97,132,112,164,145,197,182,107,133,152,159,7,193,1,42,175,16,67,173,148,62,103,51,158,79,178,146,93,127,129,140,192,89,113,34,187,78,116,91,138,181,153,141,36,170,196,126,110,162,108], 11, 64, 52, 32),
    ([5,2,10,12,18], 8, 6, 16, 2),
    ([1401,832,1344,173,1529,1905,1732,277,1490,650,1577,1886,185,1728,1827,1924,1723,1034,1839,1722,1673,1198,1667,538,911,1221,1201,1313,251,752,40,1378,1515,1789,1580,1422,907,1536,294,1677,1807,1419,1893,654,1176,812,1094,1942,876,777,1850,1382,760,347,112,1510,1278,1607,1491,429,1902,1891,647,1560,1569,196,539,836,290,1348,479,90,1922,111,1411,1286,1362,36,293,1349,667,430,96,1038,793,1339,792,1512,822,269,1535,1052,233,1835,1603,577,936,1684,1402,1739,865,1664,295,977,1265,535,1803,713,1298,1537,135,1370,748,448,254,1798,66,1915,439,883,1606,796], 19, 18, 1540, 120),
    ([1906,1988,1693,483,900,1173,805,1593,1208,1084,300,614,1325,783,1104,1450,311,1506,1388,1567,1497,47,102,338,1937,888,111,195,1041,1570,686,1707,1521,1566,74,1264,667,1486,960,389,442,329,1577,1557,1494,1382,1688,779,484,410,227,1025,1417,1475,1042,1903,1920,1712,870,1813,1137,1732,18,1065,1653,1289,1636,147,1833,1168,1087,1408,881,1129,71,924,1718,1458,371,597,1790,889,414,784,1883,6,1650,1549,552,1233,1467,1514,1568,211,1301,772,377,1751,1699,1701,1214,1874,324,1991,1006,1413,41,289,1274,802,1892,1908,1960,1635,69,423,1795,96,1024,1596,1044,1513,1390,711,1806,1298,968,1160,1232,1315,1646,1178,169,1295,466,44,10,1250,1283,927,49,267,1773,342,1828,1949,1291,244,707,408,798,938,1542,690,639,1148,1081,431,752,120,1125,339,480,247,733,266,596,987,777,214,1005,1687,160,785,1010,1282,1135,922,671,1221,250,1982,398,1959,179,325,1313,577,1053,1436,185,1014,1851,1685,1143,1510,1972,830,681,390,972,1003,844,229,1246,1257,668,1765,619,276,1355,1544,1842,1340,1375,1944,790,606,345,1487,796,1985,1673,1503,180,1642,498,1805,201,104,1658,1633,1507,1142,541,865,1193,485,216,1849,359,1422,391,856,1864,470,1888,1698,760,1778,572,1057,48,189,1086,1704,1258,192,825,585,152,1865,1645,807,225,402,1198,1476,600,1914,975,1378,1190,24,1550,723,696,1131,1831,1880,1029,713,486,126,876,1270,1891,544,61,1356,1676,1239,36,1177,620,1723,1651,1136,141,1889,1123,624,1519,725,241,1253,1119,269,763,1120,1620,642,1713,966,1204,558,1344,550,316,412,886,1309,1648,599,1893,265,258,1561,477,1967,66,1296,75,1628,715,826,1942,1966,1407,159,646,1438,1730,768,411,287,499,467,46,302,661,526,848,1327,1097,166,413,1578,574,1304,925,504,914,978,1352,1103,1859,1167,1318,1454,1990,739,1252,132,529,1622,422,1744,1819,425,945,1767,1791,976,1226,1092,305,479,174,626,1063,662,1948,1978,524,512,1255,651,1678,1059], 806, 1994, 326, -1),
]

for i, (forbidden, a, b, x, ans) in enumerate(tests):
    res = sol.minimumJumps(forbidden, a, b, x)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
