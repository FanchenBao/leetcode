# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        """LeetCode 609

        The only tricky part is the return value, which has to exclude all the
        files that do not have duplicates.

        175 ms, faster than 35.76%
        """
        dups = defaultdict(list)
        for p in paths:
            plst = p.split()
            for i in range(1, len(plst)):
                fn, cnt = plst[i].split('(')
                dups[cnt[:-1]].append(plst[0] + '/' + fn)
        return [val for val in dups.values() if len(val) > 1]


sol = Solution()
tests = [
    (["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"], [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]),
    (["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"], [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]),
    (["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"], []),
]

for i, (paths, ans) in enumerate(tests):
    res = sol.findDuplicate(paths)
    ans.sort()
    res.sort()
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
