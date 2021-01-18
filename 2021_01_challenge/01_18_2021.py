# from pudb import set_trace; set_trace()
from typing import List
import collections


class Solution1:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """Put all numbers in a counter, then go through the keys one by one.
        We check whether the key and k minus the key exists in nums. If both
        exists, we have pairs to count. To count the pairs, depending on whether
        the key and k minus the key are the same or different, we follow
        slightly different logic. Eventually, we update the counter after the
        numbers are taken out of the array.

        O(N), 600 ms, 80% ranking.
        """
        c = collections.Counter(nums)
        res = 0
        for n in c.keys():
            if c[n] and c[k - n]:
                num_pair = min(c[n], c[k - n]) if n != k - n else c[n] // 2
                c[n] -= num_pair
                c[k - n] -= num_pair
                res += num_pair
        return res


class Solution2:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """The smartass solution.
        
        Note that we are not updating the counts after the corresponding numbers
        have been used. Instead, we divide the total sum in half at the end to
        compensate for the double count. This also generalize the situation when
        n and k - n are the same.
        """
        c = collections.Counter(nums)
        return sum(min(c[n], c[k - n]) for n in c.keys()) // 2


sol = Solution2()
tests = [
    ([1, 2, 3, 4], 5, 2),
    ([3, 1, 3, 4, 3], 6, 1),
    ([1], 1, 0),
    ([1, 1], 2, 1),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.maxOperations(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
