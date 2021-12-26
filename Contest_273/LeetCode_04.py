# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right


class Solution:
    def longest_increasing_subseq_len(self, lst: List[int]) -> int:
        last_val = [0]
        for val in lst:
            idx = bisect_right(last_val, val)
            if idx == len(last_val):
                last_val.append(val)
            else:
                last_val[idx] = val
        return len(last_val) - 1

    def kIncreasing(self, arr: List[int], k: int) -> int:
        """I wasn't able to solve it yesterday. Nor had I expected to solve it
        today. But I decided to play with it just a little bit, and booya, I did
        it and it was not that hard.

        The first observation is that the entire array can be split into k
        different arrays. These arrays are like this arr[i], arr[i + k], ...
        They do not interact with each other and each of them must be
        non-decreasing. So the problem turns into finding the minimum number of
        changes that can turn each array into non-decreasing. This in turn is
        a problem of finding the longest non-decreasing subsequence already
        existing in the array. Then the number of changes is the length of the
        array minus the length of the longest non-decreasing subsequence.

        To find the longest non-decreasing subsequence, I cheated. I looked it
        up on Wikipedia, and the algo is as follows.

        We go through each number one by one. And we keep an array last_val
        such that last_val[i] is the last value of the non-decreasing
        subsequence of length i. By default, last_val must be sorted. Then for
        each new value encountered in the array, we binary search last_val to
        find where the new value can be placed. If the new value is larger or
        equal to all the values in last_val, that means the new value can extend
        the longest non-decreasing subsequence. So we append it to last_val. If
        the new value can find a spot within last_val, that means we can replace
        that value in last_val with the new value, because the new one is
        guaranteed to be smaller, which means it has a higher chance of further
        expanding the non-decreasing subsequence.

        O(K(N/K)log(N/K)), 1160 ms, 33% ranking.
        """
        remain, start, res = len(arr), 0, 0
        while remain:
            lst = [arr[i] for i in range(start, len(arr), k)]
            res += len(lst) - self.longest_increasing_subseq_len(lst)
            remain -= len(lst)
            start += 1
        return res


sol = Solution()
tests = [
    ([12,6,12,6,14,2,13,17,3,8,11,7,4,11,18,8,8,3], 1, 12),
    ([5,4,3,2,1], 1, 4),
    ([4,1,5,2,6,2], 2, 0),
    ([4,1,5,2,6,2], 3, 2),
    ([2,2,2,2,2,1,1,4,4,3,3,3,3,3], 1, 4),
]

for i, (arr, k, ans) in enumerate(tests):
    res = sol.kIncreasing(arr, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
