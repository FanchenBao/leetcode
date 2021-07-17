# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        """LeetCode 927

        Very happy that our first attempt got accepted, after a few fixes to
        handle the leading 0 issue. The idea is to create a prefix-sum-ish array
        for the first element. And then we start from the end of the array and
        gradually create the third element. For each third element, we check
        whether the same value has appeared in all possible first elements. If
        we can find such first element, we obtain its index, and use prefix sum
        magic to compute the value of the second element directly.

        This technically runs in O(N), but the left shift operation can add up
        as the list size gets big (i.e. we are handling giant numbers).

        1200 ms, 7% ranking.

        UPDATE: add edge case check, courtesy of the official solution. But it
        doesn't change the run time at all.
        """
        n = len(arr)
        # Check for easy edge cases
        sum_arr = sum(arr)
        if sum_arr % 3:
            return [-1, -1]
        if sum_arr == 0:
            return [0, n - 1]

        dict_i = {arr[0]: 0}  # O(1) check for index i given some value
        vals_i = [arr[0]]  # prefix-sum-ish array for all possible first elements
        
        # note that the end condition is one bigger than actually allowed.
        for i in range(1, n - 1):
            cur_val = ((vals_i[-1] << 1) + arr[i])
            vals_i.append(cur_val)
            dict_i[cur_val] = min(dict_i.get(cur_val, math.inf), i)
        val_j = 0
        for j in range(n - 1, 1, -1):
            val_j = ((arr[j] << (n - 1 - j)) + val_j)
            if val_j > vals_i[j - 2]:  # early exit
                break
            i = dict_i.get(val_j, -1)
            if 0 <= i <= n - 3:  # there is a first element equal to the third
                # compute the second element and compare with the third
                mid = vals_i[j - 1] - (vals_i[i] << (j - i - 1))
                if mid == val_j:
                    return [i, j]
        return [-1, -1]


class Solution2:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        """This is the official solution. Very smart.

        Reference: https://leetcode.com/problems/three-equal-parts/solution/

        352 ms.
        """
        # Check for easy edge cases
        sum_arr = sum(arr)
        if sum_arr % 3:
            return [-1, -1]
        if sum_arr == 0:
            return [0, len(arr) - 1]
        each = sum_arr // 3
        acc, indices = 0, []
        for i, val in enumerate(arr):
            if val:
                acc += 1
                if acc == 1:
                    indices.append(i)
                if acc == each:
                    indices.append(i)
                    acc = 0
        i1, j1, i2, j2, i3, j3 = indices
        if arr[i1:j1 + 1] != arr[i2:j2 + 1] or arr[i2:j2 + 1] != arr[i3:j3 + 1]:
            return [-1, -1]
        z1 = i2 - j1 - 1  # number of zeros between j1 and i2
        z2 = i3 - j2 - 1  # number of zeros between j2 and i3
        z3 = len(arr) - j3 - 1  # number of zeros between j3 and the end
        if z1 < z3 or z2 < z3:
            return [-1, -1]
        return [j1 + z3, j2 + z3 + 1]


sol = Solution2()
tests = [
    ([1, 0, 1, 0, 1], [0, 3]),
    ([1, 1, 0, 1, 1], [-1, -1]),
    ([1, 1, 0, 0, 1], [0, 2]),
    ([0, 0, 0, 0, 0], [0, 4]),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.threeEqualParts(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
