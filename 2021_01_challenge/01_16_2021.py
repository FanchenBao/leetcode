# from pudb import set_trace; set_trace()
from typing import List
from random import randint


class Solution0:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Got an easy pass today. This is easier than the easy level.

        Update: This question is medium level, which tells me that sorting the
        list is not the intended solution. I need to come up with a non-sorting
        method to solve the problem.
        
        O(NlogN, 84 ms, 27% ranking)
        """
        nums.sort()
        return nums[-k]


class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Quick sort based selection algo.

        O(NlogN), 1212 ms, 12% arnking.
        """
        size = len(nums)

        def locate_pivot(l: int, r: int) -> int:
            l_ = l
            pivot = nums[l]
            while l < r:
                while l < size and nums[l] <= pivot:
                    l += 1
                while r >= 0 and nums[r] > pivot:
                    r -= 1
                if l < r:
                    nums[l], nums[r] = nums[r], nums[l]
            nums[r], nums[l_] = nums[l_], nums[r]
            return r

        l, r = 0, size - 1
        while True:
            piv = locate_pivot(l, r)
            if size - piv == k:
                return nums[piv]
            elif size - piv > k:
                l = piv + 1
            else:
                r = piv - 1


class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Better implementation of quick select, and choose random pivot to
        avoid worst case.

        Average runtime is O(N), but the requirement is to select a random pivot
        each time. This way, the runtime is (N + 1/2 N + 1/4 N + ...) = O(N).

        72 ms, 37% ranking.
        """
        size = len(nums)

        def locate_pivot(l: int, r: int) -> int:
            piv = randint(l, r)
            nums[l], nums[piv] = nums[piv], nums[l]
            j = l + 1
            for i in range(l + 1, r + 1):
                if nums[i] < nums[l]:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
            nums[l], nums[j - 1] = nums[j - 1], nums[l]
            return j - 1

        l, r = 0, size - 1
        while True:
            piv = locate_pivot(l, r)
            if size - piv == k:
                return nums[piv]
            elif size - piv > k:
                l = piv + 1
            else:
                r = piv - 1


sol0 = Solution0()
sol = Solution2()
tests = []
for _ in range(100):
    nums = [randint(1, 1000) for _ in range(randint(1, 1000))]
    k = randint(1, len(nums))
    tests.append((nums, k))

for i, (nums, k) in enumerate(tests):
    ans = sol0.findKthLargest(nums, k)
    res = sol.findKthLargest(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}, Test: {nums}, {k}')
