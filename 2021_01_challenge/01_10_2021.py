# from pudb import set_trace; set_trace()
from typing import List
from sortedcontainers import SortedList
import bisect


class Solution1:
    def createSortedArray(self, instructions):
        """Using the Binary Indexed Tree method. Adapted from this discussion
        post: https://leetcode.com/problems/create-sorted-array-through-instructions/discuss/927531/JavaC%2B%2BPython-Binary-Indexed-Tree

        O(NlogM), where N is the size of instructions and M the largest value
        in instructions. 4244 ms, 77% ranking.
        """
        m = max(instructions)
        bit = [0] * (m + 1)  # binary indexed tree

        def update(x):
            """Update the number of elements from 1 to the current value x"""
            while x <= m:
                bit[x] += 1
                x += (x & (-x))  # go to parent

        def get(x):
            """Get the number of elements from 1 to the current value x """
            res = 0
            while x > 0:
                res += bit[x]
                x -= (x & (-x))  # go to parent
            return res

        res = 0
        for i, ins in enumerate(instructions):
            res += min(get(ins - 1), i - get(ins))
            update(ins)

        return res % (10**9 + 7)


class Solution2:
    def createSortedArray(self, instructions):
        """Use the slightly cheating method of SortedList.
        From discussion post:https://leetcode.com/problems/create-sorted-array-through-instructions/discuss/1010298/Python-Sorted-List-O(n-log-n)-solution-explained

        Approximately O(NlogN). The add() function runs actually in O(N^(1/3))
        according to the documentation of Sorted Containers. So the actual
        runtime is slower than Solution1. 6080 ms, 42% ranking.
        """
        res = 0
        slst = SortedList()
        for i, ins in enumerate(instructions):
            res += min(slst.bisect_left(ins), i - slst.bisect_right(ins))
            slst.add(ins)
        return res % (10**9 + 7)


class Solution3:
    def createSortedArray(self, instructions):
        """bisect.insort()

        TLE
        """
        res = 0
        nums = []
        for i, ins in enumerate(instructions):
            res += min(bisect.bisect_left(nums, ins), i - bisect.bisect_right(nums, ins))
            bisect.insort(nums, ins)
        return res % (10**9 + 7)


class Solution4:
    def createSortedArray(self, instructions):
        """slice trick to insert.

        Supposed to be O(N^2log(N)), but the slice trick is very fast. 4764 ms,
        66% ranking.
        """
        res = 0
        nums = []
        for i, ins in enumerate(instructions):
            l, r = bisect.bisect_left(nums, ins), bisect.bisect_right(nums, ins)
            res += min(l, i - r)
            nums[r:r] = [ins]
        return res % (10**9 + 7)


sol = Solution4()
tests = [
    ([1, 5, 6, 2], 1),
    ([1, 2, 3, 6, 5, 4], 3),
    ([1, 3, 3, 3, 2, 4, 2, 1, 2], 4),
]

for i, (instructions, ans) in enumerate(tests):
    res = sol.createSortedArray(instructions)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
