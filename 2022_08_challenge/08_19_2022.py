# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter, defaultdict


class Solution1:
    def isPossible(self, nums: List[int]) -> bool:
        """LeetCode 659

        We use counter and the fact that counter keeps the insertion order.
        Since nums is already sorted, counter's keys are sorted as well. We
        try to extend a subseq as much as possible until the count of the next
        value drops below the count of the current value. Then we know we
        cannot extend anymore, because we will be depleting the supply of
        numbers for the next subseq. We keep track of the length of the current
        subseq. If any of them is smaller than 3, we return False. Otherwise,
        we finish going through all numbers in counter, and return True.

        The one thing to note is that we also require consecutive values in the
        subsequence differ by one. I forgot about it, and got a wrong answer
        initially.

        O(N), 713 ms, faster than 68.83%
        """
        counter = Counter(nums)
        while counter:
            seq = list(counter.keys())
            l = 0
            for i, s in enumerate(seq):
                if i == 0 or (counter[s] > counter[seq[i - 1]] and s - seq[i - 1] == 1):
                    counter[s] -= 1
                    if not counter[s]:
                        counter.pop(s)
                    l += 1
                else:
                    break
            if l < 3:
                return False
        return True


class Solution2:
    def isPossible(self, nums: List[int]) -> bool:
        """Solution from https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/2446913/C%2B%2B-oror-Greedy-oror-Fully-Commented-oror-Simplest-Solution-Of-All

        Use a map to record how many times a number is needed to form a subseq.
        Each number in nums is in one of two states. Either it is not needed
        by any other subseq, so it has to start its own subseq of length at
        least three. Or it is needed by other subseq, then we fulfill that
        needs. If neither of the situations is satisfied, the number is in a
        limbo state, which means we shall return False.
        """
        freq = Counter(nums)
        need = Counter()
        for n in nums:
            if freq[n] == 0:
                continue
            if need[n] > 0:
                freq[n] -= 1
                need[n] -= 1
                need[n + 1] += 1  # extend as much as possible
            elif freq[n + 1] > 0 and freq[n + 2] > 0:
                freq[n] -= 1
                freq[n + 1] -= 1
                freq[n + 2] -= 1
                need[n + 3] += 1  # extend as much as possible
            else:
                return False
        return True




sol = Solution2()
tests = [
    ([1,2,3,3,4,5], True),
    ([1,2,3,3,4,4,5,5], True),
    ([1,2,3,4,4,5], False),
    ([1,2,3,5,5,6,7], False),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.isPossible(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
