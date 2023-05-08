# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right


class BIT:
    def __init__(self, N: int) -> None:
        self.bit = [0] * (N + 1)

    def update(self, pos: int, val: int) -> None:
        i = pos + 1
        while i < len(self.bit):
            self.bit[i] = max(self.bit[i], val)
            i += (i & -i)

    def query(self, pos: int) -> int:
        i = pos + 1
        res = 0
        while i:
            res = max(res, self.bit[i])
            i -= (i & -i)
        return res


class Solution1:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        """LeetCode 1964

        This problem can be converted into this: given a list and values at some
        positions. Now given a new position, what is the max value among all
        the positions that are smaller than the new position. Find that max
        value, and the new position's value is that max value plus one.

        It is designed for solving using binary indexed tree.

        5004 ms, faster than 6.06%

        The performance is quite bad, because the size of BIT corresponds to the
        difference between the max and min of obstacles, which can be as large
        as 10^7. The meer creation of the bit array can be very slow. Thus,
        there must be a smarter solution.
        """
        min_o, max_o = min(obstacles), max(obstacles)
        max_bit = BIT(max_o - min_o + 1)
        res = []
        for o in obstacles:
            pre_max = max_bit.query(o - min_o)
            max_bit.update(o - min_o, pre_max + 1)
            res.append(pre_max + 1)
        return res


class Solution2:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        """Use the longest increasing subsequence: https://leetcode.com/submissions/detail/768129312/

        This has been one of the toughest problems for me. I have solved LIS
        four times before, but still struggle with its greedy + binary search
        solution. I will not repeat the meaning of the algo here, because the
        doc in the link above has done a decent job of explanation. To use the
        algo for LIS here, we only need to record the length of the LIS ending
        at each obstacle. So essentially, the solucion is the same.

        Notice that this problem is slightly different from LIS, because it is
        finding the longest non-decreasing subsequence. Because of that, we must
        use bisect_right to account for repetition of values. For instance, if
        we have [1,2,3,2], the first three elements give us the aux array
        [1,2,3]. The last 2, with bisect_right, would match to index 2, which is
        currently occupied by value 3. We must swap 3 with 2, because greedily,
        it is a better value to extend the subsequence.

        For LIS, both bisect_left or bisect_right would work. But for longest
        non-decreasing subsequence, only bisect_right works.

        Furthermore, longest non-decreasing subsequence requires that repeated
        value be appended to the aux array as well, whereas in LIS, repeated
        values are ignored.

        O(NlogN), 1552 ms, faster than 66.67% 
        """
        aux = [obstacles[0]]
        res = [1]
        for i in range(1, len(obstacles)):
            idx = bisect_right(aux, obstacles[i])
            if idx == len(aux):
                aux.append(obstacles[i])
            else:
                aux[idx] = obstacles[i]
            res.append(idx + 1)
        return res


sol = Solution2()
tests = [
    ([1,2,3,2], [1,2,3,3]),
    ([2,2,1], [1,2,1]),
    ([3,1,5,6,4,2], [1,1,2,3,2,2]),
    ([2,3,1,5], [1,2,1,3]),
    ([1,3,3,3,2,4], [1,2,3,4,2,5])
]

for i, (obstacles, ans) in enumerate(tests):
    res = sol.longestObstacleCourseAtEachPosition(obstacles)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
