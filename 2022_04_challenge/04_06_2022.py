# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        """LeetCode 923

        First I counter the input array. This way, we only have to deal with
        unique values.

        Then I sort the array. For each number, we check three situations.
        First, check if the number can be used three times to form target. Then
        check if the number can be used two times and combine with a third
        value to make target. This is essentially a two-sum problem. Finally,
        check if a single copy of the number can be used to form target with
        two other distinct values.

        O(N^2), 108 ms, 70% ranking.
        """
        counter = Counter(arr)
        nums = sorted(counter)
        res, N = 0, len(nums)
        MOD = 1000000007
        for i, n in enumerate(nums):
            if counter[n] >= 3 and 3 * n == target:
                res = (res + counter[n] * (counter[n] - 1) * (counter[n] - 2) // 6) % MOD
            if counter[n] >= 2 and 2 * n <= target:
                new_t = target - 2 * n
                if new_t in counter and new_t != n:
                    res = (res + counter[n] * (counter[n] - 1) // 2 * counter[new_t]) % MOD
            if n < target:
                j = i + 1
                while j < N and target - n - nums[j] > nums[j]:
                    new_t = target - n - nums[j]
                    if new_t in counter:
                        res = (res + counter[n] * counter[nums[j]] * counter[new_t]) % MOD
                    j += 1
            else:
                break
        return res
        

sol = Solution()
tests = [
    ([1,1,2,2,3,3,4,4,5,5], 8, 20),
    ([1,1,2,2,2,2], 5, 12),
    ([0,0,0], 0, 1),
    ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 0, 680),
]

for i, (arr, target, ans) in enumerate(tests):
    res = sol.threeSumMulti(arr, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
