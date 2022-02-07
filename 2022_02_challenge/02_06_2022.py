# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        """LeetCode 80

        Keep a sliding window of bad elements. Each time a good element is
        encountered, swap the beginning of the window with the good element,
        and progress the window's boundary. If a bad element is encountered,
        only progress the right boundary of the window.

        One caveat is to use a separate variable to store the previous value,
        because once the swap is done, the element at nums[i - 1] is no longer
        the real previous value.

        O(N), 92 ms, 27% ranking.
        """
        lo, hi = 1, 1
        cnt = 1
        pre = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != pre:
                pre = nums[i]
                cnt = 1
                nums[lo], nums[i] = nums[i], nums[lo]
                lo += 1
            else:
                cnt += 1
                if cnt <= 2:
                    nums[lo], nums[i] = nums[i], nums[lo]
                    lo += 1
            hi += 1
        return lo


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        """This is from the solution I obtained from Mr. Pochmann in 2020-12-11
        The core idea is not quite the same. Here, we use i to represent the
        beginning of the bad window. As we iterate through n, for each element
        encountered, we check n == nums[i - 2]. Because i is the start of the
        bad element, then if n == nums[i - 2], that means n == nums[i - 1] ==
        nums[i - 2], which is a violation. In this case, n is bad, so we should
        not do anything with it. On the other hand, if n != nums[i - 2], that
        means n is a good element, so we put nums[i] = n, which is to place
        the good element in its correct position.

        O(N), 78 ms, 42% ranking.
        """
        i = 0
        for n in nums:
            if i < 2 or n != nums[i - 2]:  # good cases
                nums[i] = n  # instead of swapping, just assign the good element to its correct position
                i += 1
        return i

        
sol = Solution2()
tests = [
    ([1,1,1,2,2,3], 5, [1,1,2,2,3]),
    ([0,0,1,1,1,1,2,3,3], 7, [0,0,1,1,2,3,3]),
    ([1,1,1,2,2,2,3,3,3], 6, [1,1,2,2,3,3]),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.removeDuplicates(nums)
    if res == k and nums[:k] == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {k, ans}, Res: {res, nums}')
