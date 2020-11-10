# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        """53% ranking. Directly manipulating each value."""
        for row in A:
            i, j = 0, len(row) - 1
            while i < j:
                row[i] ^= 1
                row[j] ^= 1
                row[i], row[j] = row[j], row[i]
                i += 1
                j -= 1
            if i == j:
                row[i] ^= 1
        return A


class Solution2:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        """53% ranking. Treat each row as binary number"""
        w = len(A)
        m = 2**w - 1
        flipped = [''.join(str(i) for i in row[::-1]) for row in A]
        return [[int(i) for i in list(format(int(b_str, 2) ^ m, f'0{w}b'))] for b_str in flipped]


class Solution3:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        """94% ranking

        Solution 1 and 2 are both overly convoluted. This is the clean
        solution."""
        return [[i ^ 1 for i in row[::-1]] for row in A]


sol = Solution3()
tests = [
    ([[1, 1, 0], [1, 0, 1], [0, 0, 0]], [[1, 0, 0], [0, 1, 0], [1, 1, 1]]),
    ([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]], [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]),
]

for i, (A, ans) in enumerate(tests):
    res = sol.flipAndInvertImage(A)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
