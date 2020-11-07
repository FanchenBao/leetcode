# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def sum_(self, div, nums) -> int:
        return sum(n // div + 1 if n % div else n // div for n in nums)

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """1224 ms, very bad runtime. Outside the graph area"""
        left, right = min(nums), max(nums)
        while left <= right:
            mid = (left + right) // 2
            sum_ = self.sum_(mid, nums)
            if sum_ > threshold:
                left = mid + 1
            elif sum_ < threshold:
                right = mid - 1
            else:
                break
        while self.sum_(mid, nums) > threshold:
            mid += 1
        while mid and self.sum_(mid, nums) <= threshold:
            mid -= 1
        return mid + 1



class Solution2:
    def sum_(self, div, nums, cache) -> int:
        if div not in cache:
            cache[div] = sum(n // div + 1 if n % div else n // div for n in nums)
        return cache[div]

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """Even with cache, this still results in more than 1200 ms runtime."""
        left, right = min(nums), max(nums)
        cache = {}
        while left <= right:
            mid = (left + right) // 2
            sum_ = self.sum_(mid, nums, cache)
            if sum_ > threshold:
                left = mid + 1
            elif sum_ < threshold:
                right = mid - 1
            else:
                break
        while self.sum_(mid, nums, cache) > threshold:
            mid += 1
        while mid and self.sum_(mid, nums, cache) <= threshold:
            mid -= 1
        return mid + 1


class Solution3:
    def sum_(self, div, nums) -> int:
        return sum(math.ceil(n / div) for n in nums)

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """Without cache, ceil(), and a smarter binary search.
        This solution was obtained from the problem's solution write up. It
        ranked at 58%. Cache is not necessary because we are not repeating on
        the div at all. The smart part is the use of 1 as the left value
        instead of min(nums). This way, we don't have to keep shrinking after
        we are done with the binary search. Furthermore, the return of left is
        also brilliant.
        """
        left, right = 1, max(nums)
        while left <= right:
            mid = (left + right) // 2
            sum_ = self.sum_(mid, nums)
            if sum_ > threshold:
                left = mid + 1
            elif sum_ <= threshold:
                right = mid - 1
        return left


sol = Solution3()
tests = [
    ([1, 2, 5, 9], 6, 5),
    ([2, 3, 5, 7, 11], 11, 3),
    ([19], 5, 4),
    ([4], 100, 1),
]

for i, (nums, threshold, ans) in enumerate(tests):
    res = sol.smallestDivisor(nums, threshold)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
