# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def validMountainArray(self, arr: List[int]) -> bool:
        """Straightforward solution, check increasing then decreasing. There are
        a few edge cases to consider, but overall not too hard.

        O(N), 212 ms, 20% ranking
        """
        if len(arr) < 3:
            return False
        # strictly increasing
        i = 1
        while i < len(arr):
            if arr[i] == arr[i - 1]:
                return False
            elif arr[i] < arr[i - 1]:
                break
            i += 1
        if i == 1 or i == len(arr):  # no increasing portion or no decreasing portion
            return False
        # strictly decreasing
        while i < len(arr):
            if arr[i] >= arr[i - 1]:
                return False
            i += 1
        return True


class Solution2:
    def validMountainArray(self, arr: List[int]) -> bool:
        """Mr. Lee comes to rescue. A very smart solution. Start with two
        pointers on both ends of the array and climb together. If the arr is a
        mountain array, the two pointers must meet at the end.

        O(N), 200 ms, 57% ranking.
        """
        i, j = 0, len(arr) - 1
        while i < len(arr) - 2 and arr[i] < arr[i + 1]:  # walk i
            i += 1
        while j > 0 and arr[j - 1] > arr[j]:  # walk j
            j -= 1
        return 0 < i == j < len(arr)


sol = Solution2()
tests = [
    ([2, 1], False),
    ([3, 5, 5], False),
    ([0, 3, 2, 1], True),
    ([1, 2, 3, 4, 5], False),
    ([5, 4, 3, 2, 1], False),
    ([4, 3, 2, 1, 4, 5], False),
    ([1, 3, 2, 4, 3, 5, 4, 6], False),
    ([1, 5, 4, 3, 2], True),
    ([1, 2, 3, 4, 5, 0], True),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.validMountainArray(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
