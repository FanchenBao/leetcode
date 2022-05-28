# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        counter = Counter(words)
        return sum(counter[s[:i]] for i in range(1, len(s) + 1))


class Solution2:
    def countPrefixes(self, words: List[str], s: str) -> int:
        """This is the solution from lee215

        https://leetcode.com/problems/count-prefixes-of-a-given-string/discuss/1994777/JavaC%2B%2BPython-Starts-With
        """
        return sum(s.startswith(w) for w in words)



sol = Solution2()
tests = [
    (["a","b","c","ab","bc","abc"], "abc", 3),
    (["a","a"], "aa", 2),
]

for i, (words, s, ans) in enumerate(tests):
    res = sol.countPrefixes(words, s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
