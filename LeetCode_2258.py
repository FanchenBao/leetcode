# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        fire_states = []
        M, N = len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    if not fire_states:
                        fire_states.append(set())
                    fire_states[0].add((i, j))
        if not fire_states:
            return 10**9
        queue = fire_states[0]
        while queue:
            temp = set()
            for i, j in queue:
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] == 0 and (ni, nj) not in fire_states[-1]:
                        temp.add((ni, nj))
            queue = temp
            fire_states.append(fire_states[-1].union(queue))
        # binary search
        len_fire_states = len(fire_states)
        lo, hi = -2, len_fire_states
        while lo < hi:
            mid = (lo + hi) // 2
            if mid < 0:
                break
            queue = set([(0, 0)])
            tick = mid + 1
            while queue:
                temp = set()
                for i, j in queue:
                    for di, dj in [(0, 1), (1, 0)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] == 0:
                            if (ni == M - 1 and nj == N - 1 and (M - 1, N - 1) not in fire_states[min(tick - 1, len_fire_states - 1)]) or ((ni, nj) not in fire_states[min(tick, len_fire_states - 1)]):
                                temp.add((ni, nj))
                queue = temp
                tick += 1
                if (M - 1, N - 1) in queue:
                    break
            else:
                hi = mid
                continue
            lo = mid + 1
        return -1 if lo < 0 else lo - 1 if lo < len_fire_states else 10**9


sol = Solution()
tests = [
    ([[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]], 3),
    ([[0,0,0,0],[0,1,2,0],[0,2,0,0]], -1),
    ([[0,0,0],[2,2,0],[1,2,0]], 1000000000),
    ([[0,2,0,0,1],[0,2,0,2,2],[0,2,0,0,0],[0,0,2,2,0],[0,0,0,0,0]], 0),
    ([[0,0],[0,0]], 1000000000),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.maximumMinutes(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
