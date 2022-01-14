# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def capitalizeTitle(self, title: str) -> str:
        """Python's title() function does not distinguish words of different
        length. Thus if we use title(), we will have to check each word and
        turn those with length smaller or equal to 2 to lower case.

        Without using title(), we iterate through each word and either
        capitalize or lower case the word.

        28 ms, 95% ranking.
        """
        return ' '.join(w.capitalize() if len(w) > 2 else w.lower() for w in title.split())


class Solution2:
    def capitalizeTitle(self, title: str) -> str:
        """Use title() function
        """
        return ' '.join(w if len(w) > 2 else w.lower() for w in title.title().split())


sol = Solution2()
tests = [
    ("capiTalIze tHe titLe", "Capitalize The Title"),
    ("First leTTeR of EACH Word", "First Letter of Each Word"),
    ("i lOve leetcode", "i Love Leetcode"),
]

for i, (title, ans) in enumerate(tests):
    res = sol.capitalizeTitle(title)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
