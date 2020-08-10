#! /usr/bin/env python3
from typing import List
from random import randint

"""08/25/2019

Solution1:
I am very proud of this solution, because it is simple, short, and fast. Granted,
I did test run my solution against the OJ with some given test cases, but still
this is the very first complex DP solution I have written all by myself.

DP should be a very obvious choice for problems like this. However, I initially
wanted to analyze the string directly, which led to nowhere. A few obvious
observation:

1. the last substr must begin with the largest letter in the whole string
2. the last substr must continue to the end of the original string, because the
longer a string, the later it is ranked lexicologically.

This means, we will only need to record the position of the starting letter. The
DP idea is that if we have found the last substr of s[:i], how would such substr
change with an additional s[i+1]. Obviously, if s[i+1] is larger than the start
of the last substr of s[:i], we update the last substr of s[:i+1] to i+1. If
s[i+1] is the same as the start of the last substr of s[:i], and that s[i+1] is
not the same as s[i] (this is important, because a string of the same letters
can be treated as one letter represented by its first occurrence), we open up
a new possibility. This means we need an array to record multiple positions of
big letter, and our final result shall come from one of them.

The most complicated situation is when s[i+1] is smaller than the start of the
last substr of s[:i] or s[i+1] is part of a string of the same letter. If
currently we only have one candidate, we can ignore the new letter. But if we
already have more than one candidates, we need to compare s[i+1] to the
correspondingly positioned letter relative to all the candidates. For example,
suppose we have s[:i] = "zabza" and s[i+1] = 'c'. Our candidates = [0, 3]. Since
'c' is smaller than 'z', and we have two elements in candidates. We must compare
'c' to s[5 - 3 + 0] = s[2] = 'b'. Since 'c' > 'b', we know the last candidate
is bigger; we then update candidates to contain only the last elment. On the
other hand, if s[i+1] = 'a', since 'a' < 'b', we elimiate the last element. If
s[i+1] = 'b', we do nothing, because currently the two candidates lead the same
strings, and we need the next letter to decide.

The neat thing about this candidates array is that any position recorded in it
MUST lead the same exact string. This is because any difference would lead to
one candidate being kicked off. Therefore, when we do comparison with the newly
added letter, we only need to compare with letters led by candidates[0].

Another neat thing is that when the string is processed, our answer must come
from candidates[0] as it contains the longest string, even if there are other
candidates leading the same letters.

This solution has O(n) complexity, clocking in at 288ms, 74%
"""


class Solution:
    def lastSubstring(self, s: str) -> str:
        candidates: List[int] = [0]
        for i, le in enumerate(s[1:], start=1):
            if le > s[candidates[0]]:
                candidates = [i]
            # only start new if le is not following itself
            elif le == s[candidates[0]] and le != s[i - 1]:
                candidates.append(i)
            else:
                if len(candidates) > 1:
                    # new le bigger, keep the last candidate
                    if le > s[candidates[0] + i - candidates[-1]]:
                        candidates = candidates[-1:]
                    # new le smaller, pop the last candidate
                    elif le < s[candidates[0] + i - candidates[-1]]:
                        candidates.pop()
        return s[candidates[0] :]


sol = Solution()
s = "babb"
# print(sol.lastSubstring(s))


def gen_string(length: int):
    return "".join([chr(randint(97, 122)) for _ in range(length)])


print(gen_string(400000))
