# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """LeetCode 852

        Binary search.

        O(N), 615 ms, faster than 21.75%
        """
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid - 1] < arr[mid] < arr[mid + 1]:
                lo = mid + 1
            elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
                hi = mid
            else:
                return mid
        return -1


class Solution2:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """Nicer binary search
        """
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < arr[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo
        

sol = Solution2()
tests = [
    ([0,1,0], 1),
    ([0,2,1,0], 1),
    ([0,10,5,2], 1),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.peakIndexInMountainArray(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
