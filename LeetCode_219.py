# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution1:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Use a hashmap to collect the indices of all repeated values. Then we
        just need to check each consecutive pairs of indices of each repeated
        value, and if any consecutive pair's difference is not larger than k,
        we can return True.

        In implementation, it is possible to make the check while creating the
        hashmap. This can ensure early termination.

        O(N), 790 ms, 55% ranking.
        """
        hashmap = defaultdict(list)
        for i, n in enumerate(nums):
            hashmap[n].append(i)
            if len(hashmap[n]) > 1 and hashmap[n][-1] - hashmap[n][-2] <= k:
                return True
        return False


class Solution2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """Sliding window

        Inspired by: https://leetcode.com/problems/contains-duplicate-ii/discuss/61372/Simple-Java-solution

        O(N)
        """
        w = set()
        for i, n in enumerate(nums):
            if i > k:
                w.remove(nums[i - k - 1])
            if n in w:
                return True
            w.add(n)
        return False


sol = Solution2()
tests = [
    ([1,2,3,1], 3, True),
    ([1,0,1,1], 1, True),
    ([1,2,3,1,2,3], 2, False),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.containsNearbyDuplicate(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
