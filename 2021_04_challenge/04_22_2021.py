# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        """LeetCode 554

        By turning each row into a prefix sum, we can easily see where the
        gaps on each row. For instance, given a wall like this:

        [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

        This is the aligned prefix sum of each row:

        1   3   5 6
            3 4   6
        1     4   6
          2       6
            3 4   6
        1     4 5 6

        Clearly, we can see that at width 4, we have the most number of gaps,
        which in turn means at width 4, we cross the least number of bricks.
        Therefore, the solution is to compute the prefix sum for each row, and
        keep counting the frequency of each width. The final result is the
        height of the wall minus the max number of gaps at a certain width.

        O(NM) where N is the average number of bricks per row and M is the
        number of rows. 180 ms, 72% ranking.
        """
        gap_count = Counter()
        width = 0
        for row in wall:
            pre_sum = 0
            for br in row:
                pre_sum += br
                gap_count[pre_sum] += 1
            width = pre_sum
        gap_count[width] = 0  # do not include the max width
        return len(wall) - max(gap_count.values())


# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
