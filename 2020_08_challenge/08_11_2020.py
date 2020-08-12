from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def hIndex(self, citations: List[int]) -> int:
        """Straight forward sorting"""
        for i, cit in enumerate(sorted(citations)):
            if len - i >= cit:
                return cit


class Solution2:
    def hIndex(self, citations: List[int]) -> int:
        """Bucket sort"""
        buckets = [0] * (max(citations) + 1)
        for cit in citations:
            buckets[cit] += 1
        acc = 0
        res = 0
        for cit in range(len(buckets) - 1, -1, -1):
            if buckets[cit]:
                acc += buckets[cit]
                if cit >= acc:
                    res = acc
                else:
                    break
        return res


sol = Solution2()

print(sol.hIndex([1, 3, 0, 7, 5, 9, 7, 6, 9, 0, 8, 7, 6, 7, 8, 2, 2, 2, 10, 1, 9, 6, 5, 9, 3, 6, 2, 3, 2, 6, 10, 10, 10, 1, 1, 9, 6, 1, 1, 10, 7, 6, 9, 5, 10, 3, 3, 4, 9, 0, 10, 0, 3, 8, 1, 0, 3, 5, 4, 8, 1, 6, 4, 7, 3, 4, 7, 5, 4, 10, 9, 0, 6, 6, 0, 7, 1, 10, 8, 5, 4, 8, 9, 3, 4, 5, 3, 5, 5, 4, 4, 3, 4, 10, 9, 6, 5, 3, 2, 10]))

# # for i, test in enumerate(tests):
# #     (s, wordDict), ans = test
# #     res = sol.wordBreak(s, wordDict)
# #     if res == ans:
# #         print(f'Test {i + 1}: PASS')
# #     else:
# #         print(f'Test {i + 1}: Fail. Received: {res}, Expected: {ans}')