# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """Naive and simple solution

        O(N), 44ms, 13% ranking.
        """
        return ''.join(word1) == ''.join(word2)


class Solution2:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """Manual approach.

        O(N), 64 ms, Too slow for ranking.
        """
        li = lj = wi = wj = 0
        n1, n2 = len(word1), len(word2)
        while wi < n1 and wj < n2:
            if word1[wi][li] != word2[wj][lj]:
                return False
            li += 1
            lj += 1
            if li == len(word1[wi]):
                wi += 1
                li = 0
            if lj == len(word2[wj]):
                wj += 1
                lj = 0
        return wi == n1 and wj == n2 and li == 0 and lj == 0


class Solution3:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """A smart generator approach. Original:
        https://leetcode.com/explore/featured/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3597/discuss/946392/Python-Two-pointers-space-O(1)
        """

        def gen_letter(words: List[str]):
            for word in words:
                for w in word:
                    yield w
            yield None

        return all(w1 == w2 for w1, w2 in zip(gen_letter(word1), gen_letter(word2)))


sol = Solution3()
tests = [
    (['ab', 'c'], ['a', 'bc'], True),
    (['a', 'cb'], ['ab', 'c'], False),
    (['abc', 'd', 'defg'], ['abcddefg'], True),
    (['abc', 'd', 'defg'], ['abcddef'], False),
]

for i, (word1, word2, ans) in enumerate(tests):
    res = sol.arrayStringsAreEqual(word1, word2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
