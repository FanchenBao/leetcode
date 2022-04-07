# from pudb import set_trace; set_trace()
from typing import List
from itertools import accumulate


class Solution:
    def sumScores(self, s: str) -> int:
        """This problem is essentially the same as finding the Z array of s
        using the Z algorithm.

        So basically, if you know about Z algorithm, this problem is not hard.
        But if you don't know, it is very challenging to figure out the Z algo.

        In Z algo, we have indices l, r that marks a window which contains the
        longest substring that is also part of the prefix at the moment. i is
        the index of the letter currently under consideration. If i is outside
        the window, then we have to reconstruct the window. Here is something
        ingenious: we can use s[r - l] to locate the letter in the prefix. In
        other words, we only need to increment r and we can make direct
        comparison between s[r] and its corresponding value in the prefix.

        If i is inside the window, we need to find the prefix position that
        corresponds to i in the current window. We call it k and k = i - l.
        From k, we can obtain z[k], which is the longest length substring
        prefix that starts from k. If z[k] is smaller than the remaining length
        of the window (i.e. r - i + 1), then from i, we at most can have a
        substring prefix the same length as z[k]. Otherwise, if z[k] >=
        r - i + 1, that means there is possibility of extending the substring
        prefix starting from i beyond r. In this case, we set l = i and r += 1,
        and search again,

        O(N), because each time we search, it's always beyond the current r.
        This means each position in s at most is visited twice, once by the
        search and the other by i.

        532 ms, 88% ranking.
        """
        N = len(s)
        z = [0] * N
        l, r = 0, 0
        for i in range(1, N):
            if i > r:
                l, r = i, i
                while r < N and s[r] == s[r - l]:  # use r - l to refer back to prefix
                    r += 1
                z[i] = r - l
                r -= 1
            else:
                k = i - l  # index in the prefix that corresponds to i
                if z[k] < r - i + 1:
                    z[i] = z[k]
                else:
                    l, r = i, r + 1
                    while r < N and s[r] == s[r - l]:
                        r += 1
                    z[i] = r - l
                    r -= 1
        return sum(z) + N


sol = Solution()
tests = [
    ('babab', 9),
    ('azbazbzaz', 14),
]

for i, (s, ans) in enumerate(tests):
    res = sol.sumScores(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
