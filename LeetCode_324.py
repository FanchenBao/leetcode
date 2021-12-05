# from pudb import set_trace; set_trace()
from typing import List


class Solution:
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

        


sol = Solution()
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
