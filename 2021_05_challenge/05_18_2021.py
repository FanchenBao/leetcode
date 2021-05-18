# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
import re


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        """LeetCode 609

        Since the content size is quite limited (not longer than 3000), we
        can directly use the content as a key for a content-file mapping. We
        loop through all the files in the paths, and place each file directory
        into a list corresponding to the content. This allows us to group all
        the files that have the same content together.

        The one tricky is in the return. We only return the files that are
        duplicates.

        If we ignore the runtime on regex, we have O(NM), where N is the size
        of paths and M is the number of files within each path.

        104 ms, 26% ranking.
        """
        content_map = defaultdict(list)
        for path in paths:
            plst = path.split(' ')
            for file_content in plst[1:]:
                m = re.match(r'(.+)\((.*)\)', file_content)
                if m:
                    content_map[m.group(2)].append(plst[0] + '/' + m.group(1))
        return [v for v in content_map.values() if len(v) > 1]


sol = Solution()
tests = [
    (['root/a 1.txt(abcd) 2.txt(efgh)', 'root/c 3.txt(abcd)', 'root/c/d 4.txt(efgh)', 'root 4.txt(efgh)'], [['root/a/2.txt', 'root/c/d/4.txt', 'root/4.txt'], ['root/a/1.txt', 'root/c/3.txt']]),
    (['root/a 1.txt(abcd) 2.txt(efgh)', 'root/c 3.txt(abcd)', 'root/c/d 4.txt(efgh)'], [['root/a/2.txt', 'root/c/d/4.txt'], ['root/a/1.txt', 'root/c/3.txt']]),
]

for i, (paths, ans) in enumerate(tests):
    res = sol.findDuplicate(paths)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
