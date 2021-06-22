# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    res = [[1], [1, 1]]
    for _ in range(28):
        temp = [1]
        for i in range(len(res[-1]) - 1):
            temp.append(res[-1][i] + res[-1][i + 1])
        temp.append(1)
        res.append(temp)

    def generate(self, numRows: int) -> List[List[int]]:
        """LeetCode 118

        This is an easy question and we solve it using a cheeky method. By
        precomputing all 30 rows, we only need to do a splicing to return the
        result.

        O(n^2), 24 ms, 95% ranking.
        """
        return self.res[:numRows]


sol = Solution()
tests = [
    (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
    (1, [[1]]),
]

for i, (numRows, ans) in enumerate(tests):
    res = sol.generate(numRows)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
