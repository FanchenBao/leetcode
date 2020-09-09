# from pudb import set_trace; set_trace()
from typing import List
from itertools import zip_longest


class Solution1:
    def compareVersion(self, version1: str, version2: str) -> int:
        """Could've used zip_longest to solve this more efficiently"""
        v1_lst: List[int] = [int(v) for v in version1.split('.')]
        v2_lst: List[int] = [int(v) for v in version2.split('.')]
        if len(v1_lst) > len(v2_lst):
            v2_lst += [0] * (len(v1_lst) - len(v2_lst))
        else:
            v1_lst += [0] * (len(v2_lst) - len(v1_lst))
        return 1 if v1_lst > v2_lst else -1 if v1_lst < v2_lst else 0


class Solution2:
    def compareVersion(self, version1: str, version2: str) -> int:
        """I am using zip_longest"""
        v1_lst: List[int] = [int(v) for v in version1.split('.')]
        v2_lst: List[int] = [int(v) for v in version2.split('.')]
        for v1, v2 in zip_longest(v1_lst, v2_lst, fillvalue=0):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0


sol = Solution2()
tests = [
    ('0.1', '1.1', -1),
    ('1.0.1', '1', 1),
    ('7.5.2.4', '7.5.3', -1),
    ('1.01', '1.001', 0),
    ('1.0', '1.0.0', 0),
]

for i, (version1, version2, ans) in enumerate(tests):
    res = sol.compareVersion(version1, version2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
