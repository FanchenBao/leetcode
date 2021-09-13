# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def maxNumberOfBalloons(self, text: str) -> int:
        """LeetCode 1189

        Create a counter of text, and iterate through the letters in balloon
        and keep track of the min count of each letter. Note that for letter l
        and o, the count from counter must be divided by two.

        O(N) time complexity, where N is the length of text. 32 ms, 78% ranking. 
        """
        counter = Counter(text)
        res = len(text)
        for le in 'balon':
            if le in 'lo':
                res = min(res, counter[le] // 2)
            else:
                res = min(res, counter[le])
        return res


class Solution2:
    def maxNumberOfBalloons(self, text: str) -> int:
        """Make it generic.
        
        The generic function runs in O(M + N), where M, N are the length of text
        and pattern, respectively.
        """

        def generic(text: str, pattern: str) -> int:
            txt_c, pat_c = Counter(text), Counter(pattern)
            return min(txt_c[le] // c for le, c in pat_c.items())

        return generic(text, 'balloon')


sol = Solution2()
tests = [
    ('nlaebolko', 1),
    ('loonbalxballpoon', 2),
    ('leetcode', 0)
]

for i, (text, ans) in enumerate(tests):
    res = sol.maxNumberOfBalloons(text)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
