# from pudb import set_trace; set_trace()
from typing import List
import math
import string


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """LeetCode 953

        Convert each word to regular alphabet with letter corresponding to the
        order.

        O(MN + NlogN), where M is the average length of each word and N is the
        length of words. 46 ms, faster than 39.14%
        """
        m = {x: y for x, y in zip(order, string.ascii_lowercase)}
        converted = [''.join(m[le] for le in word) for word in words]
        return converted == sorted(converted)


sol = Solution()
tests = [
    (["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
    (["word","world","row"], "worldabcefghijkmnpqstuvxyz", False),
    (["apple","app"], "abcdefghijklmnopqrstuvwxyz", False),
]

for i, (words, order, ans) in enumerate(tests):
    res = sol.isAlienSorted(words, order)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
