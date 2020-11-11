# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def dist(self, p: List[int], q: List[int]) -> int:
        return (p[0] - q[0])**2 + (p[1] - q[1])**2

    def is_square(self, a: int, b: int, c: int, d: int, dists: List[List[int]]) -> bool:
        """
        a, b, c, d are index for the points.
        a b
        c d
        """
        # need to check for d_ab not being zero
        return all([
            dists[a][b],
            dists[a][b] == dists[a][c] == dists[b][d] == dists[c][d],
            dists[a][d] == dists[b][c] == 2 * dists[a][b],
        ])


    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        """44% ranking"""
        dists = [[0] * 4 for _ in range(4)]
        points = [p1, p2, p3, p4]
        for i in range(4):
            for j in range(4):
                dists[i][j] = self.dist(points[i], points[j])
        return any([
            self.is_square(0, 1, 2, 3, dists),
            self.is_square(0, 1, 3, 2, dists),
            self.is_square(0, 2, 3, 1, dists),
        ])


# sol = Solution3()
# tests = [
#     # ([1, 2, 3, 1], 3, 0, True),
#     # ([1, 0, 1, 1], 1, 2, True),
#     ([1, 5, 9, 1, 5, 9], 2, 3, False),
#     # ([1, 4, 9, 1, 4, 9], 1, 3, True),
#     # ([-1, -1], 1, -1, False),
#     # ([1, 3, 6, 2], 1, 2, True),
# ]

# for i, (nums, k, t, ans) in enumerate(tests):
#     res = sol.containsNearbyAlmostDuplicate(nums, k, t)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
