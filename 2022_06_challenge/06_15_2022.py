# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution1:
    def longestStrChain(self, words: List[str]) -> int:
        """LeetCode 1048

        The key of this solution is going from righ to left, because it reduces
        a lot of the search space. Also, the BFS idea is quite straightforward
        from the question set up.

        O(M^2N), where M is the average length of the words, and N is the total
        number of the words. 204 ms, faster than 67.19%
        """
        len_words = defaultdict(set)
        for w in words:
            len_words[len(w)].add(w)
        res = 1
        queue = []
        for length in range(max(len_words) + 1, -1, -1):
            temp = []
            visited = set()
            for w, step in queue:
                res = max(res, step)
                for i in range(length):
                    cand = w[:i] + w[i + 1:]
                    if cand in len_words[length - 1] and cand not in visited:
                        temp.append((cand, step + 1))
                        visited.add(cand)
            for w in len_words[length - 1]:
                if w not in visited:
                    temp.append((w, 1))
            queue = temp
        return res


class Solution2:
    def longestStrChain(self, words: List[str]) -> int:
        """DP solution. I have to say that it is better and easier to code than
        the BFS. Time complexity is the same as Solution1
        """
        dp = defaultdict(int)
        words.sort(key=lambda w: len(w))
        min_len = len(words[0])
        for w in words:
            if len(w) == min_len:
                dp[w] = 1
            else:
                for i in range(len(w)):
                    cand = w[:i] + w[i + 1:]
                    dp[w] = max(dp[w], dp[cand] + 1)
        return max(dp.values())
        

sol = Solution2()
tests = [
    (["a","b","ba","bca","bda","bdca"], 4),
    (["xbc","pcxbcf","xb","cxbc","pcxbc"], 5),
    (["abcd","dbqca"], 1),
]

for i, (words, ans) in enumerate(tests):
    res = sol.longestStrChain(words)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
