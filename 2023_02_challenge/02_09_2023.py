# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution1:
    def distinctNames(self, ideas: List[str]) -> int:
        """TLE
        """
        suff = defaultdict(set)
        pref = defaultdict(set)
        for idea in ideas:
            p, s = idea[0], idea[1:]
            suff[s].add(p)
            pref[p].add(s)
        res = 0
        for s in suff:
            for p in pref:
                if s in pref[p]:
                    pref[p].remove(s)
                else:
                    cur = 0
                    for pp in suff[s]:
                        cur += len(pref[p] - pref[pp])
                    res += 2 * cur
        return res


class Solution2:
    def distinctNames(self, ideas: List[str]) -> int:
        """LeetCode 2306

        We create a mapping with prefix (i.e., the first letter) as key, and
        a set of suffixes as value.

        For each prefix, we can potentially match it to a different prefix. To
        eliminate the not allowed cases, it is required that all suffixes that
        exist in the sets of both prefixes are eliminated. We can do this by
        set subtraction. After we obtain the total number of suffixes in both
        prefixes that have no overlap, each suffix in one prefix can be matched
        to each suffix in the other prefix. Thus, the total number of names
        is the product. And since we can change the oder, the product needs to
        double.

        We keep doing this for each pair of prefixes without repeating.

        O(26 * 26 * N), where N = len(ideas), 783 ms, faster than 69.56%
        """
        pref = defaultdict(set)
        for idea in ideas:
            pref[idea[0]].add(idea[1:])
        res = 0
        ps = list(pref.keys())
        for i in range(len(ps)):
            for j in range(i + 1, len(ps)):
                res += 2 * len(pref[ps[j]] - pref[ps[i]]) * len(pref[ps[i]] - pref[ps[j]])
        return res


class Solution3:
    def distinctNames(self, ideas: List[str]) -> int:
        """This is from the official solution, which is almost exactly the same
        but with better implementation where we only need to do set logic once.

        We just need to find the suffixes that appear in both sets and deduct
        their count. We don't have to do set arithmetic twice.

        549 ms, faster than 96.74%
        """
        pref = defaultdict(set)
        for idea in ideas:
            pref[idea[0]].add(idea[1:])
        res = 0
        ps = list(pref.keys())
        for i in range(len(ps)):
            for j in range(i + 1, len(ps)):
                rep = len(pref[ps[i]] & pref[ps[j]])
                res += 2 * (len(pref[ps[j]]) - rep) * (len(pref[ps[i]]) - rep)
        return res


sol = Solution3()
tests = [
    (["coffee","donuts","time","toffee"], 6),
    (["lack","back"], 0),
]

for i, (ideas, ans) in enumerate(tests):
    res = sol.distinctNames(ideas)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
