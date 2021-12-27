# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def recoverArray(self, nums: List[int]) -> List[int]:
        """TLE

        This method works, but too slow.
        """
        nums.sort()
        N = len(nums) // 2
        
        def helper(lo: int, hi: int, idx: int) -> bool:
            if idx == 2 * N:
                return True
            pos_lo = nums[idx] + k
            pos_hi = nums[idx] - k
            if lo < N and pos_lo > 0 and res[lo] == pos_lo and helper(lo + 1, hi, idx + 1):
                return True
            if hi < N and pos_hi > 0 and res[hi] == pos_hi and helper(lo, hi + 1, idx + 1):
                return True
            if lo < N and not res[lo] and pos_lo > 0:
                res[lo] = pos_lo
                if helper(lo + 1, hi, idx + 1):
                    return True
                res[lo] = 0
            if hi < N and not res[hi] and pos_hi > 0:
                res[hi] = pos_hi
                if helper(lo, hi + 1, idx + 1):
                    return True
                res[hi] = 0
            return False


        for i in range(1, 2 * N):
            k, r = divmod(nums[i] - nums[0], 2)  # obtain k
            if r == 0 and k > 0:
                res = [0] * N
                res[0] = nums[0] + k
                if helper(1, 0, 1):
                    return res


class Solution2:
    def recoverArray(self, nums: List[int]) -> List[int]:
        """This is the same idea as Solution1 but with much better
        implementation. We know that the smallest value of nums must be the
        smallest value (a0) in the desired array minus k. Thus, we can go
        through the sorted nums one by one to find a0 + k. The criteria is that
        if nums[i] - nums[0] is even, then (nums[i] - nums[0]) // 2 is a
        candidate for k.

        Once we obtain a k, the job is to verify whether this k works for all
        the values in nums. To check that, for each nums[i] it is either am - k
        or an + k, where m >= n. It is guaranteed that an must have been
        obtained previously, because an - k must have been encountered before
        we can have am - k. We thus check whether an = nums[i] - k fits the
        an already obtained. If it matches, we move on to nums[i + 1] with
        am - k and an+1 + k. Otherwise, we compute am = nums[i] + k, put it in
        the result and move on to nums[i + 1] with am+1 - k and an + k.

        The time complexity is at worst O(N^2) where N = len(nums). 

        772 ms, 14% ranking.
        """
        nums.sort()
        N = len(nums) // 2
        for i in range(1, 2 * N):
            k, r = divmod(nums[i] - nums[0], 2)  # obtain k
            if r == 0 and k > 0:
                res = [0] * N
                res[0] = nums[0] + k
                lo, hi, idx = 1, 0, 1
                while hi < N and idx < 2 * N:
                    if nums[idx] - k == res[hi]:
                        hi += 1
                    elif lo < N:
                        res[lo] = nums[idx] + k
                        lo += 1
                    else:
                        break
                    idx += 1
                else:
                    return res


class Solution3:
    def recoverArray(self, nums: List[int]) -> List[int]:
        """Better method to verify whether a given k is valid.

        The solution is also similar to problem 954

        Ref: https://leetcode.com/problems/recover-the-original-array/discuss/1647452/Python-Short-solution-explained

        O(N^2), 524 ms, 77% ranking.
        """
        nums.sort()
        for n in nums:
            k, r = divmod(n - nums[0], 2)  # obtain k
            if r == 0 and k > 0:
                res = []
                counter = Counter(nums)
                for m in nums:
                    if counter[m]:
                        if not counter[m + 2 * k]:  # a-k exists but not a+k
                            break
                        counter[m] -= 1
                        counter[m + 2 * k] -= 1
                        res.append(m + k)
                else:
                    return res


sol = Solution3()
tests = [
    ([2,10,6,4,8,12], [3,7,11]),
    ([1,1,3,3], [2,2]),
    ([5, 435], [220]),
    ([1,9,99,3,11,101], [2, 10, 100]),
    ([11,6,3,4,8,7,8,7,9,8,9,10,10,2,1,9], [2,3,7,8,8,9,9,10]),
    ([8,4,5,1,9,8,6,5,6,9,7,3,8,3,6,7,10,11,6,4], [2,4,5,5,6,7,7,8,9,10]),
    ([1,50,99,101,150,199], [51,100,149]),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.recoverArray(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
