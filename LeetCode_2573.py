# from pudb import set_trace; set_trace()
from typing import List
import math
import string



class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        N = len(lcp)
        res = [''] * N
        res[0] = 'a'
        # check diagonal
        for i in range(N):
            if lcp[i][i] != N - i:
                return ''
        # check symmetric and the max possible value for each cell
        for i in range(N):
            for j in range(i + 1, N):
                if lcp[i][j] != lcp[j][i] or lcp[i][j] > N - j or lcp[j][i] > N - i:
                    return ''

        def dp(j: int) -> bool:
            if j == N:
                return True
            for i in range(j):
                if lcp[i][j] > 0:  # match
                    if i!= 0 and
                    for k in range(lcp[i][j]):
                        if res[j + k] == '':
                            res[j + k] = res[i + k]
                        elif res[j + k] != res[i + k]:
                            return False
                else:  # mismatch
                    if res[j] != '' and res[j] == res[i]:
                        return False
                    if res[j] == '':
                        # try every letter
                        for le in string.ascii_lowercase:
                            if le != res[i]:
                                res[j] = le
                                if dp(j + 1):  # success
                                    break
                                res[j] = ''  # backtrack
                        else:
                            # has tried every letter but still fail
                            return False
                        break


        # examine lcp diagonally from top left to bottom right. 
        for k in range(1, N):
            for i in range(N - k):
                j = i + k
                if lcp[i][j] > 0:
                    # For each lcp[i][j], if it is larger than 0, then it must
                    # be one smaller than lcp[i - 1][j - 1] (unless i == 0) or
                    # lcp[i - 1][j - 1] == 0 Also, when lcp[i][j] > 0, we must
                    # have res[i] == res[j]. This is another place where check
                    # can be made.
                    if i == 0 or lcp[i - 1][j - 1] == lcp[i][j] + 1 or lcp[i - 1][j - 1] == 0:
                        if res[j] == '':
                            res[j] = res[i]
                        elif res[j] != res[i]:
                            return ''
                    else:
                        return ''
                else:
                    # If lcp[i][j] == 0, that means res[i] != res[j]. This is
                    # where we can check for accuracy. And also since we are
                    # producing res from left to right, any mismatch will be
                    # 'b' if the mismatch is 'a', or 'a' if the mismatch is 'b'
                    if res[j] == '':
                        res[j] = 'a' if res[i] == 'b' else 'b'
                    elif res[j] == res[i]:
                        return ''
        return ''.join(res)


sol = Solution()
tests = [
    ([[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]], 'abab'),
    ([[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]], 'aaaa'),
    ([[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]], ''),
    ([[2,0],[1,1]], ''),
    ([[2,2],[2,1]], ''),
    ([[4,1,1,1],[1,3,1,1],[1,1,2,1],[1,1,1,1]], ''),
    ([[8,0,0,0,0,1,2,0],[0,7,0,1,1,0,0,1],[0,0,6,0,0,0,0,0],[0,1,0,5,1,0,0,1],[0,1,0,1,4,0,0,1],[1,0,0,0,0,3,1,0],[2,0,0,0,0,1,2,0],[0,1,0,1,1,0,0,1]], "abcbbaab"),
]

for i, (lcp, ans) in enumerate(tests):
    res = sol.findTheString(lcp)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
