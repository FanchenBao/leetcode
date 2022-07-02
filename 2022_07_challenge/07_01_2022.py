# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """LeetCode 1710

        265 ms, faster than 38.26%
        """
        boxTypes.sort(key=lambda tup: tup[1], reverse=True)
        res = 0
        for c, d in boxTypes:
            if truckSize >= c:
                res += c * d
            else:
                res += truckSize * d
                break
            truckSize -= c
        return res


sol = Solution()
tests = [
    ([[1,3],[2,2],[3,1]], 4, 8),
    ([[5,10],[2,5],[4,7],[3,9]], 10, 91),
    ([[1, 3]], 1, 3),
]

for i, (boxTypes, truckSize, ans) in enumerate(tests):
    res = sol.maximumUnits(boxTypes, truckSize)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
