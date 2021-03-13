# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """The first intuition is to list all possible combinations of binary
        codes. But this immediately is not working because there are simply way
        too many of them. Therefore, we think about it in a different way, which
        means we create all possible substrings of length k from s, and then
        check how many unique substrings are there. If the number of unique
        substring of length k equals 2^k, then we know all of the binary codes
        are included in s. And we are done. This runs in O(kN) where N is the
        length of s.

        O(kN), 296 ms, 85% ranking.
        """
        return len({s[i:i + k] for i in range(len(s) - k + 1)}) == 2**k


class Solution2:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """This is the rolling hash solution from the official solution. Very
        smart. The gotcha is the precedence of the left shift operator. Make
        sure that it is wrapped in parenthesis when another operator is nearby.
        """
        hashmap = [0] * (1 << k)
        all_ones = (1 << k) - 1
        key = int(s[:k], 2)
        hashmap[key] = 1
        for i in range(k, len(s)):
            key = (key << 1) & all_ones | int(s[i])
            hashmap[key] = 1
        return sum(hashmap) == (1 << k)


sol = Solution2()
tests = [
    ('00110110', 2, True),
    ('00110', 2, True),
    ('0110', 1, True),
    ('0110', 2, False),
    ('0000000001011100', 4, False),
    ('00000000001011100', 3, True),
]

for i, (s, k, ans) in enumerate(tests):
    res = sol.hasAllCodes(s, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
