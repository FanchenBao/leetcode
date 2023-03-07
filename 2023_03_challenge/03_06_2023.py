# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_left


class Solution1:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """LeetCode 1539

        Binary search of binary search.

        O(2logN), 54 ms, faster than 65.76%
        """
        lo, hi = 0, 2001
        while lo < hi:
            mid = (lo + hi) // 2
            # use bisect_left to handle the situation where mid is in arr
            idx = bisect_left(arr, mid)
            if mid - idx > k:
                hi = mid
            else:
                lo = mid + 1
        return lo - 1


class Solution2:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """Better binary search from the last solution 2 years ago.

        arr[i] - 1 is the number of positive integers from 1 to arr[i] - 1
        i is the number of positive integers in arr from arr[0] to arr[i - 1]
        Thus, arr[i] - 1 - i is the number of positive integers missing up to
        arr[i]
        """
        lo, hi = 0, len(arr)  # they are indices
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] - 1 - mid < k:
                lo = mid + 1
            else:
                hi = mid
        # lo is the number of not-missing integers. Suppose x is the kth missing
        # integer, then from 1 to x, there are lo number of not-missing integers
        # and k missing integers. Thus, x - 1 + 1 = lo + k ==> x = lo + k
        return lo + k
        

sol = Solution2()
tests = [
    ([2,3,4,7,11], 5, 9),
    ([1,2,3,4], 2, 6),
    ([2], 1, 1),
]

for i, (arr, k, ans) in enumerate(tests):
    res = sol.findKthPositive(arr, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
