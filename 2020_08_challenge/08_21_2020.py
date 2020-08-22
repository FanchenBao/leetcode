# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        """Start from both ends and swap. Similar to quicksort but runs in O(n)"""
        f, b = 0, len(A) - 1
        while f < b:
            if A[f] % 2 == 0:
                f += 1
                continue
            if A[b] % 2 == 1:
                b -= 1
                continue
            A[f], A[b] = A[b], A[f]
            f += 1
            b -= 1
        return A


class Solution2:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        """A smarter swap.

        Instead of going from both ends towards the center, we go from the
        beginning, but keep one idx faster than the other. We swap the faster
        idx value with the slower one if the faster one encounters an even
        number.
        """
        i, j = 0, 0
        while j < len(A):
            if A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
            j += 1
        return A