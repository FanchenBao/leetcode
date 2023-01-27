# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution1:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """LeetCode 472

        We have to sort by length of each word, because this can guarantee that
        if a later word is a concatenation, it must be a concatenation of some
        of the previous words.

        My original idea is to use a trie for checking whether a word is a
        concat, but I realize that traversing the trie in the case of 'cat' and
        'cats' would require recursion, because we need to try 'cat' first and
        if it doesn't work, we need to try 'cats'. But all of this with trie
        can be complicated, and I don't want to use it as the first option.

        Then I realize that the max length of each word is at most 30. That
        means if we group the non-concat by their length, to check whether a
        word is a concat, we only need to go through at most 30 times of previous
        groups of non-concat. And if we make the group as a set, each check
        is O(1). Even if we have to go through the entire 30 times for each
        check, it is still not slow, because the total number of rounds is also
        limited.

        Hence, the solution.

        O(NlogN + K^3 * N), where N = len(words), K is the max length of a single
        word. Note that the dfs takes O(K^3). Recursion is O(K^2), for each
        recurison we perform string splicing, which is another O(K).

        572 ms, faster than 56.45%
        """
        words.sort(key=lambda w: len(w))
        m = defaultdict(set)

        def dfs(i: int, word: str) -> bool:
            if i == len(word):
                return True
            for length, nonconcat in m.items():
                if word[i:i + length] in nonconcat:
                    if dfs(i + length, word):
                        return True
            return False

        res = []
        for word in words:
            if dfs(0, word):
                res.append(word)
            else:
                m[len(word)].add(word)
        return res


class Solution2:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """DP solution. Almost the same as Solution1, but using a different
        perspective.

        For each word, we determine whether a prefix is a nonconcat. If it is,
        we through the remaining to the recurion again. DP happens when a
        remaining is already in a nonconcat or concat group, we don't have to
        process it again.

        O(NlogN, K^3 * N), 556 ms, faster than 57.10%
        """
        words.sort(key=lambda w: len(w))
        nonconcat = set()
        res = set()

        def is_concat(idx: int, word: int) -> bool:
            if word[idx:] in nonconcat or word[idx:] in res:
                return True
            if idx == len(word):
                return False
            for j in range(idx, len(word)):
                if word[idx:j + 1] in nonconcat and is_concat(j + 1, word):
                    return True
            return False

        for word in words:
            if is_concat(0, word):
                res.add(word)
            else:
                nonconcat.add(word)
        return list(res)


sol = Solution2()
tests = [
    (["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"], ["catsdogcats","dogcatsdog","ratcatdogcat"]),
    (["cat","dog","catdog"], ["catdog"]),
]

for i, (words, ans) in enumerate(tests):
    res = sol.findAllConcatenatedWordsInADict(words)
    res.sort()
    ans.sort()
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
