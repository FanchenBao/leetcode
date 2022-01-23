# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return [n for n in counter if counter[n] == 1 and n - 1 not in counter and n + 1 not in counter]


sol = Solution()
tests = [
    ([10,6,5,8], [10, 8]),
    ([1,3,5,3], [1,5]),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findLonely(nums)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
