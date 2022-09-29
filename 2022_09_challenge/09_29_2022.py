# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right


class Solution1:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """LeetCode 658

        Binary search and "merge sort".

        O(NlogN) 332 ms, faster than 87.78%
        """
        idx = bisect_right(arr, x)
        i, j = idx - 1, idx
        res = []
        while k and i >= 0 and j < len(arr):
            if x - arr[i] < arr[j] - x:
                res.append(arr[i])
                i -= 1
            elif x - arr[i] > arr[j] - x:
                res.append(arr[j])
                j += 1
            else:
                if arr[i] <= arr[j]:
                    res.append(arr[i])
                    i -= 1
                else:
                    res.append(arr[j])
                    j += 1
            k -= 1
        while k and i >= 0:
            res.append(arr[i])
            i -= 1
            k -= 1
        while k and j < len(arr):
            res.append(arr[j])
            j += 1
            k -= 1
        return sorted(res)


class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """Smart binary search

        First observation is that the returned list must be a subarray of arr,
        because otherwise we won't be having the closest values.

        Second, since we are looking for a subarray of size k, we only need to
        locate the left bound of the subarray. We use binary search to find
        such left bound.

        Each time, we compare x - arr[mid] (distance between the first element
        of the subarray and x) and arr[mid + k] - x (distance between the
        element to the right of the subarray and x).

        If x is to the right of the subarray, then x - arr[mid] must be larger
        than arr[mid + k] - x, we should set lo = mid + 1

        If x is to the left of the subarray, then x - arr[mid] must be smaller
        than arr[mid + k] - x, we should set hi = mid

        If x is inside the subarray, then the same applies, because if x -
        arr[mid] is smaller than arr[mid + k] - x, then the subarray migth have
        room to move left wards. Otherwie, the subarray might have room to move
        right wards.

        If the difference is the same, we always move left wards because we
        want to favor the smaller values.

        O(logN + K), 301 ms, faster than 95.42%
        """
        lo, hi = 0, len(arr) - k
        while lo < hi:
            mid = (lo + hi) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                hi = mid
            else:
                lo = mid + 1
        return arr[lo:lo + k]


sol = Solution2()
tests = [
    ([1,2,3,4,5], 4, 3, [1, 2, 3, 4]),
    ([1,2,3,4,5], 4, -1, [1, 2, 3, 4]),
    ([1,3,3,4,5], 4, 3, [1, 3, 3, 4]),
]

for i, (arr, k, x, ans) in enumerate(tests):
    res = sol.findClosestElements(arr, k, x)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
