# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        """LeetCode 1239

        Not difficult, because the constraint on the size of arr is very small,
        only 16. This means we can brute force it by going through all 2^16
        different combinations. The difficulty is that the input could be
        unsanitized, i.e. input string has duplicates themselves. Thus, we must
        clean that before going through the DFS part.

        O(2^N), 189 ms, faster than 64.77%
        """
        self.res = 0
        arr_sets = []
        for w in arr:
            w_set = set(w)
            if len(w_set) == len(w):
                arr_sets.append(w_set)
        
        def dfs(idx: int, s_set: str) -> None:
            if idx == len(arr_sets) or self.res == 26:
                return
            new_s_set = s_set.union(arr_sets[idx])
            if len(new_s_set) == len(s_set) + len(arr_sets[idx]):
                if len(new_s_set) > self.res:
                    self.res = len(new_s_set)
                dfs(idx + 1, new_s_set)
            dfs(idx + 1, s_set)

        dfs(0, set())
        return self.res


sol = Solution()
tests = [
    (["un","iq","ue"], 4),
    (["cha","r","act","ers"], 6),
    (["abcdefghijklmnopqrstuvwxyz"], 26),
    (["aa","bb"], 0),
    (["zog","nvwsuikgndmfexxgjtkb","nxko"], 4),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.maxLength(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
