# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution1:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """Iterate from 1 onwards. If we encounter value not in arr, that is
        a missing integer, so we decrement k. If the value is in arr, we move
        the pointer in arr forward. This procedure continues until k is 0,
        which means we have already found the kth missing integer, or arr is
        exhausted, which means the kth missing integer is bigger than all the
        values in arr.

        O(M) where M is the kth missing integer or the largest value in arr,
        52 ms, 64% ranking.
        """
        i, j = 0, 1
        while k and i < len(arr):
            if j < arr[i]:
                k -= 1
            else:
                i += 1
            j += 1
        return j - 1 + k


class Solution2:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """Faster than Solution1, because we are not iterating over each value
        but each element in arr, and compute how many integers have been
        skipped. We decrement k along the way as the number of skipped integers
        are calculated, until the gap is bigger than what k is allowed or arr
        is exhausted. We return j + k - 1.

        O(N) where N is the length of arr, 44 ms, 95% ranking.
        """
        j = 1
        for a in arr:
            if a - j < k:
                k -= a - j
            else:
                break
            j = a + 1
        return j + k - 1


class Solution3:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """I thought my solutions are good enough, yet every time, lee215 came
        up with a better one. Binary search for the win.

        The idea is brilliant. For arr, let index be i. We can say that from
        numbers 1 to a[i] - 1, there are i numbers not missing and a[i] - 1 - i
        numbers missing. Thus, our goal is to find the i such that a[i] - 1 - i
        is larger or equal to k. That means we have found i that contains
        enough missing integers for k. Then our answer is simply i + k (for the
        number i + k, we have k missing numbers and i not missing numbers).

        The question is converted to find a[i] - 1 - i that is larger or equal
        to k. Since a[i] is sorted, this can be solved using binary search.

        O(logN), 44 ms, 95% ranking.
        """
        # note the trick here to use len(arr), because it is possible that
        # there are not enough missing numbers in the arr. So we want l to land
        # outside arr. This won't cause issue because by the time l == r, we
        # already exists.
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            if arr[mid] - 1 - mid < k:
                l = mid + 1
            else:
                r = mid
        return l + k


sol = Solution3()
tests = [
    ([2, 3, 4, 7, 11], 5, 9),
    ([1, 2, 3, 4], 2, 6),
]

for i, (arr, k, ans) in enumerate(tests):
    res = sol.findKthPositive(arr, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
