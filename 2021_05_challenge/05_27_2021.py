# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def maxProduct(self, words: List[str]) -> int:
        """LeetCode 318

        I thought I am going to time out with this very naive method. We set
        aside lengths and sets of each word. We then perform pair-wise
        intersection between the word sets, and record the product of lengths if
        the intersection comes back an empty set.

        O(N^2 * M) where M is the length of each word. 984 ms, 49% ranking.
        """
        lengths = [len(w) for w in words]
        sets = [set(w) for w in words]
        res = 0
        for i in range(len(sets)):
            for j in range(i + 1, len(sets)):
                if not sets[i].intersection(sets[j]):
                    res = max(res, lengths[i] * lengths[j])
        return res


class Solution2:
    def maxProduct(self, words: List[str]) -> int:
        """The consensus on the discussion is to use a bitmap to check for
        whether two words share common letters

        O(N * M + 1), where N is the length of word, M the average length of
        each word, and we consider the size of mask_map to be constant, because
        it has maximum 2^26 items.

        208 ms, 91% ranking.
        """
        mask_map = {}
        for w in words:
            mask = 0
            for le in w:
                mask |= (1 << (ord(le) - 97))
            mask_map[mask] = max(mask_map.get(mask, 0), len(w))
        res = 0
        for a in mask_map:
            for b in mask_map:
                if not (a & b):
                    res = max(res, mask_map[a] * mask_map[b])
        return res


sol = Solution2()
tests = [
    (['abcw', 'baz', 'foo', 'bar', 'xtfn', 'abcdef'], 16),
    (['a', 'ab', 'abc', 'd', 'cd', 'bcd', 'abcd'], 4),
    (['a', 'aa', 'aaa', 'aaaa'], 0),
]

for i, (words, ans) in enumerate(tests):
    res = sol.maxProduct(words)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
