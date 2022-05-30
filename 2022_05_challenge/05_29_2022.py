# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def maxProduct(self, words: List[str]) -> int:
        """LeetCode 318

        This is a naive solution. I am surprised that it actually passed the OJ
        It basically goes through all pairs of words, check whether they have
        any shoared letter, and then compute product, if allowed.

        The reason it passed the OJ might be because the set intersection
        operation is O(1), because there are only 26 letters.

        O(N^2), 1386 ms, faster than 47.00%
        """
        sets = [set(w) for w in words]
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not sets[i].intersection(sets[j]):
                    res = max(res, len(words[i]) * len(words[j]))
        return res


class Solution2:
    def maxProduct(self, words: List[str]) -> int:
        """Using bitmap to check whether two words share letter

        614 ms, faster than 75.16% of Python3. The bitmask is definitely much
        easier to find out if two pairs share common letters. 
        """
        bms = []
        for w in words:
            bms.append(0)
            for le in w:
                bms[-1] |= (1 << (ord(le) - ord('a')))
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not (bms[i] & bms[j]):
                    res = max(res, len(words[i]) * len(words[j]))
        return res




sol = Solution2()
tests = [
    (["abcw","baz","foo","bar","xtfn","abcdef"], 16),
    (["a","ab","abc","d","cd","bcd","abcd"], 4),
    (["a","aa","aaa","aaaa"], 0),
]

for i, (words, ans) in enumerate(tests):
    res = sol.maxProduct(words)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
