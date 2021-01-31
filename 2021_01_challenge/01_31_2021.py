# from pudb import set_trace; set_trace()
from typing import List
import bisect


class Solution1:

    def reverse_in_place(self, left: int) -> None:
        right = self.size - 1
        while left < right:
            self.nums[left], self.nums[right] = self.nums[right], self.nums[left]
            left += 1
            right -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """This is most likely a medium problem. The idea is to always delegate
        the problem to a simpler one, which means for any nums, we focus on
        the current idx, and we delegate the problem to nums[idx+1:]. This is
        because, if nums[idx+1:] can resolve the problem already, there is no
        need to involve idx. The criteria that nums[idx+1:] can be resolved is
        that its values are NOT in a descending order. As long as it is not in
        a descending order, there always exists one permutation that is the next
        bigger one. So we keep delegating the problem until we hit a situation
        where the numbers are in descending order.

        When that happens, we must examine the current idx. Here is the main
        logic. If nums[idx] >= nums[idx + 1], that means nums[idx:] is also in
        a descending order. So we have to check nums[idx - 1], which means we
        have to go up in the recursion order. If nums[idx] < nums[idx + 1], that
        means we can find a solution in nums[idx:]. The way to find it is to
        swap nums[idx] with the first number that is bigger than nums[idx], and
        then sort nums[idx+1:] ascendingly. This can be achieved by first
        reversing the order of nums[idx+1:]. Since nums[idx+1:] is already in
        a descending order, reversing it naturally puts them in ascending order.
        Then we can use binary search to find the first number bigger than
        nums[idx] and perform the swap.

        O(N), 52 ms, 14% ranking.
        """
        self.size = len(nums)
        self.nums = nums

        def helper(idx: int) -> bool:
            if idx == self.size - 1:  # the last number
                return False
            if helper(idx + 1):  # the remaining numbers have been organized
                return True
            # The remaining numbers are in descending order
            if nums[idx] >= nums[idx + 1]:
                return False
            # the current number is smaller than some of the remain
            # Reverse the order first, so now from idx + 1 to the end, the
            # numbers are sorted ascendingly
            self.reverse_in_place(idx + 1)
            pos = bisect.bisect_right(nums, nums[idx], lo=idx + 1)
            nums[idx], nums[pos] = nums[pos], nums[idx]
            return True

        if not helper(0):
            self.reverse_in_place(0)


class Solution2:

    def reverse_in_place(self, left: int) -> None:
        right = self.size - 1
        while left < right:
            self.nums[left], self.nums[right] = self.nums[right], self.nums[left]
            left += 1
            right -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """The non-recusive solution. True O(1) space. It has the same logic as
        Solution1, but it avoids the overhead of setting up recursion.

        O(N), 44 ms, 54% ranking. It's O(N) because the binary search is only
        done ONCE.
        """
        self.size = len(nums)
        self.nums = nums

        if self.size == 1:
            return

        for i in range(self.size - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                self.reverse_in_place(i + 1)
                pos = bisect.bisect_right(nums, nums[i], lo=i + 1)
                nums[i], nums[pos] = nums[pos], nums[i]
                return
        self.reverse_in_place(0)


sol = Solution2()
tests = [
    ([1, 2, 3], [1, 3, 2]),
    ([1, 3, 2], [2, 1, 3]),
    ([2, 1, 3], [2, 3, 1]),
    ([2, 3, 1], [3, 1, 2]),
    ([3, 1, 2], [3, 2, 1]),
    ([3, 2, 1], [1, 2, 3]),
    ([1, 1, 5], [1, 5, 1]),
    ([1, 5, 1], [5, 1, 1]),
    ([1], [1]),
]

for i, (nums, ans) in enumerate(tests):
    sol.nextPermutation(nums)
    if nums == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {nums}')
