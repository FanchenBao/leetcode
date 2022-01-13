# from pudb import set_trace; set_trace()
from typing import List, Dict


class Solution1:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        """This is O(N) time but also O(N) space. So it does not satisfy the
        requirement.

        The idea is to do DFS traverse and see if a cycle with size larger than
        1 can be found. I need a history hashmap to record the size when each
        number is encountered during a traversal. I cannot use the original
        array, because I won't be able to tell whether a number has been
        visited or not.

        O(N) time, O(N) space, 57 ms, 60% ranking.

        UPDATE: O(N) time, O(1) space.
        """
        N = len(nums)
        for i in range(N):
            j = i
            size, di = 1001, nums[j]
            while nums[j]:
                if nums[j] > 1000:
                    if size - nums[j] > 1:
                        return True
                    break
                if di * nums[j] > 0:
                    nums[j], j = size, ((j + nums[j]) % N) if di > 0 else ((j + nums[j] + N) % N)
                    size += 1
                else:
                    break
            for k in range(N):
                if nums[k] > 1000:
                    nums[k] = 0
        return False


class Solution2:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        """So we have been having trouble finding a decent way to tell the size
        of the loop and reject a loop if its size is 1. This solution

        Ref: https://leetcode.com/problems/circular-array-loop/discuss/232417/Python-simple-solution-beats-100-with-O(1)-space

        offers a simple idea to identify a size-one loop: check whether the
        next index is the same as the current one. This way, we don't have to
        keep record of the link size. We can return true for all loops except
        those whose next index is the same as the current.

        We also create a marker for each traversal. Once we hit an index with
        the same marker of the current traversal, we know for sure that a loop
        of size larger than one has been found.

        O(N) time, O(1) space. 51 ms, 63% ranking.
        """
        N = len(nums)
        for i in range(N):
            marker, j, direction = 1001 + i, i, nums[i]
            while -1000 <= nums[j] <= 1000:
                if direction * nums[j] > 0:  # point to same direction
                    next_j = (j + nums[j] + N) % N
                    if next_j == j:  # loop of size 1, do not assign marker
                        break
                    nums[j], j = marker, next_j
                else:
                    break
            if nums[j] == marker:
                return True
        return False


sol = Solution2()
tests = [
    ([2,-1,1,2,2], True),
    ([-1, 2], False),
    ([-2,1,-1,-2,-2], False),
    ([-1,-2,-3,-4,-5], False),
    ([-1,2,1,2], True),
    ([-1,-1,-1], True),

]

for i, (nums, ans) in enumerate(tests):
    res = sol.circularArrayLoop(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
