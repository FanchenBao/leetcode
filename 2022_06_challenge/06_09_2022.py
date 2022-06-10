# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """LeetCode 167

        Use binary search to achieve O(1) extra space.

        O(NlogN) 257 ms, faster than 13.28% 
        """
        for i, n in enumerate(numbers):
            idx = bisect_right(numbers, target - n)
            if numbers[idx - 1] == target - n and idx - 1 != i:
                return [i + 1, idx]
        

sol = Solution()
tests = [
    ([2,7,11,15], 9, [1, 2]),
    ([2,3,4], 6, [1, 3]),
    ([-1,0], -1, [1, 2]),
]

for i, (numbers, target, ans) in enumerate(tests):
    res = sol.twoSum(numbers, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
