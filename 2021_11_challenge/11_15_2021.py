# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution1:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """TLE
        """
        nums.sort()
        sets = []
        for n in nums:
            len_sets = len(sets)
            for i in range(len_sets):
                s = sets[i]
                j = len(s) - 1
                while j >= 0:
                    if n % s[j] == 0:
                        break
                    j -= 1
                if j >= 0:
                    sets.append(s[:j + 1] + [n])
            if len(sets) == len_sets:
                sets.append([n])
        max_len = 0
        res = []
        for s in sets:
            if len(s) > max_len:
                max_len = len(s)
                res = s
        return res


class Solution2:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """LeetCode 368

        I sort nums first. Then I want to find the largest divisible subset that
        includes nums[0]. To do that, I go through nums[1:] and include only
        values that are divisible by nums[0]. I then divide each such value by
        nums[0] to create a new array nums_. I then run the same logic on nums_
        to obtain the largest divisible subset from nums_. This subset must
        also divide nums[0]. Thus we can add nums[0] to it to produce the
        largest subset that includes nums[0]. 

        Then, we move on to nums[1]. However, the trick is that if nums[1] is
        divisible by nums[0], we don't have to check nums[1] again. Because any
        divisible subset that includes nums[1] must be smaller than the divisible
        subset that includes nums[0]. This can be proved by contradiction. If
        the divisible subset that includes nums[1] is larger than that of
        nums[0], since nums[1] is divisible by nums[0] and nums[0] < nums[1],
        then nums[0] can also be added to the divisble subset of nums[1]. Thus
        the divisible subset of nums[1] becomes the divisible subset of nums[0].
        This means the divisible subset of nums[0] must also be larger than that
        of nums[1].

        Continue on this, we will only check the number that is not divisible
        by any factors that have been checked so far.

        Time complexity: not sure.
        240 ms, 95% ranking.
        """
        def dfs(nums_: List[int]) -> List[int]:
            if len(nums_) <= 1:
                return nums_
            factors = []
            res = []
            for i, n in enumerate(nums_):
                if any(n % f == 0 for f in factors):
                    continue
                s = dfs([v // n for v in nums_[i + 1:] if v % n == 0])
                if len(s) + 1 > len(res):
                    res = [n] + [n * v for v in s]
                factors.append(n)
            return res

        return dfs(sorted(nums))



class Solution3:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """Interesting solution from Mr. Pochmann.

        https://leetcode.com/problems/largest-divisible-subset/discuss/84002/4-lines-in-Python

        The intuition is the same as solution1, where if a value is divisible
        by the largest of a divisible subset, then the value can dividde every
        one in the divisible subset, i.e. the value can be added to the subset.
        """
        # key is the largest in a divisible subset, value is the subset
        S = {-1: []}
        for n in sorted(nums):
            S[n] = max((S[d] for d in S if n % d == 0), key=len) + [n]
        return list(max(S.values(), key=len))


class Solution4:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """Standard DP solution from

        https://leetcode.com/problems/largest-divisible-subset/discuss/1578991/C%2B%2B-4-Simple-Solutions-w-Detailed-Explanation-or-Optimizations-from-Brute-Force-to-DP
        """
        N = len(nums)
        # post[i] records the index of the next number that belongs to the same
        # max divisible subset as nums[i]
        # count[i] records the size of the max divisible subset starting from
        # nums[i]
        post, count = [-1] * N, [0] * N
        nums.sort()

        def dfs(idx: int) -> None:
            if idx == N - 1:
                count[idx] = 1
            elif count[idx] == 0:
                for i in range(idx + 1, N):
                    if nums[i] % nums[idx] == 0:
                        dfs(i)
                        if count[i] > count[idx]:
                            count[idx] = count[i]
                            post[idx] = i
                count[idx] += 1

        for i in range(N):
            dfs(i)
        idx = count.index(max(count))
        res = []
        while idx >= 0:
            res.append(nums[idx])
            idx = post[idx]
        return res


sol = Solution4()
tests = [
    ([1, 2, 3], [1, 2]),
    ([1, 2, 4, 8], [1, 2, 4, 8]),
    ([2, 3, 6, 18, 24], [2, 6, 18]),
    ([3,4,16,8], [4,8,16])
]

for i, (nums, ans) in enumerate(tests):
    res = sol.largestDivisibleSubset(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
