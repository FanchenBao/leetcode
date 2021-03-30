# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
from bisect import bisect_left, bisect_right
from functools import reduce


class Solution1:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """TLE"""
        env_dict = defaultdict(list)
        for w, h in envelopes:
            env_dict[w].append(h)
        for hs in env_dict.values():
            hs.sort()
        ws = sorted(env_dict.keys())
        dp = {w: [1] * len(env_dict[w]) for w in ws}
        for i, w in enumerate(ws[1:], start=1):
            for j, h in enumerate(env_dict[w]):
                for k in range(i - 1, -1, -1):
                    pot_w = ws[k]
                    idx = bisect_left(env_dict[pot_w], h)
                    if idx - 1 >= 0:
                        dp[w][j] = max(dp[w][j], dp[pot_w][idx - 1] + 1)
        return reduce(lambda r, vs: max(r, max(vs)), dp.values(), 0)


class Solution2:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """TLE"""
        envelopes.sort(key=lambda tup: (tup[0], tup[1]))
        dp = [1] * len(envelopes)
        for i in range(1, len(envelopes)):
            for j in range(i - 1, -1, -1):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class Solution3:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """TLE"""
        envelopes.sort(key=lambda tup: (tup[0], tup[1]))
        dp = [[1, {i}] for i in range(len(envelopes))]
        for i in range(1, len(envelopes)):
            w, h = envelopes[i]
            pot_indices = set(range(i))
            while pot_indices:
                ni = max(pot_indices)
                nw, nh = envelopes[ni]
                if nw < w and nh < h:
                    if dp[ni][0] + 1 > dp[i][0]:
                        dp[i][0] = dp[ni][0] + 1
                        dp[i][1] = {i}.union(dp[ni][1])
                    pot_indices -= dp[ni][1]
                else:
                    pot_indices.remove(ni)
        return max(v for v, _ in dp)


class Solution4:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """I failed this problem. I checked the solution, and below is the
        implementation of this answer:
        https://leetcode.com/problems/russian-doll-envelopes/discuss/82763/Java-NLogN-Solution-with-Explanation

        The basic idea is to sort the envelopes based on width acending and sort
        height when width is the same descending. Then the question becomes to
        find the longest increasing subsequence (LIS) of height.

        A dumb DP solution for LIS is O(N^2), which is likely TLE (but I am not
        sure). The correct solution for length of LIS is O(NlogN), as shown
        below. I have done LIS before, but I completely forgot about this
        solution. It keeps an array for the current 'LIS', and constantly swaps
        in the smaller value encountered. Thus, the 'LIS' is not the correct LIS
        but its length is correct. We basically try to keep 'LIS' as small as
        possible, thus we are able to append more values to it. Appending is the
        only action that grows LIS. For a better explanation, check the comment
        section of the solution for LIS:

        https://leetcode.com/problems/longest-increasing-subsequence/solution/303027

        O(NlogN), 144 ms, 92% ranking.
        """
        # notice we sort ascending on width but descending on height
        envelopes.sort(key=lambda tup: (tup[0], -tup[1]))
        hs = [h for _, h in envelopes]
        dp = [hs[0]]
        for h in hs[1:]:
            idx = bisect_right(dp, h)
            if dp[idx - 1] == h:
                continue
            if idx == len(dp):
                dp.append(h)
            else:
                dp[idx] = h
        return len(dp)


sol = Solution4()
tests = [
    ([[5, 4], [6, 4], [6, 7], [2, 3]], 3),
    ([[1, 1], [1, 1], [1, 1]], 1),
    ([[2, 100], [3, 200], [4, 300], [5, 500], [5, 400], [5, 250], [6, 370], [6, 360], [7, 380]], 5),
    ([[46, 89], [50, 53], [52, 68], [72, 45], [77, 81]], 3),
    ([[10, 8], [1, 12], [6, 15], [2, 18]], 2),
    ([[1728, 7730], [3676, 7605], [4755, 9957], [6451, 5797], [4660, 9565], [1753, 3275], [5291, 6469], [7279, 7610], [4154, 792], [3260, 4948]], 5),
]

for i, (envelopes, ans) in enumerate(tests):
    res = sol.maxEnvelopes(envelopes)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
