# from pudb import set_trace; set_trace()
from typing import List
from itertools import groupby


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        """Use groupby

        O(N), 65 ms, faster than 21.44%
        """
        k = -1
        for kk, g in groupby(num):
            if len(list(g)) >= 3 and int(kk) > k:
                k = int(kk)
        return str(k) * 3 if k >= 0 else ""

       

# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
