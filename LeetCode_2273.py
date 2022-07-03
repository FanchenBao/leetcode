# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        """O(N), 63 ms, faster than 83.91%"""
        res = []
        while len(words) > 1:
            if sorted(words[-1]) == sorted(words[-2]):
                words.pop()
            else:
                res.append(words.pop())
        res.append(words.pop())
        return res[::-1]


sol = Solution()
tests = [
    (["abba","baba","bbaa","cd","cd"], ["abba","cd"]),
    (["a","b","c","d","e"], ["a","b","c","d","e"]),
]

for i, (words, ans) in enumerate(tests):
    res = sol.removeAnagrams(words)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
