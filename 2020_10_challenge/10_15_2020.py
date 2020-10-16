# from pudb import set_trace; set_trace()
from typing import List


class Solution1:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        82% ranking
        """
        def rev(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        size = len(nums)
        rot = k % size
        rev(0, size - 1)  # reverse full list
        rev(0, rot - 1)  # reverse first part
        rev(rot, size - 1)  # reverse second part

        return nums  # have to return to run test cases.


class Solution2:

    def rotate(self, nums: List[int], k: int) -> None:
        """Cyclic replacement. 93% ranking"""
        size = len(nums)
        count, start = 0, 0
        while count < size:
            cur_idx, cur_val = start, nums[start]
            while True:
                next_idx = (cur_idx + k) % size
                nums[next_idx], cur_val = cur_val, nums[next_idx]
                cur_idx = next_idx
                count += 1
                if next_idx == start:
                    break
            start += 1
        return nums  # have to return to run test cases


sol = Solution2()
tests = [
    ([1, 2, 3, 4, 5, 6, 7], 0, [1, 2, 3, 4, 5, 6, 7]),
    ([1, 2, 3, 4, 5, 6, 7], 1, [7, 1, 2, 3, 4, 5, 6]),
    ([1, 2, 3, 4, 5, 6, 7], 2, [6, 7, 1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
    ([1, 2, 3, 4, 5, 6, 7], 4, [4, 5, 6, 7, 1, 2, 3]),
    ([1, 2, 3, 4, 5, 6, 7], 5, [3, 4, 5, 6, 7, 1, 2]),
    ([1, 2, 3, 4, 5, 6, 7], 6, [2, 3, 4, 5, 6, 7, 1]),
    ([1, 2, 3, 4, 5, 6, 7], 7, [1, 2, 3, 4, 5, 6, 7]),
    ([1, 2, 3, 4, 5, 6, 7], 8, [7, 1, 2, 3, 4, 5, 6]),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.rotate(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
