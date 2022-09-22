# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """LeetCode 985

        Straightforward solution. Follow the instructions and analyze each
        query on its own.

        O(N), 516 ms, faster than 98.72%
        """
        s = sum(v for v in nums if v % 2 == 0)
        res = []
        for v, idx in queries:
            new_n = nums[idx] + v
            if new_n % 2 == 0:
                if nums[idx] % 2:
                    s += new_n
                else:
                    s += new_n - nums[idx]
            elif nums[idx] % 2 == 0:  # new_n is odd but nums[idx] is even
                s -= nums[idx]
            nums[idx] = new_n
            res.append(s)
        return res


class Solution2:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """Official solution. Better implementation
        """
        s = sum(v for v in nums if v % 2 == 0)
        res = []
        for v, idx in queries:
            if nums[idx] % 2 == 0:
                s -= nums[idx]
            nums[idx] += v
            if nums[idx] % 2 == 0:  # new_n is odd but nums[idx] is even
                s += nums[idx]
            res.append(s)
        return res        


sol = Solution2()
tests = [
    ([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]], [8,6,2,4]),
    ([1], [[4,0]], [0]),
]

for i, (nums, queries, ans) in enumerate(tests):
    res = sol.sumEvenAfterQueries(nums, queries)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
