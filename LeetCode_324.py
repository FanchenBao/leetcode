# from pudb import set_trace; set_trace()
from typing import List
from random import randint


class Solution1:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Very very difficult for me. But the actual solution is quite simple, IF
        we do not restrict ourselves to the time and space constraints. We sort
        the nums in reverse order. Place the bigger half in the odd position
        and the even half in the even position, and we are done.

        The difficult part is to prove that this arrangement works. For that,
        https://leetcode.com/problems/wiggle-sort-ii/discuss/77684/Summary-of-the-various-solutions-to-Wiggle-Sort-for-your-reference
        offers the proof.

        The problem becomes much more complicated if the desired time and space
        complexity is considered. For that, the above mentioned post helps, as
        well as Mr. Pochmann's original post:

        https://leetcode.com/problems/wiggle-sort-ii/discuss/77677/O(n)%2BO(1)-after-median-Virtual-Indexing

        The following is the non-constrained solution.

        O(NlogN) time, O(N) space, 172 ms, 63% ranking.
        """
        copy = sorted(nums, reverse=True)
        k = len(nums) // 2
        j = 1
        for i in range(k):
            nums[j] = copy[i]
            j += 2
        j = 0
        for i in range(k, len(nums)):
            nums[j] = copy[i]
            j += 2


def kth_smallest_value(nums: List[int], k: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        p = randint(l, r)
        nums[p], nums[l] = nums[l], nums[p]
        i = l
        for j in range(l + 1, r + 1):
            # Loop invariant
            # nums[l], ... nums[i] <= nums[l]
            # nums[i + 1], ... nums[j - 1] > nums[l]
            if nums[j] < nums[l]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                
        nums[i], nums[l] = nums[l], nums[i]
        if i == k:
            return nums[i]
        if i < k:
            l = i + 1
        else:
            r = i - 1


class Solution2:
    def wiggleSort(self, nums: List[int]) -> None:
        """O(N) time and O(N) space.

        We use kth_smallest_value to find the median, and then rearrange a copy
        of nums such that all the median values are positioned correctly, and
        all the values smaller than median are pushed to the left, and those
        larger than median pushed to the right. The smaller or larger values
        themselves are not sorted.

        Finally, nums are populated again just as in Solution1.
        """
        mid = (len(nums) - 1) // 2
        m = kth_smallest_value(nums, mid)
        i, j, k = 0, len(nums) - 1, 0
        nums_copy = nums[:]
        # nums[0], ..., nums[i - 1] < m
        # nums[j + 1], ..., nums[-1] > m
        # nums[i], ..., nums[k - 1] == m
        while k <= j:
            if nums_copy[k] < m:
                nums_copy[i], nums_copy[k] = nums_copy[k], nums_copy[i]
                i += 1
                k += 1
            elif nums_copy[k] > m:
                nums_copy[j], nums_copy[k] = nums_copy[k], nums_copy[j]
                j -= 1
            else:
                k += 1
        # create the wiggly sorted array inside nums
        j = 0
        for i in range(mid, -1, -1):
            nums[j] = nums_copy[i]
            j += 2
        j = 1
        for i in range(len(nums) - 1, mid, -1):
            nums[j] = nums_copy[i]
            j += 2


class Solution3:
    def wiggleSort(self, nums: List[int]) -> None:
        """Virtual indexing to make the solution O(N) in time and O(1) in space.

        This is from Mr. Pochmann's idea.
        """
        mid = (len(nums) - 1) // 2
        m = kth_smallest_value(nums, mid)
        M = lambda i: (2 * i + 1) % (len(nums) | 1)
        i, j, k = 0, len(nums) - 1, 0  # i, j, k are virtual indices
        # Virtually, the following must hold
        # nums[0], ..., nums[i - 1] < m
        # nums[j + 1], ..., nums[-1] > m
        # nums[i], ..., nums[k - 1] == m
        while k <= j:
            if nums[M(k)] > m:
                nums[M(i)], nums[M(k)] = nums[M(k)], nums[M(i)]
                i += 1
                k += 1
            elif nums[M(k)] < m:
                nums[M(j)], nums[M(k)] = nums[M(k)], nums[M(j)]
                j -= 1
            else:
                k += 1


sol = Solution3()
tests = [
    [1,5,1,1,6,4],
    [1,3,2,2,3,1],
    [4,5,5,6],
    [1,1,2,1,2,2,1],
]

for k, (nums) in enumerate(tests):
    sol.wiggleSort(nums)
    correct = True
    for i in range(1, len(nums)):
        if (i % 2 and nums[i] > nums[i - 1]) or (i % 2 == 0 and nums[i] < nums[i - 1]):
            continue
        else:
            correct = False
            break
    if correct:
        print(f'Test {k}: PASS')
    else:
        print(f'Test {k}; Fail. Res: {nums}')
