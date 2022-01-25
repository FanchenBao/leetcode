# from pudb import set_trace; set_trace()
from typing import List
from itertools import groupby


class Solution1:
    def validMountainArray(self, arr: List[int]) -> bool:
        """LeetCode 941

        This is a naive analysis, which feels very convoluted. I don't like it.

        O(N), 249 ms, 37% ranking.
        """
        if len(arr) < 3:
            return False
        up_cnt = down_cnt = 0
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                return False
            if arr[i] > arr[i - 1]:
                up_cnt += 1
                if down_cnt > 0:
                    return False
            else:
                down_cnt += 1
                if up_cnt == 0:
                    return False
        return up_cnt * down_cnt != 0


class Solution2:
    def validMountainArray(self, arr: List[int]) -> bool:
        """Use itertools.groupby, but it is slower.
        """
        groups = [k for k, g in groupby(-1 if l < r else 0 if l == r else 1 for l, r in zip(arr, arr[1:]))]
        return len(groups) == 2 and groups[0] == -1 and groups[1] == 1


class Solution3:
    def validMountainArray(self, arr: List[int]) -> bool:
        """Two pointer method from Lee215
        """
        i, j = 0, len(arr) - 1
        while i < len(arr) - 1 and arr[i] < arr[i + 1]:
            i += 1
        while j > 0 and arr[j - 1] > arr[j]:
            j -= 1
        return 0 < i == j < len(arr) - 1


sol = Solution3()
tests = [
    ([2, 1], False),
    ([3, 5, 5], False),
    ([0, 3, 2, 1], True),
    ([0,1,2,3,4,5,6,7,8,9], False),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.validMountainArray(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
