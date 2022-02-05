# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def findMaxLength(self, nums: List[int]) -> int:
        """LeetCode 525

        This is very similar to the max subarray sum problem using the divide
        and conquer idea. The main logic is to compute the max cross array that
        have the longest length of balanced 0s and 1s. The method I use is
        counting the net 1s on the left and net 1s on the right (i.e. plus one
        when encountering one, and minus one when encountering zero), then
        match th two net one count.

        O(NlogN), 4125 ms, 5% ranking.

        I highly suspect that a Kadane-ish method exists that can solve the
        problem in O(N)
        """
        
        def helper(lo: int, hi: int) -> int:
            if lo == hi:
                return 0
            mid = (lo + hi) // 2
            ld = {}
            max_cross_len = 0
            net_one_cnt = 0
            for i in range(mid, lo - 1, -1):
                if nums[i]:
                    net_one_cnt += 1
                else:
                    net_one_cnt -= 1
                ld[net_one_cnt] = i
            net_one_cnt = 0
            for j in range(mid + 1, hi + 1):
                if nums[j]:
                    net_one_cnt += 1
                else:
                    net_one_cnt -= 1
                if -net_one_cnt in ld:
                    max_cross_len = max(max_cross_len, j - ld[-net_one_cnt] + 1)
            return max(helper(lo, mid), helper(mid + 1, hi), max_cross_len)

        return helper(0, len(nums) - 1)


class Solution2:
    def findMaxLength(self, nums: List[int]) -> int:
        """I had the idea of counting net ones, but I didn't realize that if
        we start this counting from the beginning, then anytime when two
        indices have the same count, that means the subarray in between has
        net count one equal to zero, which means it is a balanced array. Thus,
        all we need to do is to record the first occurrence of a certain count,
        and compute the length of the balanced array when the same count occurs
        again.

        This is from solution 2 of the official answer.

        O(N), 1083 ms, 44% ranking.
        """
        net_one_map = {0: -1}  # avoid considering cnt == 0 separately
        res, cnt = 0, 0
        for i, n in enumerate(nums):
            cnt += 1 if n else -1
            if cnt not in net_one_map:
                net_one_map[cnt] = i
            else:
                res = max(res, i - net_one_map[cnt])
        return res


sol = Solution2()
tests = [
    ([0, 1], 2),
    ([0, 1, 0], 2),
    ([0], 0),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findMaxLength(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
