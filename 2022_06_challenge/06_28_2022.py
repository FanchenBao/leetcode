# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter
import heapq


class Solution1:
    def minDeletions(self, s: str) -> int:
        """LeetCode 1647

        Once we take the counter of s, the problem becomes given a list of
        numbers (at most 26 numbers), how many values need to be deducted from
        the numbers such that all the remaining numbers are unique.

        The strategy is that for each number that is a repeat, i.e. has been
        seen before, we must deduct from that value until it reaches a number
        that has not been seen before. Here, we use a little trick to speed up
        the process, if there are a lot of repeats. Each time when a value
        finally settles down, we record the value and the settled-down value.
        Next time, if the same value is encountered, we pull out the previous
        settled-down value and start a new search from there.
        
        O(N + K^2), 179 ms, faster than 73.27%
        """
        memo = {}
        seen = set()
        res = 0
        for v in sorted(Counter(s).values()):
            if v not in seen:
                memo[v] = v
                seen.add(v)
            else:
                start = memo[v]
                while start and start in seen:
                    start -= 1
                seen.add(start)
                memo[v] = start
                res += v - start
        return res


class Solution2:
    def minDeletions(self, s: str) -> int:
        """Priority queue, from the official solution
        O(N + KlogK), 228 ms, faster than 58.81%
        """
        heap = [-v for v in Counter(s).values()]
        heapq.heapify(heap)
        res = 0
        cur = heapq.heappop(heap)
        while heap and cur:  # important to stop early when cur == 0
            nex = heapq.heappop(heap)
            if cur != nex:
                cur = nex
            else:
                heapq.heappush(heap, nex + 1)
                res += 1
        return res


class Solution3:
    def minDeletions(self, s: str) -> int:
        """The sorting method, from the official solution.

        Keep track of a max_freq_allowed value. Also sort the frequencies in
        descending order. As we go through each freq, if it is smaller than the
        max_freq_allowed, then we know this freq can be used directly, no
        deletion needed. However, once we do that, we shall update the
        max_freq_allowed to the current freq minus one. This is because all the
        remaining freqs are smaller or equal to the current one. Thus, the only
        possible max_freq_allowed is the current freq minus one.

        If the current freq is larger than max_freq_allowed, then we must
        delete until the current freq reaches max_freq_allowed. And then we
        decrement max_freq_allowed.

        O(NlogN), 164 ms, faster than 79.69%
        """
        nums = sorted(Counter(s).values(), reverse=True)
        max_freq_allwoed = nums[0]
        res = 0
        for i, n in enumerate(nums):
            if n <= max_freq_allwoed:
                max_freq_allwoed = n - 1
            else:
                res += n - max_freq_allwoed
                if max_freq_allwoed:
                    max_freq_allwoed -= 1
        return res


sol = Solution3()
tests = [
    ('aab', 0),
    ('aaabbbcc', 2),
    ('ceabaacb', 2),
    ("abcabc", 3),
    ("gfngerrdgfjtgfbjytrgndsegrdfghdnhrtehrsaa", 18),
]

for i, (s, ans) in enumerate(tests):
    res = sol.minDeletions(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
