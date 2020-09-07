# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution1:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        """Brute force. Naive approach
    
        Surprisingly, this brute force passed OJ with runtime 1664 ms.
        """
        A_ones = []
        for i, row in enumerate(A):
            for j, a in enumerate(row):
                if a:
                    A_ones.append((i, j))
        B_ones = set()
        for i, row in enumerate(B):
            for j, b in enumerate(row):
                if b:
                    B_ones.add((i, j))
        n = len(A)
        res = 0
        for h in range(-n + 1, n):
            for v in range(-n + 1, n):
                new_A_ones = set()
                for a_i, a_j in A_ones:
                    new_A_ones.add((a_i + v, a_j + h))
                res = max(res, len(new_A_ones.intersection(B_ones)))
        return res


class Solution2:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        """Find all the ones, then compute the vector needed for two ones to match.
        
        The max occurrence of such vector is the max overlap. Pass OJ with runtime
        652 ms.
        """
        n = len(A)
        A_ones = []
        B_ones = []
        for i in range(n):
            for j in range(n):
                if A[i][j]:
                    A_ones.append([i, j])
                if B[i][j]:
                    B_ones.append([i, j])
        vectors = defaultdict(lambda: 0)
        res = 0
        for a_i, a_j in A_ones:
            for b_i, b_j in B_ones:
                vector = (b_i - a_i, b_j - a_j)
                vectors[vector] += 1
                res = max(res, vectors[vector])
        return res
