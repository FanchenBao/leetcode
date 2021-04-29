# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right, bisect_left


class Solution1:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """LeetCode 34

        This is more of a cheating method using bisect. The real work should
        be to implement bisect_left and bisect_right from scratch.

        O(log(N)), 84 ms, 68% ranking
        """
        l = bisect_left(nums, target)
        if l == len(nums) or nums[l] != target:
            return [-1, -1]
        return [l, bisect_right(nums, target) - 1]


class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """Non-cheating method. Took us a good while to come up with the correct
        version of binary search.
        """
        N = len(nums)
        if N == 0:
            return [-1, -1]

        def binary_search(left: int, right: int, bias: str) -> int:
            """bias == left means we return the right most index that is smaller
            than the first occurrence of target. bias == right means returning
            the left most index that is larger than the last occurrence of
            target.
            """
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                elif bias == 'left':
                    right = mid - 1
                else:  # bias == 'right'
                    left = mid + 1
            if 0 <= left < N and nums[left] == target:
                return left
            if 0 <= right < N and nums[right] == target:
                return right
            return -1

        l = binary_search(0, N - 1, 'left')
        return [-1, -1] if l < 0 else [l, binary_search(0, N - 1, 'right')]


sol = Solution2()
tests = [
    ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
    ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
    ([], 0, [-1, -1]),
    ([1], 1, [0, 0]),
    ([1], 0, [-1, -1]),
    ([2, 2], 2, [0, 1]),
    ([2, 2], 0, [-1, -1]),
    ([2, 2], 3, [-1, -1]),
]

for i, (nums, target, ans) in enumerate(tests):
    res = sol.searchRange(nums, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
