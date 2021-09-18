# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """LeetCode 350

        Two pointer solution, similar to merge sort.

        O(min(M, N) + MlogM + NlogN), 44 ms, 86% ranking.
        """
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        res = []
        while i < m and j < n:
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res


sol = Solution()
tests = [
    ([1, 2, 2, 1], [2, 2], [2, 2]),
    ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9])
]

for i, (nums1, nums2, ans) in enumerate(tests):
    res = sol.intersect(nums1, nums2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
