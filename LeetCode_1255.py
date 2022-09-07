# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        """Since the length of words is only 14, we can brute force this
        problem without issue. Brute force is carried by DFS with backtracking.

        UPDATE: prune all the words that cannot be formed by letters before entering
        BFS

        O(2^N), 153 ms, faster than 35.93%
        """
        self.counter = Counter(letters)
        counter_words = []
        score_words = []
        for word in words:
            c = Counter(word)
            if not c - self.counter:
                counter_words.append(c)
                score_words.append(
                    sum(v * score[ord(k) - 97] for k, v in c.items()),
                )
        self.res = 0
        N = len(counter_words)

        def dfs(idx: int, cur_score: int) -> None:
            if idx == N:
                self.res = max(self.res, cur_score)
            else:
                for i in range(idx, N):
                    c = counter_words[i]
                    if not c - self.counter:
                        self.counter -= c
                        dfs(i + 1, cur_score + score_words[i])
                        self.counter += c
                    else:
                        dfs(i + 1, cur_score)

        dfs(0, 0)
        return self.res


sol = Solution()
tests = [
    (["dog","cat","dad","good"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0], 23),
    (["xxxz","ax","bx","cx"], ["z","a","b","c","x","x","x"], [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10], 27),
    (["leetcode"], ["l","e","t","c","o","d"], [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0], 0),
    (["add","dda","bb","ba","add"], ["a","a","a","a","b","b","b","b","c","c","c","c","c","d","d","d"], [3,9,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 51),
]

for i, (words, letters, score, ans) in enumerate(tests):
    res = sol.maxScoreWords(words, letters, score)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
