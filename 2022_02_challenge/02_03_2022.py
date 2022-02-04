# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter, defaultdict


class Solution1:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """LeetCode 454

        The method used is a glorified 3SUM. We first pick out the sum of nums1
        and nums2, then go through nums3 one by one and check if the required
        value exists in nums4. All the while, we use counter to keep track of
        the number of repeats each value can take.

        O(N^3), 1989 ms, 5% ranking. Terrible time complexity.
        """
        memo, res = defaultdict(int), 0
        nums1cnt = Counter(nums1)
        nums2cnt = Counter(nums2)
        nums3cnt = Counter(nums3)
        nums4cnt = Counter(nums4)
        for n1 in nums1cnt:
            for n2 in nums2cnt:
                tgt = 0 - n1 - n2
                if tgt not in memo:
                    for n3 in nums3cnt:
                        memo[tgt] += nums3cnt[n3] * nums4cnt[tgt - n3]
                res += memo[tgt] * nums1cnt[n1] * nums2cnt[n2]
        return res


class Solution2:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """Two 2SUM problem, as hinted by the discussion titles.

        O(N^2), 544 ms, 99% ranking.
        """
        cnt1 = Counter(n1 + n2 for n1 in nums1 for n2 in nums2)
        cnt2 = Counter(n3 + n4 for n3 in nums3 for n4 in nums4)
        return sum(cnt1[c1] * cnt2[-c1] for c1 in cnt1)


sol = Solution2()
tests = [
    ([1,2], [-2,-1], [-1,2], [0,2], 2),
    ([0], [0], [0], [0], 1),
]

for i, (nums1, nums2, nums3, nums4, ans) in enumerate(tests):
    res = sol.fourSumCount(nums1, nums2, nums3, nums4)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
