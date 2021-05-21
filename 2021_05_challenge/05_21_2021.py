# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def is_match(self, word: str, pattern: str) -> bool:
        mapping = {}
        letters = {chr(i) for i in range(97, 123)}
        for w, p in zip(word, pattern):
            if p not in mapping:
                if w in letters:  # p not seen and w not mapped
                    mapping[p] = w
                    letters.remove(w)
                else:  # p not seen but w already mapped. Failing surjection
                    return False
            elif w != mapping[p]:  # p seen but not mapped to w. Failing injection
                return False
        return True

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """LeetCode 890

        Brute force solution, because the size of each word is small (50) and
        the length of words is also small (20). We check each word with the
        pattern letter by letter. We use a dict to serve as mapping between each
        letter in the pattern and the letter in the word. This mapping allows
        us to check for injection.

        Meanwhile, we also set up a set of lower case English letters. Each time
        a letter from the word is mapped, we remove the letter from the set.
        This is to check for surjection.

        Once both check passes for all the letters in word and pattern, we have
        a match. Any failed check results in a non-match.

        O(NM) where N is the length of words and M the length of each word.
        24 ms, 97% ranking.
        """
        return [w for w in words if self.is_match(w, pattern)]


class Solution2:
    def is_match(self, word: str, pattern: str) -> bool:
        if len(set(word)) == len(set(pattern)):
            mapping = {}
            for w, p in zip(word, pattern):
                if p not in mapping:
                    mapping[p] = w
                elif mapping[p] != w:
                    return False
            return True
        return False

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """32 ms"""
        return [w for w in words if self.is_match(w, pattern)]


class Solution3:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """This is a solution by lee215. He is able to acquire the true pattern
        from pattern, using the order of the first occurrence of each letter
        in the pattern.

        Ref: https://leetcode.com/problems/find-and-replace-pattern/discuss/161288/C%2B%2BJavaPython-Normalise-Word
        """

        def get_pattern(word: str) -> List[int]:
            mapping = {}
            return [mapping.setdefault(w, len(mapping)) for w in word]

        pp = get_pattern(pattern)
        return [w for w in words if get_pattern(w) == pp]


sol = Solution3()
tests = [
    (['abc', 'deq', 'mee', 'aqq', 'dkd', 'ccc'], 'abb', ['mee', 'aqq']),
    (['a', 'b', 'c', 'd'], 'a', ['a', 'b', 'c', 'd']),
]

for i, (words, pattern, ans) in enumerate(tests):
    res = sol.findAndReplacePattern(words, pattern)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
