# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict
import string


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """LeetCode 336

        We failed today. Had to read the solution from my previous attempt more
        than a year ago. Apparently, I solved this problem last time. But this
        time, I got bogged down by trying to implement a Trie. In reality, we
        just need to analyze the situation of appending to the right and
        appending to the left.

        Also note that we don't have to check for duplicates, because the
        condition for matching to the right is different from to the left. This
        means, if B is matched to A from the right, we are using the right most
        letters of A as the center piece. Thus, it is not possible to match A
        to B from the left, because when matching to the left, we use the left
        most letters of B as the center piece. Since these are two different
        scenarios, they will not duplicate.

        O(NM^2), 7602 ms, faster than 14.94%
        """
        idx_map = {word: i for i, word in enumerate(words)}
        res = []
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                # we try to append to the right. This requires that if word[j:]
                # is a palindrome, then we must match word[:j][::-1] in idx_map
                if word[j:] == word[j:][::-1]:
                    k = idx_map.get(word[:j][::-1], -1)
                    if i != k and k >= 0:
                        res.append([i, k])
                # we try to append to the left. This requires that if word[:j]
                # is a palindrome, then we must match word[j:][::-1] in idx_map
                if j > 0 and word[:j] == word[:j][::-1]:
                    k = idx_map.get(word[j:][::-1], -1)
                    if i != k and k >= 0:
                        res.append([k, i])
        return res


sol = Solution()
tests = [
    (["abcd","dcba","lls","s","sssll"], [[0,1],[1,0],[3,2],[2,4]]),
    (["bat","tab","cat"], [[0,1],[1,0]]),
    (["a",""], [[0,1],[1,0]]),
    (["a","abc","aba",""], [[0,3],[3,0],[2,3],[3,2]]),
    (["a","b","c","ab","ac","aa"], [[3,0],[1,3],[4,0],[2,4],[5,0],[0,5]]),
    (["ab","ba","abc","cba"], [[0,1],[1,0],[2,1],[2,3],[0,3],[3,2]]),
    (["aba","ba","a","caba"], [[0,1],[2,1],[0,3]]),
]

for i, (words, ans) in enumerate(tests):
    res = sol.palindromePairs(words)
    res.sort()
    ans.sort()
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
