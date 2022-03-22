# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """LeetCode 763

        We first find the last index of each letter. Then we create a window
        that covers the first and last appearance of s[0]. We then iterate
        through each letter. If a letter's last index is larger than the current
        window, the window's end is expanded. This stops when the current index
        is larger than the window. That means all the letters within the window
        only appear in the window. Thus, the size of the window can be pushed
        to tbe result list.

        O(N), 39 ms, 92% ranking.
        """
        hashmap = {le: i for i, le in enumerate(s)}
        res = []
        start, end = 0, hashmap[s[0]]
        for i in range(1, len(s)):
            if i > end:
                res.append(end - start + 1)
                start, end = i, hashmap[s[i]]
            else:
                end = max(end, hashmap[s[i]])
        res.append(end - start + 1)
        return res


sol = Solution()
tests = [
    ('ababcbacadefegdehijhklij', [9, 7, 8]),
    ('eccbbbbdec', [10]),
    ('a', [1]),
    ('aaa', [3]),
    ('aaab', [3, 1]),
    ('baaa', [1, 3]),
]

for i, (s, ans) in enumerate(tests):
    res = sol.partitionLabels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
