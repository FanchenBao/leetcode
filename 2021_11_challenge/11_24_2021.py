# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """LeetCode 986

        Two pointers, one for the firstList and the other secondList. For each
        interval, we first decide whether there is an overlap. If there is no
        overlap, we move the pointer whose interval is lagging behind forward.

        If there are overlap, we compute the overlapping range, and then move
        the pointer whose end range is smaller forward.

        O(min(M, N)), where M is the length of firstList, N secondList.
        179 ms, 26% ranking.
        """
        res = []
        ai, bi = 0, 0
        m, n = len(firstList), len(secondList)
        while ai < m and bi < n:
            sa, ea = firstList[ai]
            sb, eb = secondList[bi]
            if ea < sb:
                ai += 1
            elif eb < sa:
                bi += 1
            else:
                res.append([max(sa, sb), min(ea, eb)])
                if ea <= eb:
                    ai += 1
                else:
                    bi += 1
        return res


class Solution2:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """Official solution. We don't have to check for non-overlapping
        separately.

        Ref: https://leetcode.com/problems/interval-list-intersections/solution/
        """
        res = []
        ai, bi = 0, 0
        m, n = len(firstList), len(secondList)
        while ai < m and bi < n:
            lo, hi = (
                max(firstList[ai][0], secondList[bi][0]),
                min(firstList[ai][1], secondList[bi][1]),
            )
            if lo <= hi:
                res.append([lo, hi])
            if firstList[ai][1] <= secondList[bi][1]:
                ai += 1
            else:
                bi += 1
        return res


sol = Solution2()
tests = [
    ([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]], [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]),
    ([[1,3],[5,9]], [], []),
    ([], [[4,8],[10,12]], []),
]

for i, (firstList, secondList, ans) in enumerate(tests):
    res = sol.intervalIntersection(firstList, secondList)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
