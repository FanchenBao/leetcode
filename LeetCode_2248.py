# from pudb import set_trace; set_trace()
from typing import List
from functools import reduce
from collections import Counter


class Solution1:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        """Naive solution, but perfectly fine for a contest.

        125 ms, faster than 17.50%
        """
        return sorted(reduce(lambda val, ele: val.intersection(ele), [set(row) for row in nums]))


class Solution2:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        """Use set.intersection(set1, set2, ...) to avoid using reduce
        This is from lee215's comment
        https://leetcode.com/problems/intersection-of-multiple-arrays/discuss/1977782/Python3-1-LINE-Solution-oror-Simple-Explanation/1364937

        74 ms, faster than 83.32%
        """
        return sorted(set.intersection(*(set(row) for row in nums)))


class Solution3:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        """Using counter"""
        return sorted(k for k, v in reduce(lambda val, ele: val + Counter(ele), nums, Counter()).items() if v == len(nums))
        

sol = Solution3()
tests = [
    ([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], [3, 4]),
    ([[1,2,3],[4,5,6]], []),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.intersection(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
