# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
from bisect import bisect_right


class Solution1:
    def LCS(self, s1, s2) -> int:
        M, N = len(s1), len(s2)
        dp = [0] * (N + 1)
        for i in range(1, M + 1):
            temp = [0] * (N + 1)
            for j in range(1, N + 1):
                if s1[i - 1] == s2[j - 1]:
                    temp[j] = dp[j - 1] + 1
                else:
                    temp[j] = max(dp[j], temp[j - 1])
            dp = temp
        return dp[N]

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        """Naive solution TLE. We are running the same LCS algorithm for each
        word in words.
        """
        return sum(self.LCS(s, w) == len(w) for w in words)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.matches = []
        self.word = ''

    def __repr__(self):
        return f'{self.children.keys()}, {self.matches}, {self.word}'


class Solution2:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        """TLE as well.
        """
        root = TrieNode()
        for w in words:
            node = root
            for le in w:
                if le not in node.children:
                    node.children[le] = TrieNode()
                node = node.children[le]
            node.word = w

        N = len(s)
        self.res = 0

        def dfs(node: TrieNode, pre_indices: List[int], cur_le: str) -> None:
            last_match = -1
            for pre_idx in pre_indices:
                if pre_idx + 1 > last_match:
                    for i in range(pre_idx + 1, N):
                        if s[i] == cur_le:
                            node.matches.append(i)
                            last_match = i
            if node.matches:
                if node.word:
                    self.res += 1
                for le, child in node.children.items():
                    dfs(child, node.matches, le)

        for le, child in root.children.items():
            dfs(child, range(-1, N - 1), le)
        return self.res


class Solution3:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        """LeetCode 792

        The idea is that to match any letter in word to s, we try to find the
        earliest occurrence of letter in s. This is because the more to the
        left we match a letter, the more chance we have to match the remaining
        of word. We can turn s into a mapping with key being the letter and
        value being a list of indices where the key occurrs in s and in order.

        Then for each letter in word, we keep track of the smallest index that
        allows matching for the previous letter. And we use binary search to
        check where the previous matching index is located in the current list
        of indices of the current letter. If there are indices in the current
        letter that are larger than the previous matching index, we reassign
        the previous matching index to the smallest index of the current letter
        that is larger than the previous matching index, and we continue.

        We stop when the current letter is not present in the mapping, or there
        is no more indices left to match the current letter.

        O(M + Nlog(M)), where M is the length of s and N is the length of the
        total number of letters in words. 596 ms, 59% ranking.
        """
        mapping = defaultdict(list)
        for i, le in enumerate(s):
            mapping[le].append(i)
        res = 0
        for w in words:
            mi = -1
            for le in w:
                if le not in mapping:
                    break
                mapping_i = bisect_right(mapping[le], mi)
                if mapping_i == len(mapping[le]):
                    break
                mi = mapping[le][mapping_i]
            else:
                res += 1
        return res


sol = Solution3()
tests = [
    ('abcde', ['a', 'bb', 'acd', 'ace'], 3),
    ('dsahjpjauf', ['ahjpjau', 'ja', 'ahbwzgqnuk', 'tnmlanowax'], 2),
]

for i, (s, words, ans) in enumerate(tests):
    res = sol.numMatchingSubseq(s, words)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
