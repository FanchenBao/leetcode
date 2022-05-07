# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """LeetCode 1679

        Finally an easy one after a pretty bad running towards the end of April
        This one is very straightforward. No explanation needed.

        715 ms, faster than 79.33%
        """
        counter = Counter(nums)
        res = 0
        for a in counter.keys():
            if a == k - a:
                res += counter[a] // 2
                counter[a] = 0
            elif counter[a] and counter[k - a]:
                c = min(counter[a], counter[k - a])
                res += c
                counter[a] -= c
                counter[k - a] -= c
        return res


class Solution2:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """The smartass solution deserves to be submitted again.
        """
        c = Counter(nums)
        return sum(min(c[a], c[k - a]) for a in c.keys()) // 2

        
sol = Solution2()
tests = [
    ([1,2,3,4], 5, 2),
    ([3,1,3,4,3], 6, 1),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.maxOperations(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
