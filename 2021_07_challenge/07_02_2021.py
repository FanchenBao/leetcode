# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right
import math


class Solution1:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """LeetCode 658

        Binary search to locate x in arr, then we go left of x and right of x
        one by one, comparing the difference with x. If the left candidate is
        closer to x, we include it and move more to the left. The same goes with
        the right candidate. The process ends when we have accumulated enough
        closest elements.

        O(log(N) + k), where N is the length of arr. 296 ms, 67% ranking.
        """
        sm, lg = [], []
        mid = bisect_right(arr, x)
        left, right = mid - 1, mid
        n = len(arr)
        while len(sm) + len(lg) < k:
            cand_l = arr[left] if left >= 0 else -math.inf
            cand_r = arr[right] if right < n else math.inf
            if x - cand_l <= cand_r - x:
                sm.append(cand_l)
                left -= 1
            else:
                lg.append(cand_r)
                right += 1
        return sm[::-1] + lg


class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """This is the same solution as mine, but with better implementation.

        Ref: https://leetcode.com/problems/find-k-closest-elements/solution/

        Notice that we don't have to use extra space to save the candidates,
        because the resulting array must be bounded by left and right pointers.
        """
        mid = bisect_right(arr, x)
        left, right = mid - 1, mid
        n = len(arr)
        while right - left - 1 < k:
            cand_l = arr[left] if left >= 0 else -math.inf
            cand_r = arr[right] if right < n else math.inf
            if x - cand_l <= cand_r - x:
                left -= 1
            else:
                right += 1
        return arr[left + 1:right]


class Solution3:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """Smarter binary search. Search only for the left bound.

        Ref: https://leetcode.com/problems/find-k-closest-elements/solution/
        """
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            # There is an extra trick in the if statement. Given arr[mid] and
            # arr[mid + k], there are three positions where x can be. If x is
            # in between arr[mid] and arr[mid + k], then we compare x - arr[mid]
            # and arr[mid + k] - x, no issue.
            # If x is larger than arr[mid + k], then we must gravitate towards
            # arr[mid + k]. Interestingly, comparing x - arr[mid] and arr[mid + k]
            # - x does indeed help us gravitate towards arr[mid + k].
            # Similarly, if x is smaller than arr[mid], the same comparision
            # will also allow us to gravitate towards arr[mid].
            if x - arr[mid] <= arr[mid + k] - x:
                # left bound is at most mid
                right = mid
            else:  # left bound is at least mid + 1
                left = mid + 1
        return arr[left:left + k]


sol = Solution3()
tests = [
    # ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
    # ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4]),
    ([1, 1, 2, 2, 2, 2, 2, 3, 3], 3, 3, [2, 3, 3]),
]

for i, (arr, k, x, ans) in enumerate(tests):
    res = sol.findClosestElements(arr, k, x)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
