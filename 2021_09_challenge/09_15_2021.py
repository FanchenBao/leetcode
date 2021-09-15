# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """LeetCode 978

        Very typical DP problem. We keep the count of the longest turbulent
        subarray ending at each val in arr. Then for the next value, we check
        if it can continue the turbulent subarray ending the its previous value.
        If it can, we extend the count. Otherwise, we restart with a turbulent
        array of size two if the current and the previous values are not the
        same. If the current and the previous values are the same, the size of
        the turbulent array is one.

        Note that we use XOR to simplify the logic of checking whether the
        current value can extend the turbulent array of the preivous value.

        O(N), 520 ms, 45% ranking.
        """
        res, pre = 1, 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                pre = 1
            else:
                pre = pre + 1 if i > 1 and not (arr[i] < arr[i - 1]) ^ (arr[i - 1] > arr[i - 2]) else 2
                res = max(res, pre)
        return res


class Solution2:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """Sliding window method from the official solution.

        The idea is that we keep two pointers. The lo pointer points to the
        start of a potential subarray, and the other pointer keeps moving on the
        array until we hit a stopping point. The stopping point is defined as
        a case where the turbulent subarray cannot continue. When this happens,
        we aggregate the current result.

        This solution runs for 472 ms. It is faster than Solution1 because it
        checks max() much less often.
        """
        res, lo, N = 1, 0, len(arr)
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                res = max(res, i - lo)
                lo = i
            elif i > 1 and ((arr[i] < arr[i - 1]) ^ (arr[i - 1] > arr[i - 2])):
                res = max(res, i - lo)
                lo = i - 1
        return max(res, N - lo)


sol = Solution2()
tests = [
    ([9, 4, 2, 10, 7, 8, 8, 1, 9], 5),
    ([4, 8, 12, 16], 2),
    ([100], 1),
    ([0, 1, 1, 0, 1, 0, 1, 1, 0, 0], 5),
    ([0, 8, 45, 88, 48, 68, 28, 55, 17, 24], 8),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.maxTurbulenceSize(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
