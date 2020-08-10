#! /usr/bin/env python3
from typing import List, Tuple, Set, Dict
from random import randint
from functools import reduce
from collections import Counter

"""09/05/2019

Solution1:
Most naive solution. TLE as expected.

Solution2:
Although this solution also TLE, I am very proud of it nonetheless. Because I
used bitmap to check whether a word is in a puzzle. And I used the function
`reduce`; and I used a lot of list comprehension. However, the culprit for TLE
here is the nested loop. With 10^5 number of words and 10^4 number of puzzles,
it is simply impossible to make a O(MN) solution pass OJ. I was stuck there; I
couldn't figure out a way to avoid O(MN complexity.

UPDATE 09/06/2019
Solution3:
I had to read the discussion to realize that instead of doing nested loops with
both puzzles and words, I can do combinations with the puzzle itself, and match
each combination to the words. Since the puzzle only has 7 letters, and the
first letter has to be there, there are only 2^6 possibilities for each puzzle,
much much less than the 10^5 number of words to check. Here, it is important to
note that the type of combination is nC0 + nC1 + nC2 + ... + nCn (e.g. 'abcd'
is expanded to 'a', 'ab', 'ac', 'abc', 'ad', 'abd', 'acd', 'abcd').

Using the same bitmap technique, and this vastly optimized (O(64N) vs. O(MN))
logic, solution3 passed OJ easily, clocking in at 712 ms, 83%
"""


class Solution1:
    def findNumOfValidWords(
        self, words: List[str], puzzles: List[str]
    ) -> List[int]:
        res: List[int] = []
        for puzzle in puzzles:
            first: str = puzzle[0]
            p_set: Set[str] = set(puzzle)
            count: int = 0
            for word in words:
                contains_first_letter: bool = False
                all_word_in_puzzle: bool = True
                for c in word:
                    if c == first:
                        contains_first_letter = True
                    if c not in p_set:
                        all_word_in_puzzle = False
                        break
                if contains_first_letter and all_word_in_puzzle:
                    count += 1
            res.append(count)
        return res


class Solution2:
    def findNumOfValidWords(
        self, words: List[str], puzzles: List[str]
    ) -> List[int]:
        pb: List[Tuple[int, int]] = [
            (
                reduce(lambda x, y: x | y, (1 << ord(c) - 97 for c in s)),
                ord(s[0]) - 97,
            )
            for s in puzzles
        ]
        wb: List[int] = [
            reduce(lambda x, y: x | y, (1 << ord(c) - 97 for c in s))
            for s in words
        ]
        return [
            sum(1 if (1 << f & w and w | p == p) else 0 for w in wb)
            for p, f in pb
        ]


class Solution3:
    def findNumOfValidWords(
        self, words: List[str], puzzles: List[str]
    ) -> List[int]:
        wb: List[int] = [
            reduce(lambda x, y: x | y, (1 << ord(c) - 97 for c in s))
            for s in words
        ]
        count: Dict[int, int] = Counter(wb)
        res: List[int] = []
        for p in puzzles:
            # get combinations of all lengths for p, including first letter
            comb: List[int] = [1 << ord(p[0]) - 97]
            for c in p[1:]:
                comb += [co | 1 << ord(c) - 97 for co in comb]
            res.append(sum(count[co] for co in comb))
        return res


sol = Solution3()
words_length = 10 ** 5
puzzles_length = 10 ** 4
words = [
    "".join(chr(randint(97, 122)) for _ in range(randint(4, 4)))
    for _ in range(words_length)
]
puzzles = []
for _ in range(puzzles_length):
    p: Set[str] = set()
    while len(p) < 7:
        p.add(chr(randint(97, 122)))
    puzzles.append("".join(p))
# print(words)
# print(puzzles)
print(sol.findNumOfValidWords(words, puzzles))
