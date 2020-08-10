#! /usr/bin/env python3
from typing import List, Dict, Tuple

# from random import randint
from collections import defaultdict, Counter
from itertools import groupby

"""08/20/2019

Solution1:

O(n) complexity. While I used 'dp' in the solution, it is not actually dp. I
use a dictionary to track the ranges of each letter. Starting from the first
letter, each addition of a new letter, we update the ranges for that letter.
The impact this new letter can have on the text can be expressed in two ways.
One is that some letter from the previous stretches add to the new stretch. The
other is the new letter adding to the stretch right in front of itself. The
first way is easy to understand. The second way requires some analysis. The
reason that we only need to add the new letter to the stretch right in front of
it (in the code below, we denote it dp[t][-2]), instead of checking all
previous stretches, is that all stretches ahead of dp[t][-2] have already been
checked by dp[t][-2] itself. So there is no need to do the same checks again
with the new letter.

During the check, there are two scenarios. Either the target stretch and the
stretch ahead of it are separated by only one letter, in which case we can
merge the two stretches, or more than one letter, in which case we just add one
to the current length of the target stretch.

This solution clocked in at 120 ms, 22%


Solution2:
Much cleaner solution from
https://leetcode.com/problems/swap-for-longest-repeated-character-substring/discuss/355852/Python-Groupby
The use of `groupby` to compute the ranges of each letter is a brilliant move.
Furthermore, checking with the total number of each letter when adding one to
an existing range or merging ranges is another brilliant solution to prevent
adding non-existent letter to the solution.

This solution clocked in at 80 ms, 53%
"""


class Solution1:
    def maxRepOpt1(self, text: str) -> int:
        dp: Dict[str, List[List[int]]] = defaultdict(list)
        res = 1
        for i, t in enumerate(text):
            if t not in dp:
                dp[t].append([i, i])
            else:
                # update last stretch
                if dp[t][-1][1] == i - 1:
                    dp[t][-1][1] = i
                else:
                    dp[t].append([i, i])
                # analyze new_len after addition of new letter
                if len(dp[t]) == 1:  # only one stretch
                    new_len = dp[t][-1][1] - dp[t][-1][0] + 1
                elif len(dp[t]) == 2:  # two stretches
                    if (
                        dp[t][-1][0] - dp[t][-2][1] > 2
                    ):  # the last two stretches separated by more than one letter
                        new_len = (
                            max(
                                dp[t][-1][1] - dp[t][-1][0],
                                dp[t][-2][1] - dp[t][-2][0],
                            )
                            + 1
                            + 1
                        )
                    else:  # last two stretches separated by exactly one letter
                        new_len = (
                            dp[t][-2][1]
                            - dp[t][-2][0]
                            + 1
                            + dp[t][-1][1]
                            - dp[t][-1][0]
                            + 1
                        )
                else:  # at least three stretches
                    # Some letter from previous stretches add to the new stretch
                    new_stretch_len = 0
                    if (
                        dp[t][-1][0] - dp[t][-2][1] == 2
                    ):  # the last two stretches separated by only one letter
                        new_stretch_len = (
                            dp[t][-2][1]
                            - dp[t][-2][0]
                            + 1
                            + dp[t][-1][1]
                            - dp[t][-1][0]
                            + 1
                            + 1
                        )
                    else:
                        new_stretch_len = dp[t][-1][1] - dp[t][-1][0] + 1 + 1
                    # New letter add to previous stretches
                    pre_stretch_len = 0
                    if dp[t][-2][0] - dp[t][-3][1] == 2:
                        pre_stretch_len = (
                            dp[t][-3][1]
                            - dp[t][-3][0]
                            + 1
                            + dp[t][-2][1]
                            - dp[t][-2][0]
                            + 1
                            + 1
                        )
                    else:
                        pre_stretch_len = dp[t][-2][1] - dp[t][-2][0] + 1 + 1
                    new_len = max(new_stretch_len, pre_stretch_len)
                res = max(res, new_len)
        return res


class Solution2:
    def maxRepOpt1(self, text: str) -> int:
        count: Dict[str, int] = Counter(text)
        stretches: List[Tuple[str, int]] = [
            (k, len(list(g))) for k, g in groupby(text)
        ]
        res: int = 1
        # Each stretch add one
        for k, length in stretches:
            res = max(res, min(length + 1, count[k]))
        # Merge two stretches together
        for i in range(1, len(stretches) - 1):
            # same letter and stretches separated by one letter
            if (
                stretches[i - 1][0] == stretches[i + 1][0]
                and stretches[i][1] == 1
            ):
                res = max(
                    res,
                    min(
                        stretches[i - 1][1] + stretches[i + 1][1] + 1,
                        count[stretches[i - 1][0]],
                    ),
                )
        return res


def individual_test():
    sol = Solution1()
    text = "babbaaabbbbbaa"
    print(sol.maxRepOpt1(text))


def test():
    sol = Solution2()
    # test case 1
    text = "ababa"
    if sol.maxRepOpt1(text) != 3:
        print(f"Test case 1: FAIL. Wrong answer {sol.maxRepOpt1(text)}")
    else:
        print("Test case 1: PASS")

    # test case 2
    text = "aaabaaa"
    if sol.maxRepOpt1(text) != 6:
        print(f"Test case 2: FAIL. Wrong answer {sol.maxRepOpt1(text)}")
    else:
        print("Test case 2: PASS")

    # test case 3
    text = "aaabbaaa"
    if sol.maxRepOpt1(text) != 4:
        print(f"Test case 3: FAIL. Wrong answer {sol.maxRepOpt1(text)}")
    else:
        print("Test case 3: PASS")

    # test case 4
    text = "aaaaa"
    if sol.maxRepOpt1(text) != 5:
        print(f"Test case 4: FAIL. Wrong answer {sol.maxRepOpt1(text)}")
    else:
        print("Test case 4: PASS")

    # test case 5
    text = "abcdef"
    if sol.maxRepOpt1(text) != 1:
        print(f"Test case 5: FAIL. Wrong answer {sol.maxRepOpt1(text)}")
    else:
        print("Test case 5: PASS")

    # test case 6
    text = "bbababaaaa"
    if sol.maxRepOpt1(text) != 6:
        print(f"Test case 6: FAIL. Wrong answer {sol.maxRepOpt1(text)}")
    else:
        print("Test case 6: PASS")

    # test case 7
    text = "baaabaaaaaaabaab"
    if sol.maxRepOpt1(text) != 11:
        print(f"Test case 7: FAIL. Wrong answer {sol.maxRepOpt1(text)}")
    else:
        print("Test case 7: PASS")

    # test case 8
    text = "babbaaabbbbbaa"
    if sol.maxRepOpt1(text) != 6:
        print(f"Test case 8: FAIL. Wrong answer {sol.maxRepOpt1(text)}")
    else:
        print("Test case 8: PASS")


test()
# individual_test()
