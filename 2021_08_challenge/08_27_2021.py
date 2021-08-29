# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict, Counter


class Solution1:
    def lcs(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [0] * (n + 1)
        for i in range(1, m + 1):
            temp = [0] * (n + 1)
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    temp[j] = dp[j - 1] + 1
                else:
                    temp[j] = max(temp[j - 1], dp[j])
            dp = temp
        return temp[n]

    def findLUSlength(self, strs: List[str]) -> int:
        """LeetCode 522

        This is a complex problem, but not necesssarily complicated. First,
        we realize that a longer string is always an uncommon subsequence of a
        shorter string. Therefore, it is the best strategy to examine long
        strings first. Second, we realize that for stirngs of the same length,
        if there exists a unique string, then that string is the uncommon
        subsequence of all the other strings of the same length. Therefore, we
        shall start with the longest strings. If there is a unique one among the
        longest strings, then we can return the length of that string
        immediately.

        Things get a bit more complex if there is no unique strings of the
        longest size. This means, all the strings of the longest size are the
        same. In that case, we have to look for a string of the next longest
        size. We do the same: first check if there is any uniques. If there is
        not, we continue with the next longest size. If there are uniques, then
        the unique will be the uncommon subsequence of all the strings of the
        same size or smaller. BUT, we must also check whether this string is NOT
        a common subsequence of all the strings of longer size. For this, we
        need to run LCS between the current string and all the strings of longer
        size. If the LCS returns a size that is equal to the current string,
        that means the current string is a subsequence of a longer string and
        that we cannot use it. Otherwise, the current string is a good one and
        we can return its size.

        We will see how other people figure out the time complexity.

        60 ms, 15% ranking.
        """
        groups = defaultdict(Counter)
        for s in strs:
            groups[len(s)][s] += 1
        sorted_sizes = sorted(groups, reverse=True)
        for i, size in enumerate(sorted_sizes):
            for cur_s, count in groups[size].items():
                if count == 1:
                    if i == 0:
                        return size
                    is_lcs = False
                    for j in range(i):
                        for pre_s in groups[sorted_sizes[j]]:
                            if self.lcs(cur_s, pre_s) == size:
                                is_lcs = True
                                break
                        if is_lcs:
                            break
                    if not is_lcs:
                        return size
        return -1


class Solution2:
    def is_subseq(self, s1: str, s2: str) -> int:
        """check whether s1 is a subsequence of s2, given len(s1) <= len(s2)"""
        iter_s2 = iter(s2)
        return all(c in iter_s2 for c in s1)

    def findLUSlength(self, strs: List[str]) -> int:
        """Similar idea as Solution1, but to reduce all the clutter, we can
        simply test whether a long string is a subsequence of all other strings.
        Any long string that satisfies this requirement is the solution. In
        other words, we brute force it without having to find uniques and stuff.
        We can do this because the total size of strs and the size of each str
        is very small.

        The most impressive is how DBabichev examines whether one string is a
        subsequence of another string. While I use LCS for this, he uses
        iterator and the "in" expression with iterator. Refer to my comment
        about how this works: https://leetcode.com/problems/longest-uncommon-subsequence-ii/discuss/1428753/Python-O(n2k)-solution-explained/1063028

        Courtesy: https://leetcode.com/problems/longest-uncommon-subsequence-ii/discuss/1428753/Python-O(n2k)-solution-explained
        """
        sorted_strs = sorted(strs, key=lambda s: -len(s))
        for i, s in enumerate(sorted_strs):
            valid = True
            for j, s_ in enumerate(sorted_strs):
                if len(s_) < len(s):
                    break
                if j == i:
                    continue
                if self.is_subseq(s, s_):
                    valid = False
                    break
            if valid:
                return len(s)
        return -1


sol = Solution2()
tests = [
    (['aba', 'cdc', 'eae'], 3),
    (['aaa', 'aaa', 'aa'], -1),
]

for i, (strs, ans) in enumerate(tests):
    res = sol.findLUSlength(strs)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
