# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution1:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """LeetCode 909

        My god. Haven't pulled three-hour effort for a long time. This one is
        not really difficult, but I just didn't think of BFS at all. Have to
        resort to the official solution for the BFS idea, but this
        implementation still sucks.

        9544 ms, faster than 5.17%
        """
        N = len(board)
        tgt = N * N
        dj = [1] * N
        for k in range(N - 2, -1, -2):
            dj[k] = -1
        m = {}
        lab, j = 1, 0
        for i in range(N - 1, -1, -1):
            while True:
                m[lab] = [i, j]
                if 0 <= j + dj[i] < N:
                    j += dj[i]
                    lab += 1
                else:
                    lab += 1
                    break

        visited = [[[0, 0] for _ in range(N)] for _ in range(N)]
        queue = [[N - 1, 0, 0, 1]]  # [i, j, is_jump, label]
        steps = 0
        while queue:
            tmp = []
            # print(queue)
            for i, j, is_jump, label in queue:
                # print(i, j, is_jump, label)
                visited[i][j][is_jump] = 1
                for i in range(1, 7):
                    next_label = min(tgt, label + i)
                    if tgt == next_label:
                        return steps + 1
                    ni, nj = m[next_label]
                    if board[ni][nj] < 0 and not visited[ni][nj][0]:
                        tmp.append([ni, nj, 0, next_label])
                    elif board[ni][nj] == tgt:
                        return steps + 1
                    elif board[ni][nj] > 0:
                        nni, nnj = m[board[ni][nj]]
                        if not visited[nni][nnj][1]:
                            tmp.append([nni, nnj, 1, board[ni][nj]])
            steps += 1
            queue = tmp

        return -1


class Solution2:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """Let's implement it again.

        Two main differences compared to Solution1.

        1. We can BFS using just the labels. The row and col coordinates are not
        necessary. Of course, we must create a mapping between the labels and
        the board values, but after that, we can very easily move forward in
        labels, compared to computing the next cell's row and col.
        2. There is no need to consider whether the move to the next cell is
        a jump or not. When we visit a cell, it is guaranteed to be a
        non-jumping cell, regardless of its board values. This is because we
        already handle the jumping during the cell visit, such that the cells
        pushed to the queue is always a non-jumping cell.

        O(N^2) 1026 ms, faster than 5.37%
        """
        N = len(board)
        tgt = N * N
        m = [0]  # mapping between a label and its associated value on board
        j, dj = 0, 1
        for i in range(N - 1, -1, -1):
            while 0 <= j < N:
                m.append(board[i][j])
                j += dj
            j -= dj
            dj *= -1
        
        queue = [1]  # [label]
        visited = set()
        steps = 0
        while queue:
            tmp = []
            for lab in queue:
                visited.add(lab)
                for i in range(1, min(tgt - lab + 1, 7)):
                    next_label = lab + i
                    if next_label == tgt:
                        return steps + 1
                    if m[next_label] < 0 and next_label not in visited:
                        tmp.append(next_label)
                    elif m[next_label] == tgt:
                        return steps + 1
                    elif m[next_label] not in visited:
                        tmp.append(m[next_label])
            steps += 1
            queue = tmp
        return -1



        

sol = Solution2()
tests = [
    ([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]], 4),
    ([[-1,-1],[-1,3]], 1),
    ([[-1,-1,-1],[-1,9,8],[-1,8,9]], 1),
    ([[1,1,-1],[1,1,1],[-1,1,1]], -1),
    ([[-1,4,-1],[6,2,6],[-1,3,-1]], 2),
    ([[-1,1,2,-1],[2,13,15,-1],[-1,10,-1,-1],[-1,6,2,8]], 2),
    ([[-1,42,12,-1,1,-1,-1],[-1,-1,5,-1,-1,46,44],[18,22,6,39,-1,-1,-1],[-1,-1,40,-1,-1,-1,37],[49,38,24,-1,14,29,-1],[-1,-1,6,-1,-1,-1,20],[-1,-1,12,10,-1,5,26]], 2),
]

for i, (board, ans) in enumerate(tests):
    res = sol.snakesAndLadders(board)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
