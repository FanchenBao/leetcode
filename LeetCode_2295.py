# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        """The only trick is to use a dict to keep track of the values and its
        index. The index is very important, because we need to use it to
        reconstruct the array for return.

        O(N), 2223 ms, faster than 48.26%
        """
        d = {n: i for i, n in enumerate(nums)}
        for rem, rep in operations:
            d[rep] = d.pop(rem)
        res = [0] * len(nums)
        for n, i in d.items():
            res[i] = n
        return res


sol = Solution()
tests = [
    ([1,2,4,6], [[1,3],[4,7],[6,1]], [3,2,7,1]),
    ([1,2], [[1,3],[2,1],[3,2]], [2, 1]),
]

for i, (nums, operations, ans) in enumerate(tests):
    res = sol.arrayChange(nums, operations)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
