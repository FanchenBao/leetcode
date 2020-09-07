# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution1:
    def wordPattern(self, pattern: str, str: str) -> bool:
        """Pass OJ, runtime 28 ms"""
        str_lst = str.split(' ')
        if len(pattern) != len(str_lst):
            return False
        pattern_pos = defaultdict(list)
        word_pattern = defaultdict(set)
        for i, pat in enumerate(pattern):
            # different words matching the same pattern
            if pat in pattern_pos and str_lst[i] != str_lst[pattern_pos[pat][-1]]:
                return False
            # same word matching different patterns
            if str_lst[i] in word_pattern and pat not in word_pattern[str_lst[i]]:
                return False
            pattern_pos[pat].append(i)
            word_pattern[str_lst[i]].add(pat)
        return True


class Solution2:
    def wordPattern(self, pattern: str, str: str) -> bool:
        """Simpler solution.

        Same runtime as Solution1, but much simpler code.
        """
        str_lst = str.split(' ')
        if len(pattern) != len(str_lst):
            return False
        return [pattern.index(p) for p in pattern] == [str_lst.index(s) for s in str_lst]



sol = Solution2()
tests = [
    ('abba', 'dog cat cat dog', True),
    ('abba', 'dog cat cat fish', False),
    ('aaaa', 'dog cat cat dog', False),
    ('abba', 'dog dog dog dog', False),
    ('aaaa', 'dog dog dog dog', True),
    ('abbc', 'dog cat cat fish', True),
    ('aaaaaa', 'dog dog dog dog', False),
]

for i, (pattern, str, ans) in enumerate(tests):
    res = sol.wordPattern(pattern, str)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
