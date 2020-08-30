# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def flip(self, A: List[int], k: int) -> None:
        f = 0
        b = k
        while f < b:
            A[f], A[b] = A[b], A[f]
            f += 1
            b -= 1

    def pancakeSort(self, A: List[int]) -> List[int]:
        """Most generic solution"""
        res = []
        for i in range(len(A) - 1, -1, -1):
            idx = A[:i + 1].index(max(A[:i + 1]))
            if idx != i:
                res += [idx + 1, i + 1]
                self.flip(A, idx)
                self.flip(A, i)
        return res


class Solution2:
    def flip(self, k: int) -> None:
        if k <= 0:
            return
        f = 0
        b = k
        while f < b:
            self.A[f], self.A[b] = self.A[b], self.A[f]
            f += 1
            b -= 1
        self.res.append(k + 1)

    def swap(self, i: int, j: int) -> None:
        """i and j are indices"""
        self.flip(j)
        self.flip(j - i)
        self.flip(j - i - 1)
        self.flip(j - i - 2)
        self.flip(j - i - 1)
        self.flip(j)

    def pancakeSort(self, A: List[int]) -> List[int]:
        """Interesting solution to swap numbers at given position without
        changing the order of the remaining.
        """
        self.A = A
        self.res = []
        i = 0
        while i < len(A):
            if A[i] != i + 1:
                self.swap(i, A[i] - 1) if A[i] > i + 1 else self.swap(A[i] - 1, i)
                print(self.A)
            else:
                i += 1
        return self.res


sol = Solution2()
A = [4, 1, 5, 3, 2]
print(sol.pancakeSort(A))