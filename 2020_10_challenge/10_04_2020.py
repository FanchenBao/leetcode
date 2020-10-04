# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """84% ranking

        A solution in discussion suggested that sorting first based on start
        and then reverse on end. This way, when test case 4 will be sorted as
        [[1, 4], [1, 2], [3, 4]]. Since the first interval with the same start
        we encounter will always have the largest end, the check for e > over_e
        will not apply to the intervals with the same start. Thus, we eliminate
        the need to test over_s < s. For details, see Solution2
        """
        intervals.sort(key=lambda inter: inter[0])  # sort based on start
        res = 1
        over_s, over_e = intervals[0]
        for s, e in intervals[1:]:
            if e > over_e:
                if over_s < s:
                    res += 1
                over_s, over_e = s, e
        return res


class Solution2:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """Imporved from the previous solution.
        """
        # sort based on start and reverse on end
        intervals.sort(key=lambda inter: (inter[0], -inter[1]))
        res, over_e = 0, 0
        for s, e in intervals:
            if e > over_e:
                res += 1
                over_e = e
        return res


sol = Solution2()
tests = [
    ([[1, 4], [3, 6], [2, 8]], 2),
    ([[1, 4], [2, 3]], 1),
    ([[0, 10], [5, 12]], 2),
    ([[3, 10], [4, 10], [5, 11]], 2),
    ([[1, 2], [1, 4], [3, 4]], 1),
    ([[1, 2]], 1),
]

for i, (intervals, ans) in enumerate(tests):
    res = sol.removeCoveredIntervals(intervals)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
