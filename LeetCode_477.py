# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def totalHammingDistance(self, nums: List[int]) -> int:
        """The idea is to count the number of 1s and 0s on each position in the
        binary representation of each number. What we need to know is the total
        number of pairs of 0-1 that can be formed at this position. This can
        be computed by finding the total number of pairs, minus the number of
        pairs of 1-1 and the number of pairs of 0-0

        628 ms, 49% ranking.
        """
        max_dig = len(bin(max(nums))) - 2
        res, N = 0, len(nums)
        for i in range(max_dig):
            counter = Counter(1 if n & (1 << i) else 0 for n in nums)
            res += N * (N - 1) // 2 - counter[1] * (counter[1] - 1) // 2 - counter[0] * (counter[0] - 1) // 2
        return res


class Solution2:
    def totalHammingDistance(self, nums: List[int]) -> int:
        """Same idea as solution1, but this part:

        N * (N - 1) // 2 - counter[1] * (counter[1] - 1) // 2 - counter[0] * (counter[0] - 1) // 2

        can be simplified as counter[1] * (N - counter[1]), because counter[1]
        + counter[0] = N

        Ref: https://leetcode.com/problems/total-hamming-distance/discuss/96226/Java-O(n)-time-O(1)-Space

        484 ms, 76% ranking.
        """
        res, N = 0, len(nums)
        for i in range(32):
            one_cnt = sum((n >> i) & 1 for n in nums)
            res += one_cnt * (N - one_cnt)
        return res



sol = Solution2()
tests = [
    ([4, 14, 2], 6),
    ([4, 14, 4], 4),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.totalHammingDistance(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
