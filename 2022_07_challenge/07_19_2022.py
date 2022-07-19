# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """LeetCode 118

        30 ms, faster than 95.07%
        """
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        for i in range(3, numRows + 1):
            tmp = [1]
            for j in range(1, len(res[-1])):
                tmp.append(res[-1][j] + res[-1][j - 1])
            tmp.append(1)
            res.append(tmp)
        return res


sol = Solution()
tests = [
    (5, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]),
    (6, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1]]),
    (7, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1]]),
]

for i, (numRows, ans) in enumerate(tests):
    res = sol.generate(numRows)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
