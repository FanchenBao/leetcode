# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict, Counter
from bisect import bisect_left


class Solution1:
    def takeCharacters(self, s: str, k: int) -> int:
        """Pretty bad, and I don't like this solution at all. But it worked.

        We produce prefix sum on the count of 'a', 'b', and 'c' going from left
        to right, and right to left.

        Then we go from left to right taking 0, 1, 2, ... minutes. For each such
        minute, we know the number of 'a', 'b', 'c' we can take from the left.
        Then we go to the right and binary search to find the earliest minutes
        needed to satisfy k for all three letters. We then keep track of the min
        of all the earliest minutes, and that is our solution.

        O(NlogN), 2292 ms, faster than 11.38%
        """
        N = len(s)
        lpsum = {"a": [0], "b": [0], "c": [0]}
        rpsum = {"a": [0], "b": [0], "c": [0]}
        for i in range(N):
            for le in lpsum.keys():
                lpsum[le].append(lpsum[le][-1] + int(le == s[i]))
        for j in range(N - 1, -1, -1):
            for le in lpsum.keys():
                rpsum[le].append(rpsum[le][-1] + int(le == s[j]))
        res = math.inf
        for lt in range(len(lpsum["a"])):
            if lt >= res:
                break
            t = 0
            for le in lpsum.keys():
                lc = lpsum[le][lt]
                rt = bisect_left(rpsum[le], k - lc)
                if lt + rt > N:
                    break
                t = max(t, lt + rt)
            else:
                res = min(res, t)
        return res if res < math.inf else -1


class Solution2:
    def takeCharacters(self, s: str, k: int) -> int:
        """Convert the problem to finding at most count[le] - k number of a, b
        or c in a substring across the middle of s.

        This can be solved with sliding window.

        Ref: https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/discuss/2948183/Python-clean-12-line-sliding-window-solution-with-explanation

        O(N), 865 ms, faster than 29.01%

        UPDATE: during sliding window, we only need to check the current letter
        437 ms, faster than 60.28%
        """
        letters = "abc"
        limit = Counter(s)
        # find limit
        for le in letters:
            if limit[le] < k:
                return -1
            limit[le] -= k
        i = 0
        c = Counter()
        max_l = 0
        for j in range(len(s)):
            c[s[j]] += 1
            while c[s[j]] > limit[s[j]]:
                c[s[i]] -= 1
                i += 1
            max_l = max(max_l, j - i + 1)
        return len(s) - max_l


class Solution3:
    def takeCharacters(self, s: str, k: int) -> int:
        """
        This is the attempt oon 2024-11-22. I will do my best not to peek at
        the other two solutions above.

        This solution will use a wrap-around technique to implement sliding
        window to find the smallest sliding window that spans the start and
        end of the string such that the letters in the span fulfill the
        requirement.

        O(N), 238 ms, faster than 51.50%
        """
        N = len(s)
        if 3 * k > N:
            return -1
        counter = Counter(s)
        if not all(counter[le] >= k for le in ["a", "b", "c"]):
            return -1
        i, j = 0, N - 1
        res = N
        while i <= j and counter[s[i]] - 1 >= k:
            counter[s[i]] -= 1
            i += 1
        res = j - i + 1
        while i < N:
            j = (j + 1) % N
            counter[s[j]] += 1
            while i < N and (counter[s[i]] - 1 >= k or i <= j):
                counter[s[i]] -= 1
                i = i + 1
            res = min(res, N - i + j + 1)
        return min(res, j - (i % N) + 1)


sol = Solution2()
tests = [
    ("aabaaaacaabc", 2, 8),
    ("a", 1, -1),
    ("aabaaaacaabcb", 2, 6),
    ("acba", 1, 3),
    ("cbaabccac", 3, -1),
    ("abc", 1, 3),
]

for i, (s, k, ans) in enumerate(tests):
    res = sol.takeCharacters(s, k)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
