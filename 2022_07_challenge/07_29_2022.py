# from pudb import set_trace; set_trace()
from typing import List
from itertools import groupby


class Solution1:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """LeetCode 890
        
        One dict and one set.

        O(N) 60 ms, faster than 29.41%
        """
        res = []
        for word in words:
            p2w = {}
            mapped_w = set()
            for p, w in zip(pattern, word):
                if p not in p2w:
                    if w in mapped_w:
                        break
                    p2w[p] = w
                    mapped_w.add(w)
                elif p2w[p] != w:
                    break
            else:
                res.append(word)
        return res


class Solution2:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """Inspired by my previous solution:

        https://leetcode.com/submissions/detail/496266268/

        But I think I can use groupby for it. UPDATE: Nope, cannot use groupby,
        because of test case like this: ["abc","cba","xyx","yxx","yyx"]

        The groupby pattern of 'abc' and 'xyx' is the same, but they are
        actually different. So we have to go back to lee215's method of
        producing pattern.

        44 ms, faster than 67.99%

        Update: use setdefault => 31 ms, faster than 96.19%
        """

        def get_pattern(word) -> List[int]:
            tmp = {}
            return [tmp.setdefault(w, i) for i, w in enumerate(word)]

        pp = get_pattern(pattern)
        return [word for word in words if get_pattern(word) == pp]
        

sol = Solution2()
tests = [
    (["abc","deq","mee","aqq","dkd","ccc"], "abb", ["mee","aqq"]),
    (["a","b","c"], "a", ["a","b","c"])
]

for i, (words, pattern, ans) in enumerate(tests):
    res = sol.findAndReplacePattern(words, pattern)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
