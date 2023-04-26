# from pudb import set_trace; set_trace()
from typing import List
import math
import string


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        N = len(lcp)
        res = [''] * N
        res[0] = 'a'
        if lcp[0][0] != N:
            return ''
        # check symmetric, diagonal, and the max possible value for each cell
        for i in range(N):
            for j in range(i, N):
                if lcp[i][j] != lcp[j][i] or (i > 0 and lcp[i - 1][j - 1] and lcp[i][j] != lcp[i - 1][j - 1] - 1) or lcp[i][j] > N - j or lcp[j][i] > N - i:
                    return ''

        # for row in lcp:
        #     print(row)

        def dp(i: int, j: int) -> bool:
            if j == N or i >= j:
                return True
            if lcp[i][j] > 0:  # match
                k = 0
                while j + k < N:
                    if k < lcp[i][j]:
                        if res[j + k] == '':
                            res[j + k] = res[i + k]
                        elif res[j + k] != res[i + k]:
                            return False
                    elif res[j + k] != '' and res[j + k] == res[i + k]:
                        return False
                    k += 1
                return dp(i + lcp[i][j], j + lcp[i][j])
            else:  # mismatch
                if res[j] != '' and res[j] == res[i]:
                    return False
                if res[j] == '':
                    # try every letter
                    for le in string.ascii_lowercase:
                        if le != res[i]:
                            res[j] = le
                            if dp(i, j + 1) and dp(i + 1, j):  # success
                                break
                            res[j] = ''  # backtrack
                    else:
                        # has tried every letter but still fail
                        return False
            return True
        
        if dp(0, 1):
            return ''.join(res)
        return ''


sol = Solution()
tests = [
    # ([[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]], 'abab'),
    # ([[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]], 'aaaa'),
    # ([[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]], ''),
    # ([[2,0],[1,1]], ''),
    # ([[2,2],[2,1]], ''),
    # ([[4,1,1,1],[1,3,1,1],[1,1,2,1],[1,1,1,1]], ''),
    ([[8,0,0,0,0,1,2,0],[0,7,0,1,1,0,0,1],[0,0,6,0,0,0,0,0],[0,1,0,5,1,0,0,1],[0,1,0,1,4,0,0,1],[1,0,0,0,0,3,1,0],[2,0,0,0,0,1,2,0],[0,1,0,1,1,0,0,1]], "abcbbaab"),
    # ([[14,2,1,0,0,0,1,0,0,0,2,1,0,0],[2,13,1,0,0,0,1,0,0,0,4,1,0,0],[1,1,12,0,0,0,1,0,0,0,1,3,0,0],[0,0,0,11,1,0,0,0,2,1,0,0,2,1],[0,0,0,1,10,0,0,0,1,1,0,0,1,1],[0,0,0,0,0,9,0,1,0,0,0,0,0,0],[1,1,1,0,0,0,8,0,0,0,1,1,0,0],[0,0,0,0,0,1,0,7,0,0,0,0,0,0],[0,0,0,2,1,0,0,0,6,1,0,0,2,1],[0,0,0,1,1,0,0,0,1,5,0,0,1,1],[2,4,1,0,0,0,1,0,0,0,4,1,0,0],[1,1,3,0,0,0,1,0,0,0,1,3,0,0],[0,0,0,2,1,0,0,0,2,1,0,0,2,1],[0,0,0,1,1,0,0,0,1,1,0,0,1,1]], "aaabbcacbbaabb"),
]

for i, (lcp, ans) in enumerate(tests):
    res = sol.findTheString(lcp)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
