# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """LeetCode 88
        
        This is not O(1) space, so probably not the official solution. Also we
        struggled a lot with the edges cases where m or n is zero.

        O(M + N) time and space. 63 ms, faster than 26.57%
        """
        if n == 0:
            return
        if m == 0:
            arr = nums2
        else:
            arr = []
            i, j = 0, 0
            nums1[m] = math.inf
            nums2.append(math.inf)
            while i != m or j != n:
                if nums1[i] <= nums2[j]:
                    arr.append(nums1[i])
                    i += 1
                else:
                    arr.append(nums2[j])
                    j += 1
        for i, a in enumerate(arr):
            nums1[i] = a


class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """I checked the solution. The trick is to start nums1 and nums2 from
        the end going backwards. So we are picking the larger value. I didn't
        come up with this last time, nor did I do it this time.

        O(1) space, O(M + N) time. 50 ms, faster than 52.99%
        """
        if n == 0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 or j >= 0:
            if j >= 0 and (i < 0 or nums1[i] < nums2[j]):
                nums1[k] = nums2[j]
                j -= 1
            elif i >= 0 and (j < 0 or nums1[i] >= nums2[j]):
                nums1[k] = nums1[i]
                i -= 1
            k -= 1


        

# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
