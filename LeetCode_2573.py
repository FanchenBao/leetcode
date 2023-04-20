# from pudb import set_trace; set_trace()
from typing import List
import math



class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        N = len(lcp)
        res = [0] * N
        res[0] = 97
        # check diagonal
        for i in range(N):
            if lcp[i][i] != N - i:
                return ''
        # check symmetric
        for i in range(N):
            for j in range(i + 1, N):
                if lcp[i][j] != lcp[j][i] or lcp[i][j] > N - j or lcp[j][i] > N - i:
                    return ''
        for j in range(1, N):
            cand = 97
            for i in range(j):
                if lcp[i][j] == 0:
                    if cand == res[i]:
                        cand = res[i] + 1
                else:
                    if res[i] >= cand:
                        cand = res[i]
                    else:
                        return ''
            if cand > 122:  # 'z'
                return -1
            res[j] = cand
        return ''.join(chr(r) for r in res)


sol = Solution()
tests = [
    ([[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]], 'abab'),
    ([[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]], 'aaaa'),
    ([[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]], ''),
    ([[2,0],[1,1]], ''),
    ([[2,2],[2,1]], ''),
    ([[4,1,1,1],[1,3,1,1],[1,1,2,1],[1,1,1,1]], ''),
]

for i, (lcp, ans) in enumerate(tests):
    res = sol.findTheString(lcp)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
