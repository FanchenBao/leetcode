# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        even, odd = Counter(), Counter()
        evencnt = (len(nums) + 1) // 2
        oddcnt = len(nums) - evencnt
        for i, n in enumerate(nums):
            if i % 2:
                odd[n] += 1
            else:
                even[n] += 1
        even_most_common = even.most_common(2)
        while len(even_most_common) != 2:
            even_most_common.append((0, 0))
        odd_most_common = odd.most_common(2)
        while len(odd_most_common) != 2:
            odd_most_common.append((0, 0))
        if even_most_common[0][0] != odd_most_common[0][0]:
            return evencnt - even_most_common[0][1] + oddcnt - odd_most_common[0][1]
        return min(
            evencnt - even_most_common[0][1] + oddcnt - odd_most_common[1][1],
            evencnt - even_most_common[1][1] + oddcnt - odd_most_common[0][1],
        )


sol = Solution()
tests = [
    ([3,1,3,2,4,3], 3),
    ([1,2,2,2,2], 2),
    ([1], 0),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.minimumOperations(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
