# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict
from itertools import chain


class Solution1:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """LeetCode 491

        I initially did not want to use set, but couldn't figure out a way
        without set to remove duplicates.

        O(N^2), 218 ms, faster than 92.19% 
        """
        dp = [[(n,)] for n in nums]
        res_set = set()
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] >= nums[i]:
                    for seq in dp[j]:
                        new_seq = (nums[i],) + seq
                        if new_seq not in res_set:
                            dp[i].append(new_seq)
                            res_set.add(new_seq)
        return [list(tup) for tup in res_set]


class Solution2:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """Here is how to NOT use set. We just stop when we encounter a dup,
        because if we keep moving on, it will repeat the same situation. For
        example, say we have [1, 1, 1, 1]. At position 1, we've already handled
        the situation of three 1s. Thus, at position 0, we shall not progress
        past position 1, because if we do, we will be in the same situation of
        three 1s.

        207 ms, faster than 99.06%
        """
        dp = [[] for _ in nums]
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] >= nums[i]:
                    for seq in dp[j]:
                        dp[i].append([nums[i]] + seq)
                    if nums[j] == nums[i]:
                        break
            else:
                dp[i].append([nums[i]])
        return [v for v in chain(*dp) if len(v) > 1]



sol = Solution2()
tests = [
    ([4,6,7,7], [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]),
    ([4,4,3,2,1], [[4,4]]),
    ([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1], [[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5],[1,2,3,4,5,6],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,10],[1,2,3,4,5,6,7,9],[1,2,3,4,5,6,7,9,10],[1,2,3,4,5,6,7,10],[1,2,3,4,5,6,8],[1,2,3,4,5,6,8,9],[1,2,3,4,5,6,8,9,10],[1,2,3,4,5,6,8,10],[1,2,3,4,5,6,9],[1,2,3,4,5,6,9,10],[1,2,3,4,5,6,10],[1,2,3,4,5,7],[1,2,3,4,5,7,8],[1,2,3,4,5,7,8,9],[1,2,3,4,5,7,8,9,10],[1,2,3,4,5,7,8,10],[1,2,3,4,5,7,9],[1,2,3,4,5,7,9,10],[1,2,3,4,5,7,10],[1,2,3,4,5,8],[1,2,3,4,5,8,9],[1,2,3,4,5,8,9,10],[1,2,3,4,5,8,10],[1,2,3,4,5,9],[1,2,3,4,5,9,10],[1,2,3,4,5,10],[1,2,3,4,6],[1,2,3,4,6,7],[1,2,3,4,6,7,8],[1,2,3,4,6,7,8,9],[1,2,3,4,6,7,8,9,10],[1,2,3,4,6,7,8,10],[1,2,3,4,6,7,9],[1,2,3,4,6,7,9,10],[1,2,3,4,6,7,10],[1,2,3,4,6,8],[1,2,3,4,6,8,9],[1,2,3,4,6,8,9,10],[1,2,3,4,6,8,10],[1,2,3,4,6,9],[1,2,3,4,6,9,10],[1,2,3,4,6,10],[1,2,3,4,7],[1,2,3,4,7,8],[1,2,3,4,7,8,9],[1,2,3,4,7,8,9,10],[1,2,3,4,7,8,10],[1,2,3,4,7,9],[1,2,3,4,7,9,10],[1,2,3,4,7,10],[1,2,3,4,8],[1,2,3,4,8,9],[1,2,3,4,8,9,10],[1,2,3,4,8,10],[1,2,3,4,9],[1,2,3,4,9,10],[1,2,3,4,10],[1,2,3,5],[1,2,3,5,6],[1,2,3,5,6,7],[1,2,3,5,6,7,8],[1,2,3,5,6,7,8,9],[1,2,3,5,6,7,8,9,10],[1,2,3,5,6,7,8,10],[1,2,3,5,6,7,9],[1,2,3,5,6,7,9,10],[1,2,3,5,6,7,10],[1,2,3,5,6,8],[1,2,3,5,6,8,9],[1,2,3,5,6,8,9,10],[1,2,3,5,6,8,10],[1,2,3,5,6,9],[1,2,3,5,6,9,10],[1,2,3,5,6,10],[1,2,3,5,7],[1,2,3,5,7,8],[1,2,3,5,7,8,9],[1,2,3,5,7,8,9,10],[1,2,3,5,7,8,10],[1,2,3,5,7,9],[1,2,3,5,7,9,10],[1,2,3,5,7,10],[1,2,3,5,8],[1,2,3,5,8,9],[1,2,3,5,8,9,10],[1,2,3,5,8,10],[1,2,3,5,9],[1,2,3,5,9,10],[1,2,3,5,10],[1,2,3,6],[1,2,3,6,7],[1,2,3,6,7,8],[1,2,3,6,7,8,9],[1,2,3,6,7,8,9,10],[1,2,3,6,7,8,10],[1,2,3,6,7,9],[1,2,3,6,7,9,10],[1,2,3,6,7,10],[1,2,3,6,8],[1,2,3,6,8,9],[1,2,3,6,8,9,10],[1,2,3,6,8,10],[1,2,3,6,9],[1,2,3,6,9,10],[1,2,3,6,10],[1,2,3,7],[1,2,3,7,8],[1,2,3,7,8,9],[1,2,3,7,8,9,10],[1,2,3,7,8,10],[1,2,3,7,9],[1,2,3,7,9,10],[1,2,3,7,10],[1,2,3,8],[1,2,3,8,9],[1,2,3,8,9,10],[1,2,3,8,10],[1,2,3,9],[1,2,3,9,10],[1,2,3,10],[1,2,4],[1,2,4,5],[1,2,4,5,6],[1,2,4,5,6,7],[1,2,4,5,6,7,8],[1,2,4,5,6,7,8,9],[1,2,4,5,6,7,8,9,10],[1,2,4,5,6,7,8,10],[1,2,4,5,6,7,9],[1,2,4,5,6,7,9,10],[1,2,4,5,6,7,10],[1,2,4,5,6,8],[1,2,4,5,6,8,9],[1,2,4,5,6,8,9,10],[1,2,4,5,6,8,10],[1,2,4,5,6,9],[1,2,4,5,6,9,10],[1,2,4,5,6,10],[1,2,4,5,7],[1,2,4,5,7,8],[1,2,4,5,7,8,9],[1,2,4,5,7,8,9,10],[1,2,4,5,7,8,10],[1,2,4,5,7,9],[1,2,4,5,7,9,10],[1,2,4,5,7,10],[1,2,4,5,8],[1,2,4,5,8,9],[1,2,4,5,8,9,10],[1,2,4,5,8,10],[1,2,4,5,9],[1,2,4,5,9,10],[1,2,4,5,10],[1,2,4,6],[1,2,4,6,7],[1,2,4,6,7,8],[1,2,4,6,7,8,9],[1,2,4,6,7,8,9,10],[1,2,4,6,7,8,10],[1,2,4,6,7,9],[1,2,4,6,7,9,10],[1,2,4,6,7,10],[1,2,4,6,8],[1,2,4,6,8,9],[1,2,4,6,8,9,10],[1,2,4,6,8,10],[1,2,4,6,9],[1,2,4,6,9,10],[1,2,4,6,10],[1,2,4,7],[1,2,4,7,8],[1,2,4,7,8,9],[1,2,4,7,8,9,10],[1,2,4,7,8,10],[1,2,4,7,9],[1,2,4,7,9,10],[1,2,4,7,10],[1,2,4,8],[1,2,4,8,9],[1,2,4,8,9,10],[1,2,4,8,10],[1,2,4,9],[1,2,4,9,10],[1,2,4,10],[1,2,5],[1,2,5,6],[1,2,5,6,7],[1,2,5,6,7,8],[1,2,5,6,7,8,9],[1,2,5,6,7,8,9,10],[1,2,5,6,7,8,10],[1,2,5,6,7,9],[1,2,5,6,7,9,10],[1,2,5,6,7,10],[1,2,5,6,8],[1,2,5,6,8,9],[1,2,5,6,8,9,10],[1,2,5,6,8,10],[1,2,5,6,9],[1,2,5,6,9,10],[1,2,5,6,10],[1,2,5,7],[1,2,5,7,8],[1,2,5,7,8,9],[1,2,5,7,8,9,10],[1,2,5,7,8,10],[1,2,5,7,9],[1,2,5,7,9,10],[1,2,5,7,10],[1,2,5,8],[1,2,5,8,9],[1,2,5,8,9,10],[1,2,5,8,10],[1,2,5,9],[1,2,5,9,10],[1,2,5,10],[1,2,6],[1,2,6,7],[1,2,6,7,8],[1,2,6,7,8,9],[1,2,6,7,8,9,10],[1,2,6,7,8,10],[1,2,6,7,9],[1,2,6,7,9,10],[1,2,6,7,10],[1,2,6,8],[1,2,6,8,9],[1,2,6,8,9,10],[1,2,6,8,10],[1,2,6,9],[1,2,6,9,10],[1,2,6,10],[1,2,7],[1,2,7,8],[1,2,7,8,9],[1,2,7,8,9,10],[1,2,7,8,10],[1,2,7,9],[1,2,7,9,10],[1,2,7,10],[1,2,8],[1,2,8,9],[1,2,8,9,10],[1,2,8,10],[1,2,9],[1,2,9,10],[1,2,10],[1,3],[1,3,4],[1,3,4,5],[1,3,4,5,6],[1,3,4,5,6,7],[1,3,4,5,6,7,8],[1,3,4,5,6,7,8,9],[1,3,4,5,6,7,8,9,10],[1,3,4,5,6,7,8,10],[1,3,4,5,6,7,9],[1,3,4,5,6,7,9,10],[1,3,4,5,6,7,10],[1,3,4,5,6,8],[1,3,4,5,6,8,9],[1,3,4,5,6,8,9,10],[1,3,4,5,6,8,10],[1,3,4,5,6,9],[1,3,4,5,6,9,10],[1,3,4,5,6,10],[1,3,4,5,7],[1,3,4,5,7,8],[1,3,4,5,7,8,9],[1,3,4,5,7,8,9,10],[1,3,4,5,7,8,10],[1,3,4,5,7,9],[1,3,4,5,7,9,10],[1,3,4,5,7,10],[1,3,4,5,8],[1,3,4,5,8,9],[1,3,4,5,8,9,10],[1,3,4,5,8,10],[1,3,4,5,9],[1,3,4,5,9,10],[1,3,4,5,10],[1,3,4,6],[1,3,4,6,7],[1,3,4,6,7,8],[1,3,4,6,7,8,9],[1,3,4,6,7,8,9,10],[1,3,4,6,7,8,10],[1,3,4,6,7,9],[1,3,4,6,7,9,10],[1,3,4,6,7,10],[1,3,4,6,8],[1,3,4,6,8,9],[1,3,4,6,8,9,10],[1,3,4,6,8,10],[1,3,4,6,9],[1,3,4,6,9,10],[1,3,4,6,10],[1,3,4,7],[1,3,4,7,8],[1,3,4,7,8,9],[1,3,4,7,8,9,10],[1,3,4,7,8,10],[1,3,4,7,9],[1,3,4,7,9,10],[1,3,4,7,10],[1,3,4,8],[1,3,4,8,9],[1,3,4,8,9,10],[1,3,4,8,10],[1,3,4,9],[1,3,4,9,10],[1,3,4,10],[1,3,5],[1,3,5,6],[1,3,5,6,7],[1,3,5,6,7,8],[1,3,5,6,7,8,9],[1,3,5,6,7,8,9,10],[1,3,5,6,7,8,10],[1,3,5,6,7,9],[1,3,5,6,7,9,10],[1,3,5,6,7,10],[1,3,5,6,8],[1,3,5,6,8,9],[1,3,5,6,8,9,10],[1,3,5,6,8,10],[1,3,5,6,9],[1,3,5,6,9,10],[1,3,5,6,10],[1,3,5,7],[1,3,5,7,8],[1,3,5,7,8,9],[1,3,5,7,8,9,10],[1,3,5,7,8,10],[1,3,5,7,9],[1,3,5,7,9,10],[1,3,5,7,10],[1,3,5,8],[1,3,5,8,9],[1,3,5,8,9,10],[1,3,5,8,10],[1,3,5,9],[1,3,5,9,10],[1,3,5,10],[1,3,6],[1,3,6,7],[1,3,6,7,8],[1,3,6,7,8,9],[1,3,6,7,8,9,10],[1,3,6,7,8,10],[1,3,6,7,9],[1,3,6,7,9,10],[1,3,6,7,10],[1,3,6,8],[1,3,6,8,9],[1,3,6,8,9,10],[1,3,6,8,10],[1,3,6,9],[1,3,6,9,10],[1,3,6,10],[1,3,7],[1,3,7,8],[1,3,7,8,9],[1,3,7,8,9,10],[1,3,7,8,10],[1,3,7,9],[1,3,7,9,10],[1,3,7,10],[1,3,8],[1,3,8,9],[1,3,8,9,10],[1,3,8,10],[1,3,9],[1,3,9,10],[1,3,10],[1,4],[1,4,5],[1,4,5,6],[1,4,5,6,7],[1,4,5,6,7,8],[1,4,5,6,7,8,9],[1,4,5,6,7,8,9,10],[1,4,5,6,7,8,10],[1,4,5,6,7,9],[1,4,5,6,7,9,10],[1,4,5,6,7,10],[1,4,5,6,8],[1,4,5,6,8,9],[1,4,5,6,8,9,10],[1,4,5,6,8,10],[1,4,5,6,9],[1,4,5,6,9,10],[1,4,5,6,10],[1,4,5,7],[1,4,5,7,8],[1,4,5,7,8,9],[1,4,5,7,8,9,10],[1,4,5,7,8,10],[1,4,5,7,9],[1,4,5,7,9,10],[1,4,5,7,10],[1,4,5,8],[1,4,5,8,9],[1,4,5,8,9,10],[1,4,5,8,10],[1,4,5,9],[1,4,5,9,10],[1,4,5,10],[1,4,6],[1,4,6,7],[1,4,6,7,8],[1,4,6,7,8,9],[1,4,6,7,8,9,10],[1,4,6,7,8,10],[1,4,6,7,9],[1,4,6,7,9,10],[1,4,6,7,10],[1,4,6,8],[1,4,6,8,9],[1,4,6,8,9,10],[1,4,6,8,10],[1,4,6,9],[1,4,6,9,10],[1,4,6,10],[1,4,7],[1,4,7,8],[1,4,7,8,9],[1,4,7,8,9,10],[1,4,7,8,10],[1,4,7,9],[1,4,7,9,10],[1,4,7,10],[1,4,8],[1,4,8,9],[1,4,8,9,10],[1,4,8,10],[1,4,9],[1,4,9,10],[1,4,10],[1,5],[1,5,6],[1,5,6,7],[1,5,6,7,8],[1,5,6,7,8,9],[1,5,6,7,8,9,10],[1,5,6,7,8,10],[1,5,6,7,9],[1,5,6,7,9,10],[1,5,6,7,10],[1,5,6,8],[1,5,6,8,9],[1,5,6,8,9,10],[1,5,6,8,10],[1,5,6,9],[1,5,6,9,10],[1,5,6,10],[1,5,7],[1,5,7,8],[1,5,7,8,9],[1,5,7,8,9,10],[1,5,7,8,10],[1,5,7,9],[1,5,7,9,10],[1,5,7,10],[1,5,8],[1,5,8,9],[1,5,8,9,10],[1,5,8,10],[1,5,9],[1,5,9,10],[1,5,10],[1,6],[1,6,7],[1,6,7,8],[1,6,7,8,9],[1,6,7,8,9,10],[1,6,7,8,10],[1,6,7,9],[1,6,7,9,10],[1,6,7,10],[1,6,8],[1,6,8,9],[1,6,8,9,10],[1,6,8,10],[1,6,9],[1,6,9,10],[1,6,10],[1,7],[1,7,8],[1,7,8,9],[1,7,8,9,10],[1,7,8,10],[1,7,9],[1,7,9,10],[1,7,10],[1,8],[1,8,9],[1,8,9,10],[1,8,10],[1,9],[1,9,10],[1,10],[1,1],[1,1,1],[1,1,1,1],[1,1,1,1,1],[1,1,1,1,1,1],[2,3],[2,3,4],[2,3,4,5],[2,3,4,5,6],[2,3,4,5,6,7],[2,3,4,5,6,7,8],[2,3,4,5,6,7,8,9],[2,3,4,5,6,7,8,9,10],[2,3,4,5,6,7,8,10],[2,3,4,5,6,7,9],[2,3,4,5,6,7,9,10],[2,3,4,5,6,7,10],[2,3,4,5,6,8],[2,3,4,5,6,8,9],[2,3,4,5,6,8,9,10],[2,3,4,5,6,8,10],[2,3,4,5,6,9],[2,3,4,5,6,9,10],[2,3,4,5,6,10],[2,3,4,5,7],[2,3,4,5,7,8],[2,3,4,5,7,8,9],[2,3,4,5,7,8,9,10],[2,3,4,5,7,8,10],[2,3,4,5,7,9],[2,3,4,5,7,9,10],[2,3,4,5,7,10],[2,3,4,5,8],[2,3,4,5,8,9],[2,3,4,5,8,9,10],[2,3,4,5,8,10],[2,3,4,5,9],[2,3,4,5,9,10],[2,3,4,5,10],[2,3,4,6],[2,3,4,6,7],[2,3,4,6,7,8],[2,3,4,6,7,8,9],[2,3,4,6,7,8,9,10],[2,3,4,6,7,8,10],[2,3,4,6,7,9],[2,3,4,6,7,9,10],[2,3,4,6,7,10],[2,3,4,6,8],[2,3,4,6,8,9],[2,3,4,6,8,9,10],[2,3,4,6,8,10],[2,3,4,6,9],[2,3,4,6,9,10],[2,3,4,6,10],[2,3,4,7],[2,3,4,7,8],[2,3,4,7,8,9],[2,3,4,7,8,9,10],[2,3,4,7,8,10],[2,3,4,7,9],[2,3,4,7,9,10],[2,3,4,7,10],[2,3,4,8],[2,3,4,8,9],[2,3,4,8,9,10],[2,3,4,8,10],[2,3,4,9],[2,3,4,9,10],[2,3,4,10],[2,3,5],[2,3,5,6],[2,3,5,6,7],[2,3,5,6,7,8],[2,3,5,6,7,8,9],[2,3,5,6,7,8,9,10],[2,3,5,6,7,8,10],[2,3,5,6,7,9],[2,3,5,6,7,9,10],[2,3,5,6,7,10],[2,3,5,6,8],[2,3,5,6,8,9],[2,3,5,6,8,9,10],[2,3,5,6,8,10],[2,3,5,6,9],[2,3,5,6,9,10],[2,3,5,6,10],[2,3,5,7],[2,3,5,7,8],[2,3,5,7,8,9],[2,3,5,7,8,9,10],[2,3,5,7,8,10],[2,3,5,7,9],[2,3,5,7,9,10],[2,3,5,7,10],[2,3,5,8],[2,3,5,8,9],[2,3,5,8,9,10],[2,3,5,8,10],[2,3,5,9],[2,3,5,9,10],[2,3,5,10],[2,3,6],[2,3,6,7],[2,3,6,7,8],[2,3,6,7,8,9],[2,3,6,7,8,9,10],[2,3,6,7,8,10],[2,3,6,7,9],[2,3,6,7,9,10],[2,3,6,7,10],[2,3,6,8],[2,3,6,8,9],[2,3,6,8,9,10],[2,3,6,8,10],[2,3,6,9],[2,3,6,9,10],[2,3,6,10],[2,3,7],[2,3,7,8],[2,3,7,8,9],[2,3,7,8,9,10],[2,3,7,8,10],[2,3,7,9],[2,3,7,9,10],[2,3,7,10],[2,3,8],[2,3,8,9],[2,3,8,9,10],[2,3,8,10],[2,3,9],[2,3,9,10],[2,3,10],[2,4],[2,4,5],[2,4,5,6],[2,4,5,6,7],[2,4,5,6,7,8],[2,4,5,6,7,8,9],[2,4,5,6,7,8,9,10],[2,4,5,6,7,8,10],[2,4,5,6,7,9],[2,4,5,6,7,9,10],[2,4,5,6,7,10],[2,4,5,6,8],[2,4,5,6,8,9],[2,4,5,6,8,9,10],[2,4,5,6,8,10],[2,4,5,6,9],[2,4,5,6,9,10],[2,4,5,6,10],[2,4,5,7],[2,4,5,7,8],[2,4,5,7,8,9],[2,4,5,7,8,9,10],[2,4,5,7,8,10],[2,4,5,7,9],[2,4,5,7,9,10],[2,4,5,7,10],[2,4,5,8],[2,4,5,8,9],[2,4,5,8,9,10],[2,4,5,8,10],[2,4,5,9],[2,4,5,9,10],[2,4,5,10],[2,4,6],[2,4,6,7],[2,4,6,7,8],[2,4,6,7,8,9],[2,4,6,7,8,9,10],[2,4,6,7,8,10],[2,4,6,7,9],[2,4,6,7,9,10],[2,4,6,7,10],[2,4,6,8],[2,4,6,8,9],[2,4,6,8,9,10],[2,4,6,8,10],[2,4,6,9],[2,4,6,9,10],[2,4,6,10],[2,4,7],[2,4,7,8],[2,4,7,8,9],[2,4,7,8,9,10],[2,4,7,8,10],[2,4,7,9],[2,4,7,9,10],[2,4,7,10],[2,4,8],[2,4,8,9],[2,4,8,9,10],[2,4,8,10],[2,4,9],[2,4,9,10],[2,4,10],[2,5],[2,5,6],[2,5,6,7],[2,5,6,7,8],[2,5,6,7,8,9],[2,5,6,7,8,9,10],[2,5,6,7,8,10],[2,5,6,7,9],[2,5,6,7,9,10],[2,5,6,7,10],[2,5,6,8],[2,5,6,8,9],[2,5,6,8,9,10],[2,5,6,8,10],[2,5,6,9],[2,5,6,9,10],[2,5,6,10],[2,5,7],[2,5,7,8],[2,5,7,8,9],[2,5,7,8,9,10],[2,5,7,8,10],[2,5,7,9],[2,5,7,9,10],[2,5,7,10],[2,5,8],[2,5,8,9],[2,5,8,9,10],[2,5,8,10],[2,5,9],[2,5,9,10],[2,5,10],[2,6],[2,6,7],[2,6,7,8],[2,6,7,8,9],[2,6,7,8,9,10],[2,6,7,8,10],[2,6,7,9],[2,6,7,9,10],[2,6,7,10],[2,6,8],[2,6,8,9],[2,6,8,9,10],[2,6,8,10],[2,6,9],[2,6,9,10],[2,6,10],[2,7],[2,7,8],[2,7,8,9],[2,7,8,9,10],[2,7,8,10],[2,7,9],[2,7,9,10],[2,7,10],[2,8],[2,8,9],[2,8,9,10],[2,8,10],[2,9],[2,9,10],[2,10],[3,4],[3,4,5],[3,4,5,6],[3,4,5,6,7],[3,4,5,6,7,8],[3,4,5,6,7,8,9],[3,4,5,6,7,8,9,10],[3,4,5,6,7,8,10],[3,4,5,6,7,9],[3,4,5,6,7,9,10],[3,4,5,6,7,10],[3,4,5,6,8],[3,4,5,6,8,9],[3,4,5,6,8,9,10],[3,4,5,6,8,10],[3,4,5,6,9],[3,4,5,6,9,10],[3,4,5,6,10],[3,4,5,7],[3,4,5,7,8],[3,4,5,7,8,9],[3,4,5,7,8,9,10],[3,4,5,7,8,10],[3,4,5,7,9],[3,4,5,7,9,10],[3,4,5,7,10],[3,4,5,8],[3,4,5,8,9],[3,4,5,8,9,10],[3,4,5,8,10],[3,4,5,9],[3,4,5,9,10],[3,4,5,10],[3,4,6],[3,4,6,7],[3,4,6,7,8],[3,4,6,7,8,9],[3,4,6,7,8,9,10],[3,4,6,7,8,10],[3,4,6,7,9],[3,4,6,7,9,10],[3,4,6,7,10],[3,4,6,8],[3,4,6,8,9],[3,4,6,8,9,10],[3,4,6,8,10],[3,4,6,9],[3,4,6,9,10],[3,4,6,10],[3,4,7],[3,4,7,8],[3,4,7,8,9],[3,4,7,8,9,10],[3,4,7,8,10],[3,4,7,9],[3,4,7,9,10],[3,4,7,10],[3,4,8],[3,4,8,9],[3,4,8,9,10],[3,4,8,10],[3,4,9],[3,4,9,10],[3,4,10],[3,5],[3,5,6],[3,5,6,7],[3,5,6,7,8],[3,5,6,7,8,9],[3,5,6,7,8,9,10],[3,5,6,7,8,10],[3,5,6,7,9],[3,5,6,7,9,10],[3,5,6,7,10],[3,5,6,8],[3,5,6,8,9],[3,5,6,8,9,10],[3,5,6,8,10],[3,5,6,9],[3,5,6,9,10],[3,5,6,10],[3,5,7],[3,5,7,8],[3,5,7,8,9],[3,5,7,8,9,10],[3,5,7,8,10],[3,5,7,9],[3,5,7,9,10],[3,5,7,10],[3,5,8],[3,5,8,9],[3,5,8,9,10],[3,5,8,10],[3,5,9],[3,5,9,10],[3,5,10],[3,6],[3,6,7],[3,6,7,8],[3,6,7,8,9],[3,6,7,8,9,10],[3,6,7,8,10],[3,6,7,9],[3,6,7,9,10],[3,6,7,10],[3,6,8],[3,6,8,9],[3,6,8,9,10],[3,6,8,10],[3,6,9],[3,6,9,10],[3,6,10],[3,7],[3,7,8],[3,7,8,9],[3,7,8,9,10],[3,7,8,10],[3,7,9],[3,7,9,10],[3,7,10],[3,8],[3,8,9],[3,8,9,10],[3,8,10],[3,9],[3,9,10],[3,10],[4,5],[4,5,6],[4,5,6,7],[4,5,6,7,8],[4,5,6,7,8,9],[4,5,6,7,8,9,10],[4,5,6,7,8,10],[4,5,6,7,9],[4,5,6,7,9,10],[4,5,6,7,10],[4,5,6,8],[4,5,6,8,9],[4,5,6,8,9,10],[4,5,6,8,10],[4,5,6,9],[4,5,6,9,10],[4,5,6,10],[4,5,7],[4,5,7,8],[4,5,7,8,9],[4,5,7,8,9,10],[4,5,7,8,10],[4,5,7,9],[4,5,7,9,10],[4,5,7,10],[4,5,8],[4,5,8,9],[4,5,8,9,10],[4,5,8,10],[4,5,9],[4,5,9,10],[4,5,10],[4,6],[4,6,7],[4,6,7,8],[4,6,7,8,9],[4,6,7,8,9,10],[4,6,7,8,10],[4,6,7,9],[4,6,7,9,10],[4,6,7,10],[4,6,8],[4,6,8,9],[4,6,8,9,10],[4,6,8,10],[4,6,9],[4,6,9,10],[4,6,10],[4,7],[4,7,8],[4,7,8,9],[4,7,8,9,10],[4,7,8,10],[4,7,9],[4,7,9,10],[4,7,10],[4,8],[4,8,9],[4,8,9,10],[4,8,10],[4,9],[4,9,10],[4,10],[5,6],[5,6,7],[5,6,7,8],[5,6,7,8,9],[5,6,7,8,9,10],[5,6,7,8,10],[5,6,7,9],[5,6,7,9,10],[5,6,7,10],[5,6,8],[5,6,8,9],[5,6,8,9,10],[5,6,8,10],[5,6,9],[5,6,9,10],[5,6,10],[5,7],[5,7,8],[5,7,8,9],[5,7,8,9,10],[5,7,8,10],[5,7,9],[5,7,9,10],[5,7,10],[5,8],[5,8,9],[5,8,9,10],[5,8,10],[5,9],[5,9,10],[5,10],[6,7],[6,7,8],[6,7,8,9],[6,7,8,9,10],[6,7,8,10],[6,7,9],[6,7,9,10],[6,7,10],[6,8],[6,8,9],[6,8,9,10],[6,8,10],[6,9],[6,9,10],[6,10],[7,8],[7,8,9],[7,8,9,10],[7,8,10],[7,9],[7,9,10],[7,10],[8,9],[8,9,10],[8,10],[9,10]]),
    ([1,1,1], [[1,1], [1,1,1]]),
    ([1,1,1,1], [[1,1], [1,1,1],[1,1,1,1]]),
    ([4,6,4,6], [[4,6],[4,6,6],[4,4],[4,4,6],[6,6]]),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findSubsequences(nums)
    res.sort()
    ans.sort()
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')