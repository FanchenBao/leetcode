# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution1:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """Brute force. TLE"""
        for i in range(len(nums) - 1):
            for j in range(i + 1, min(i + 1 + k, len(nums))):
                if abs(nums[i] - nums[j]) <= t and abs(i - j) <= k:
                    return True
        return False


class Solution2:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """Passed OJ at 140 ms"""
        nums_idx = defaultdict(list)
        for i, num in enumerate(nums):
            nums_idx[num].append(i)
        sorted_nums_idx = sorted(nums_idx.items(), key=lambda x: x[0])
        for m, (num_i, idices_i) in enumerate(sorted_nums_idx):
            if len(idices_i) > 1 and 0 <= t:  # num has repeats, if satisfy t. only need to check index
                for i, j in zip(idices_i, idices_i[1:]):
                    if abs(i - j) <= k:
                        return True
            for n in range(m + 1, len(sorted_nums_idx)):
                num_j, idices_j = sorted_nums_idx[n]
                if abs(num_i - num_j) <= t:  # check t, then check k
                    idx_i = 0
                    idx_j = 0
                    while idx_i < len(idices_i) and idx_j < len(idices_j):
                        if abs(idices_i[idx_i] - idices_j[idx_j]) <= k:
                            return True
                        if idices_i[idx_i] > idices_j[idx_j]:
                            idx_j += 1
                        elif idices_i[idx_i] < idices_j[idx_j]:
                            idx_i += 1
                else:  # since the nums are sorted, once the comparison blows up t, no need to continue
                    break
        return False


class Solution3:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """This is the really brilliant solution found on the forum.

        The idea is that to constrain numbers with value difference <= t, all
        we need to do is to is to divide the number by (t + 1). The remainder
        of this operation must be 0 to t, therefore if we group the numbers
        that have the same quotient when divided by (t + 1), it is guaranteed
        that the absolute difference between them is <= t.

        This grouping can be done via a dict. Each quotient corresponds to a
        number. If two numbers have the same quotient, i.e. they belong to the
        same (t + 1) size bucket, they must satisfy the requirement (wait, what
        about the requirement on the indices? I will talk about it later).
        
        It is also possible that the numbers on adjacent buckets satisfy the
        t requirements. But beyond adjacent buckets, the numbers no longer
        satisfy the t requirement, because the difference between the number
        must be at least 2t. So we need to check the bucket itself, and the
        buckets immediately ahead and behind the bucket.

        Now, let's discuss the k requirement. The k requirement specifies that
        the search must be contained within a moving window of size k. In other
        words, as long as the checking method mentioned above happens within
        the k-size moving window, the result is always valid. To avoid going
        over the window size, we always delete the number (and its bucket,
        since each bucket can only have one number. If it has two, it already
        satisfies the t requirement) that has just fallen out of the k-size
        moving window. 
        """
        if t < 0:  # absolute difference cannot be negative
            return False
        buckets = {}
        bucket_size = t + 1
        for i, num in enumerate(nums):
            bucket = num // bucket_size
            # check for t requirement
            if bucket in buckets:
                return True
            if bucket - 1 in buckets and abs(buckets[bucket - 1] - num) <= t:
                return True
            if bucket + 1 in buckets and abs(buckets[bucket + 1] - num) <= t:
                return True
            buckets[bucket] = num
            # ensure k-size moving window
            if i >= k:
                del buckets[nums[i - k] // bucket_size]
        return False


sol = Solution3()
tests = [
    # ([1, 2, 3, 1], 3, 0, True),
    # ([1, 0, 1, 1], 1, 2, True),
    ([1, 5, 9, 1, 5, 9], 2, 3, False),
    # ([1, 4, 9, 1, 4, 9], 1, 3, True),
    # ([-1, -1], 1, -1, False),
    # ([1, 3, 6, 2], 1, 2, True),
]

for i, (nums, k, t, ans) in enumerate(tests):
    res = sol.containsNearbyAlmostDuplicate(nums, k, t)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
