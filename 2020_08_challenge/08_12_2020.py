# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def getRow(self, rowIndex: int) -> List[int]:
        """Programming solution"""
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        curr_row = [1, 1]
        for r in range(2, rowIndex + 1):
            new_row = [1] * (r + 1)
            for i in range(1, r):
                new_row[i] = curr_row[i] + curr_row[i - 1]
            curr_row = new_row
        return curr_row


class Solution2:
    def getRow(self, rowIndex: int) -> List[int]:
        """Binomial expansion solution"""
        frac = [1]
        for i in range(1, 34):
            frac.append(frac[-1] * i)
        half = [frac[rowIndex] // (frac[j] * frac[rowIndex - j]) for j in range(rowIndex // 2 + 1)]
        return half + half[::-1] if rowIndex % 2 else half[:-1] + half[::-1]


class Solution3:
    def getRow(self, rowIndex: int) -> List[int]:
        """O(k) space"""
        res = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            pre = 1
            for j in range(1, i):
                cur = res[j]
                res[j] += pre
                pre = cur
        return res


class Solution4:
    def getRow(self, rowIndex: int) -> List[int]:
        """Better O(k) space"""
        res = [0] * (rowIndex + 1)
        res[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                res[j] += res[j - 1]
        return res



sol = Solution4()

print(sol.getRow(20) == [1, 20, 190, 1140, 4845, 15504, 38760, 77520, 125970, 167960, 184756, 167960, 125970, 77520, 38760, 15504, 4845, 1140, 190, 20, 1])
print(sol.getRow(20))
# # for i, test in enumerate(tests):
# #     (s, wordDict), ans = test
# #     res = sol.wordBreak(s, wordDict)
# #     if res == ans:
# #         print(f'Test {i + 1}: PASS')
# #     else:
# #         print(f'Test {i + 1}: Fail. Received: {res}, Expected: {ans}')