#! /usr/bin/env python3
from typing import List, Dict
from collections import defaultdict
from bisect import bisect_right, bisect_left
from random import randint

"""09/04/2019

Solution1:
TLE. The logic is sound for determining whether palindrome can be formed. We
check how many letters have odd number of appearances in the range. If total
number of letters is odd, we are allowed one letter to have odd number of
appearances. For the rest of odd-appearing letters, they must all be turned into
even-appearing to satisfy palindrome. Since each letter change can make two
odd-appearing letters even-appearing, we just need to check whether the number
of odd-appearing letters is even, and if it is even, whether the number of pairs
is smaller or equal to the number of letters allowed to be modified. These
operations are all O(1) in nature, so the only reason for TLE is to retrieve
the number of odd-appearing letters. Here, I construct first a Dict with indices
of all letters. Then I use binary search to get the number of appearances for
each letter in the range. However, the complexity O(52nlog(n)) is not good
enough.

Solution2:
Same basic idea as Solution1, but I optimized the method to compute number of
odd-appearing letters. It still took O(n) to set up the data structure, a list
whose element is another list recording the number of letters seen so far. This
way, we can compute the number of odd-appearing letters in O(1) time, instead
of O(log(n)). This solution passed OJ, clocking at a whopping 2664 ms, not even
on the percentage chart.


UPDATE 09/05/2019

Solution3:
This is exactly the same solution as mine, but with better logic. I got it from
the discussion section here:

https://leetcode.com/problems/can-make-palindrome-from-substring/discuss/371849/JavaPython-3-3-codes-each%3A-prefix-sum-of-counting-characters-first-then-compare

The key improvements in logic is three folds.

First, use sum() to compute the number of odd-appearing letters, since when we
do modulo 2, the odd number gives 1, which can be summed together to get the
total.

Second, there is no need to check for the length of substring being odd or even.
In my method, if the length is odd, we can remove one count from num_odd. But
that removal can also be done by doing interger division by 2. So checking length
is unnecessary. Furthermore, checking whether num_odd is even is also unnecessary,
because if num_odd is odd, then length of substring must be odd, which is good;
if num_odd is even, then length of substring must be even, which is also good.
The benefits of not having to check for num_odd and length of substring is a
massive simplification of the logic, which allows for the last improvement.

Third, use list comprehension to directly return the answer.

These improvements don't speed up the solution. Solution3 still clocked in at
2732 ms, similar to Solution2. But the simplified logic makes the solution much
neater.


Solution4:
This is the real deal. Also from the same discussion post above. The idea is to
not use a list to record the number of letters encountered at each position of
`s`, but use a bitmap. We can use the lowest 26 bits of an integer to represent
whether a letter has occurred odd (1) or even number of times (0). When constructing
the list, we observe that if at the previous position a letter is marked 1, then
the occurrence of the same letter at the current position would make it 0. Thus
we have an XOR relationship. We would first left shift to the proper bitmap
position, then XOR the previous bitmap at this position with 1 to get the current
value at this bitmap position.

To get the odd or even-appearing information for all letters in a substring, we
do XOR between query[1] and query[0]. If a letter appears odd number of times
at query[1] and query[0], then it must occur even number of times in between.
Afterwards, we need to count how many odds (or 1s) we get. We use `bin()`, which
turns an integer, which is the result of XOR, into a str of its binary repr.
Then we only need to count how many 1s are in the str.

This solution is a massive improvement in runtime, clocked in at 1500ms, 48%
"""


class Solution1:
    def canMakePaliQueries(
        self, s: str, queries: List[List[int]]
    ) -> List[bool]:
        res: List[bool] = [False] * len(s)
        letter_pos: Dict[str, List[int]] = defaultdict(list)
        for i, le in enumerate(s):
            letter_pos[le].append(i)
        for i, q in enumerate(queries):
            num_odd: int = 0
            # num of letters having odd number of appearances
            for i in range(97, 123):
                if (
                    bisect_right(letter_pos[chr(i)], q[1])
                    - bisect_left(letter_pos[chr(i)], q[0])
                ) % 2:
                    num_odd += 1
            # if sub has odd length, we are allowed one letter with odd appearances
            if (q[1] - q[0] + 1) % 2:
                num_odd -= 1
            # odd-appearances letters must be in pairs to have a chance of becoming palindrome
            if num_odd % 2 == 0 and num_odd // 2 <= q[2]:
                res[i] = True
        return res


class Solution2:
    def canMakePaliQueries(
        self, s: str, queries: List[List[int]]
    ) -> List[bool]:
        res: List[bool] = [False] * len(queries)
        letter_counts = [[0] * 26]
        for i in range(1, len(s) + 1):
            letter_counts.append(letter_counts[i - 1][:])
            letter_counts[i][ord(s[i - 1]) - 97] += 1
        for i, q in enumerate(queries):
            # num of letters having odd number of appearances
            num_odd: int = 0
            for j in range(26):
                if (letter_counts[q[1] + 1][j] - letter_counts[q[0]][j]) % 2:
                    num_odd += 1
            # if sub has odd length, we are allowed one letter with odd appearances
            if (q[1] - q[0] + 1) % 2:
                num_odd -= 1
            # odd-appearances letters must be in pairs to have a chance of becoming palindrome
            if num_odd % 2 == 0 and num_odd // 2 <= q[2]:
                res[i] = True
        return res


class Solution3:
    def canMakePaliQueries(
        self, s: str, queries: List[List[int]]
    ) -> List[bool]:
        letter_counts = [[0] * 26]
        for i, c in enumerate(s):
            letter_counts.append(letter_counts[i][:])
            letter_counts[i + 1][ord(c) - 97] += 1
        return [
            sum(
                (letter_counts[q[1] + 1][j] - letter_counts[q[0]][j]) % 2
                for j in range(26)
            )
            // 2
            <= q[2]
            for q in queries
        ]


class Solution4:
    def canMakePaliQueries(
        self, s: str, queries: List[List[int]]
    ) -> List[bool]:
        odd_even: List[int] = [0]
        for i, c in enumerate(s):
            odd_even.append(odd_even[i] ^ (1 << ord(c) - 97))
        return [
            bin(odd_even[q[1] + 1] ^ odd_even[q[0]]).count("1") // 2 <= q[2]
            for q in queries
        ]


sol = Solution4()
L = 10 ** 5
s = "".join(chr(randint(97, 122)) for _ in range(L))
queries = []
for _ in range(L):
    f = randint(0, L - 1)
    b = randint(f, L - 1)
    queries.append([f, b, randint(0, 10)])
# print(f'"{s}"')
# print(queries)
sol.canMakePaliQueries(s, queries)
