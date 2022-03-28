# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        res = [[], []]
        for n in set1:
            if n not in set2:
                res[0].append(n)
        for n in set2:
            if n not in set1:
                res[1].append(n)
        return res


sol = Solution()
tests = [
    ([2,4,1,1,6,5], 3),
    ([6,6,5,5,4,1], 0),
    ([6,6,6], 0),
    ([1,2,3], 0),
    ([1,2,1,2,1,1], 3),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.countHillValley(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
