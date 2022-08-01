# from pudb import set_trace; set_trace()
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        """LeetCode 307

        This is one of those problems that if you know what data structure to
        use, it is not difficult. This one in particular requires Segment Tree,
        or better, Fenway Tree (binary indexed tree). That said, I am still not
        proficient at producing BIT from scratch.

        O(N) for initialization, O(logN) for update and query.

        1630 ms, faster than 92.92%
        """
        self.nums = nums
        self.bit = [0] * (len(nums) + 1)
        for i, n in enumerate(nums):
            self._update(i, n)
        
    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._update(index, delta)

    def _update(self, index: int, delta: int) -> None:
        i = index + 1
        while i < len(self.bit):
            self.bit[i] += delta
            i += (i & -i)

    def _query(self, index: int) -> int:
        i, res = index + 1, 0
        while i:
            res += self.bit[i]
            i -= (i & -i)
        return res

    def sumRange(self, left: int, right: int) -> int:
        return self._query(right) - self._query(left - 1)



sol = Solution()
tests = [
    ([4,2,1,3], [[1,2],[2,3],[3,4]]),
    ([1,3,6,10,15], [[1,3]]),
    ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.minimumAbsDifference(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
