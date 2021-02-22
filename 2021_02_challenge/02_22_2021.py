# from pudb import set_trace; set_trace()
from typing import List
import heapq


class Solution1:
    def contains(self, s, word) -> bool:
        i = 0
        for le in word:
            while i < len(s) and s[i] != le:
                i += 1
            if i == len(s):
                return False
            i += 1
        return True

    def findLongestWord(self, s: str, d: List[str]) -> str:
        """We first sort the original dictionary in such way that the result
        is ordered first by length in descending order and second by
        lexicographic in ascending order if the length is the same.

        Then for each word in the sorted dictionary, we check whether the word
        is contained in the s. We return the first word that matches to s. If
        no word matches, we return empty string.

        O(NlogN + N * x), 404 ms, 60% ranking
        """
        d.sort(key=lambda s_: (-len(s_), s_))
        for word in d:
            if self.contains(s, word):
                return word
        return ''


class Solution2:
    def contains(self, s, word) -> bool:
        i = 0
        for le in word:
            while i < len(s) and s[i] != le:
                i += 1
            if i == len(s):
                return False
            i += 1
        return True

    def findLongestWord(self, s: str, d: List[str]) -> str:
        """Use heap, same complexity, similar performance.

        O(N + N(logN + x)), 420 ms, 58% ranking.
        """
        heap = [(-len(word), word) for word in d]
        heapq.heapify(heap)
        while heap:
            _, word = heapq.heappop(heap)
            if self.contains(s, word):
                return word
        return ''


class Solution3:
    def contains(self, word, s) -> bool:
        i = 0
        for le in s:
            if i < len(word) and word[i] == le:
                i += 1
        return i == len(word)

    def findLongestWord(self, s: str, d: List[str]) -> str:
        """Better algorithm to find whether a word is in s.
        Everything else is the same as above.

        This is courtesy of the official solution.

        O(NlogN + N * x), 316 ms, 71% ranking
        """
        for word in sorted(d, key=lambda s_: (-len(s_), s_)):
            if self.contains(word, s):
                return word
        return ''


class Solution4:
    def contains(self, word, s) -> bool:
        i = 0
        for le in s:
            if i < len(word) and word[i] == le:
                i += 1
        return i == len(word)

    def findLongestWord(self, s: str, d: List[str]) -> str:
        """No need to sort. Just compare the result.

        O(N * x), 400 ms, 61% ranking.
        """
        res = ''
        for word in d:
            if self.contains(word, s):
                res = word if len(word) > len(res) else word if len(word) == len(res) and word < res else res
        return res


class Solution5:
    def contains(self, word, s) -> bool:
        """This very smart use of iterator is from Mr. Pochmann:
        https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/discuss/99590/Short-Python-solutions

        When we call le in it, the iterator goes from start to end to see
        whether an letter matches le. Afterwards, the iterator remembers its
        state and does not start from the beginning for the next letter to match

        le in it returns false when iterator is exhausted.
        """
        it = iter(s)
        return all(le in it for le in word)

    def findLongestWord(self, s: str, d: List[str]) -> str:
        """No need to sort. Just compare the result.

        O(N * x), 148 ms, 79% ranking. Man, Mr. Pochmann's iterator trick works
        very well.
        """
        res = ''
        for word in d:
            if self.contains(word, s):
                res = word if len(word) > len(res) else word if len(word) == len(res) and word < res else res
        return res


sol = Solution5()
tests = [
    ('abpcplea', ['ale', 'apple', 'monkey', 'plea'], 'apple'),
    ('pabcplea', ['ale', 'apple', 'monkey', 'plea'], 'plea'),
    ('abpcplea', ['a', 'b', 'c'], 'a'),
    ('a', ['ale', 'apple', 'monkey', 'plea'], ''),
    ('bab', ['ba', 'ab', 'a', 'b'], 'ab'),
]

for i, (s, d, ans) in enumerate(tests):
    res = sol.findLongestWord(s, d)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
