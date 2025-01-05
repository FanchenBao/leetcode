# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict, Counter
from bisect import bisect_left, bisect_right


class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        """
        We find all the pairs that have the same products. Then we check how
        many subsequences we can create within each list of pairs.

        This solution may TLE
        """
        products = defaultdict(list)
        N = len(nums)
        for p in range(N - 4):
            for r in range(p + 4, N):
                products[nums[p] * nums[r]].append([p, r])
        res = 0
        for pairs in products.values():
            for i in range(len(pairs) - 1):
                for j in range(i + 1, len(pairs)):
                    p, r = pairs[i]
                    q, s = pairs[j]
                    if q - p > 1 and r - q > 1 and s - r > 1:
                        res += 1
        return res


class Solution2:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        """
        We will binary search it when we try to create subsequences

        TLE
        """
        products = defaultdict(list)
        N = len(nums)
        for p in range(N - 4):
            for r in range(p + 4, N):
                products[nums[p] * nums[r]].append([p, r])
        res = 0
        for pairs in products.values():
            for i in range(len(pairs) - 1):
                p, r = pairs[i]
                q_lo = bisect_left(pairs, p + 2, lo=i + 1, key=lambda pair: pair[0])
                q_hi = (
                    bisect_right(pairs, r - 2, lo=i + 1, key=lambda pair: pair[0]) - 1
                )
                for j in range(q_lo, q_hi + 1):
                    if pairs[j][1] - r > 1:
                        res += 1
        return res


class Solution3:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        """
        This is from the hint. Instead of finding p * r == q * s, we find
        p / q = s / r. We put all the matching (p, q) and (r, s) pairs in the
        same array, and then use binary search to create subsequences.

        It is a much better approach compared to solution2, because the binary
        search only needs to consider s >= q + 1, and all potential s are sorted
        already.

        O(N^2logN), 9041 ms, 5.03%
        """
        ratios_pq = defaultdict(list)
        ratios_rs = defaultdict(list)
        N = len(nums)
        for i in range(N - 2):
            for j in range(i + 2, N):
                g_pq = math.gcd(nums[i], nums[j])
                ratios_pq[(nums[i] // g_pq, nums[j] // g_pq)].append((i, j))
                g_rs = math.gcd(nums[j], nums[i])
                ratios_rs[(nums[j] // g_rs, nums[i] // g_rs)].append((i, j))
        res = 0
        for ratio, pairs in ratios_pq.items():
            for i in range(len(pairs)):
                _, q = pairs[i]
                r_idx = bisect_left(ratios_rs[ratio], q + 2, key=lambda tups: tups[0])
                res += len(ratios_rs[ratio]) - r_idx
        return res


class Solution4:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        """
        Optimized version of solution 3

        O(N^2logN), 4014 ms, 17.51%
        """
        ratios_pq = defaultdict(list)
        ratios_rs = defaultdict(list)
        N = len(nums)
        for i in range(N - 2):
            for j in range(i + 2, N):
                g_pq = math.gcd(nums[i], nums[j])
                ratios_pq[(nums[i] // g_pq, nums[j] // g_pq)].append(j)
                g_rs = math.gcd(nums[j], nums[i])
                ratios_rs[(nums[j] // g_rs, nums[i] // g_rs)].append(i)
        res = 0
        for ratio, qs in ratios_pq.items():
            for q in qs:
                r_idx = bisect_left(ratios_rs[ratio], q + 2)
                res += len(ratios_rs[ratio]) - r_idx
        return res


class Solution5:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        """
        Further optimization

        O(N^2logN), 3724 ms 19.43%
        """
        ratios_pq = defaultdict(list)
        ratios_rs = defaultdict(list)
        N = len(nums)
        for i in range(N - 2):
            for j in range(i + 2, N):
                g = math.gcd(nums[i], nums[j])
                ratios_pq[(nums[i] // g, nums[j] // g)].append(j)
                ratios_rs[(nums[j] // g, nums[i] // g)].append(i)
        res = 0
        for ratio, qs in ratios_pq.items():
            for q in qs:
                r_idx = bisect_left(ratios_rs[ratio], q + 2)
                res += len(ratios_rs[ratio]) - r_idx
        return res


class Solution6:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        """
        This solution is from lee215
        https://leetcode.com/problems/count-special-subsequences/solutions/6199506/java-c-python-hashmap

        The key is to iterate with r. For each r position, we can iteratively
        accumulate the count of all nums[p] / nums[q] to the left of r.
        Then we go through s, and for each nums[r] / nums[s], we add the count
        from nums[p] / nums[q]

        The brilliance of this solution is to use r as the anchor for the
        iteration and use counter to quickly find the number of subsequences.

        O(N^2), 2220 ms, 37.42%
        """
        ratios: Counter = Counter()
        N = len(nums)
        res = 0
        for r in range(4, N - 2):
            q = r - 2
            for p in range(q - 1):
                g = math.gcd(nums[p], nums[q])
                ratios[(nums[p] // g, nums[q] // g)] += 1
            for s in range(r + 2, N):
                g = math.gcd(nums[s], nums[r])
                res += ratios[(nums[s] // g, nums[r] // g)]
        return res


class Solution7:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        """
        Same as solution6, but directly use float as key

        O(N^2), 1405 ms, 79.17%
        """
        ratios: Counter = Counter()
        N = len(nums)
        res = 0
        for r in range(4, N - 2):
            q = r - 2
            for p in range(q - 1):
                ratios[(nums[p] / nums[q])] += 1
            for s in range(r + 2, N):
                res += ratios[nums[s] / nums[r]]
        return res


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
