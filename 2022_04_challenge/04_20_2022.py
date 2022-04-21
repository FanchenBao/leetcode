# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        """LeetCode 1200

        Sort and traverse adjacent pairs.

        O(nlogn) 344 ms, 64% ranking.
        """
        arr.sort()
        min_abs = math.inf
        res = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] < min_abs:
                res = [[arr[i - 1], arr[i]]]
                min_abs = arr[i] - arr[i - 1]
            elif arr[i] - arr[i - 1] == min_abs:
                res.append([arr[i - 1], arr[i]])
        return res


sol = Solution()
tests = [
    ([4,2,1,3], [[1,2],[2,3],[3,4]]),
    ([1,3,6,10,15], [[1,3]]),
    ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.minimumAbsDifference(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
