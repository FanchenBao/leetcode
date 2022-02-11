# from pudb import set_trace; set_trace()
from typing import List
from itertools import accumulate
from collections import Counter


class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """LeetCode 560

        I use prefix sum and a counter on the prefix sum. Then I iterate the
        prefix sum array. For each element p, I can check whether p + k exists
        in the prefix sum. If it does, then there must be a subarray in between
        p and p + k that sums up to k. The tricky part is to handle the case
        of k = 0 and nums containing 0. To handle that, I do counter[p] -= 1
        before incrementing the result. counter[p] -= 1 means that we remove
        the current position from consideration. This can prevent duplicates
        when either p + k goes back to p or some future value goes back to p.

        O(N), 449 ms, 19% ranking.
        """
        presum = list(accumulate(nums))
        counter = Counter(presum)
        res = 0
        for p in presum:
            counter[p] -= 1  # avoid double counting
            res += counter[p + k] + bool(p == k)
        return res


class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """This is from the official solution. Same idea, but its
        implementation is more intuitive and does not have to battle the edge
        cases.

        O(N), 370 ms, 40% ranking.
        """
        counter = Counter([0])
        res, presum = 0, 0
        for n in nums:
            presum += n
            res += counter[presum - k]
            counter[presum] += 1
        return res


sol = Solution2()
tests = [
    ([1, 1, 1], 2, 2),
    ([1, 2, 3], 3, 2),
    ([1], 0, 0),
    ([0, 0, 0], 0, 6),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.subarraySum(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
