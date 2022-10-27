# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter
import numpy as np


class Solution1:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        """LeetCode 835

        Not hard in terms of figuring out a method, but very complicated in
        implementation. First turn both images into bitmaps. Then brute force
        it by traversing all possible overlap states. At each state, compute
        the number of overlapped positions.

        The difficulty lies in accurately finding out the correct bitmap from
        both images at each overlapped state to perform the AND operation.

        O(N^4), 645 ms, faster than 81.87%
        """
        n = len(img1)
        bitmap1 = [sum(v << (n - i - 1) for i, v in enumerate(row)) for row in img1]
        bitmap2 = [sum(v << (n - i - 1) for i, v in enumerate(row)) for row in img2]
        res = 0
        for i in range(2 * n - 1):
            for j in range(2 * n - 1):
                cur = 0
                if i <= n - 1:
                    if j <= n - 1:
                        for ii in range(n - i - 1, n):
                            ol = ((bitmap1[ii] & ((1 << (j + 1)) - 1)) << (n - j - 1)) & (bitmap2[ii - (n - i - 1)])
                            cur += bin(ol).count('1')
                    else:
                        for ii in range(n - i - 1, n):
                            ol = (bitmap1[ii] >> (j - n + 1)) & (bitmap2[ii - (n - i - 1)])
                            cur += bin(ol).count('1')
                else:
                    if j <= n - 1:
                        for ii in range(2 * n - i - 1):
                            ol = ((bitmap1[ii] & ((1 << (j + 1)) - 1)) << (n - j - 1)) & (bitmap2[ii + i - n + 1])
                            cur += bin(ol).count('1')
                    else:
                        for ii in range(2 * n - i - 1):
                            ol = (bitmap1[ii] >> (j - n + 1)) & (bitmap2[ii + i - n + 1])
                            cur += bin(ol).count('1')
                res = max(res, cur)
        return res


class Solution2:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        """Solution No.2 from the official solution.

        Find all the vectors that allows a 1 in img1 to move to another 1 in
        img2. Keep count of this vector. Then if another pair of 1s in the two
        images require the same vector to overlap, then we know using this
        vector to shift the image would result in two overlaps. Therefore, the
        problem is transformed to finding the max number of occurrences of
        any vector that allows the 1s in the two images to overlap.
        """
        n = len(img1)
        ones_1 = []
        ones_2 = []
        for i in range(n):
            for j in range(n):
                if img1[i][j]:
                    ones_1.append((i, j))
                if img2[i][j]:
                    ones_2.append((i, j))
        counter = Counter()
        for i1, j1 in ones_1:
            for i2, j2 in ones_2:
                vec = (i2 - i1, j2 - j1)
                counter[vec] += 1
        return max(counter.values()) if counter else 0


class Solution3:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        """This is the third solution of the official solution, using numpy and
        convolution.

        The problem is basically convolution. And convolution of two matrixes
        can be obtained in numpy via piece-wise product. Thus, we just need to
        expand one of the images. Let the other image move around the expanded
        image,  and then use dot product to find the total number of
        overlapping 1s.
        """
        n = len(img1)
        img1 = np.array(img1)
        img2 = np.array(img2)
        padded = np.pad(img2, n - 1, constant_values=0)
        res = 0
        for i in range(2 * n - 1):
            for j in range(2 * n - 1):
                kernel = padded[i:i + n,j:j + n]
                res = max(res, np.sum(kernel * img1))
        return res


sol = Solution3()
tests = [
    ([[1,1,0],[0,1,0],[0,1,0]], [[0,0,0],[0,1,1],[0,0,1]], 3),
    ([[1]], [[1]], 1),
    ([[0]], [[0]], 0),
    ([[1, 0, 1], [0, 0, 0], [1, 1, 1]], [[1, 1, 0], [0, 0, 0], [1, 1, 1]], 4),
]

for i, (img1, img2, ans) in enumerate(tests):
    res = sol.largestOverlap(img1, img2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
