#! /usr/bin/env python3
from typing import List, Set

# from collections import deque
from random import randint
from time import time

"""09/19/2019

Solution1:
Most naive solution. It definitely works, but it will cause either memory error
or TLE, because there is basically no optimization involved in this solution.
I am leaving it here for reference and testing purpose.


Solution2:
Improving upon Solution1, now it has a check for repeated subarray sum. If a
repeated subarray sum is found for a certain pos in arr, we can terminate the
computation early. This solution passed more test cases than Solution1, but it
still timed out.


Solution3:
Further improvement upon Solution2. Note that we can end computation as long as
a certain pos in arr equal to what it has got previously. There is no need to
record any other subarray sum because unless repeats happen, the subarray sum
is going to increase regardless. This solution is faster than Solution2, but
that is only because we no longer use Set() operations. So, it still times out.


Solution4:
Finally got it! Solution4, completely different mind set compared to previous
solutions. Previously, I tried to catch repetition and use that to end computation.
Solution4, on the other hand, goes back to the traditional solution for finding
max subarray: divide and conquer. The only two tricks are:

1. Instead of dividing arr, we consider arr as a whole and divide the total
number k. Each division, we compute the max subarray of left (k + 1) // 2 repeats
of arr, right k // 2 repeats of arr, and the max sum of cross array.
2. Cross array requires the max of subarray starting at the front of the split
and ending at the end of the split. We can easily computte max_sub_start and
max_sub_end for arr. However, for repeats of arr, we have to also consider
the sum of arr. If the sum is positive, then max_sub_start/end can cross over
to the next repeat.

After taking care of these two tricks, we can arrive at the correct solution
with a simple recursive function.

This solution clocked in at 464 ms.


Solution5:
After reading the discussion boards, it is now clear that for k > 2, we don't
have to consider any of the arr in between. If sum(arr) <= 0, having
any repeats larger than 2 would definitely decrease or not change subarray sum
compared to having only 2 or 1 arr. If sum(arr) > 0, including a full repeat
of arr would always increase subarray sum. Therefore, we only need to consider
the max_cross + sum(arr) * (k - 2)

A bit more detail on the situation where sum(arr) > 0. An array can always be
displayed like this:

sum(arr) = prefix + max_subarray + suffix
max_sub_start = prefix + max_subarray
max_sub_end = max_subarray + suffix

when sum(arr) > 0, max_cross = max_sub_start + max_sub_end = sum(arr) + max_subarray > max_subarray
Therefore, we only have to consider max_cross + sum(arr) * (k - 2)

This solution clocked in at 380 ms.
"""


class Solution1:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        new_arr: List[int] = arr * k
        res: int = 0
        curr_max: int = new_arr[0]
        for a in new_arr[1:]:
            curr_max = max(a, curr_max + a)
            res = max(curr_max, res)
        return res % (10 ** 9 + 7)


class Solution2:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        # breakpoint()
        max_overall: int = 0
        max_sub_end: int = 0
        records: List[Set[int]] = [set() for _ in range(len(arr))]
        for i, a in enumerate(arr):
            max_sub_end = max(a, a + max_sub_end)
            records[i].add(max_sub_end)
            max_overall = max(max_overall, max_sub_end)
        for _ in range(k - 1):
            has_repeat: bool = False
            for i, a in enumerate(arr):
                max_sub_end = max(a, a + max_sub_end)
                if max_sub_end in records[i]:  # repeat starts
                    has_repeat = True
                    break
                else:
                    records[i].add(max_sub_end)
                max_overall = max(max_overall, max_sub_end)
            if has_repeat:
                break
        return max_overall % (10 ** 9 + 7)

    def __str__(self):
        return "Solution2"


class Solution3:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        # breakpoint()
        max_overall: int = 0
        max_sub_end: int = 0
        records: List[int] = [0] * len(arr)
        for i, a in enumerate(arr):
            max_sub_end = max(a, a + max_sub_end)
            records[i] = max_sub_end
            max_overall = max(max_overall, max_sub_end)
        for j in range(k - 1):
            is_not_bigger: bool = False
            for i, a in enumerate(arr):
                max_sub_end = max(a, a + max_sub_end)
                if (
                    max_sub_end == records[i]
                ):  # unable to get even bigger subarray max
                    is_not_bigger = True
                    break
                else:
                    records[i] = max_sub_end
                max_overall = max(max_overall, max_sub_end)
            if is_not_bigger:
                break
        return max_overall % (10 ** 9 + 7)

    def __str__(self):
        return "Solution3"


class Solution4:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        max_each: int = 0  # max subarray sum for arr
        me: int = 0  # max subarray sum ending in the last pos
        ms: int = 0  # max subarray sum starting at the first pos
        s: int = 0  # sum of the array
        for i, a in enumerate(arr):
            me = max(a, a + me)
            max_each = max(max_each, me)
            s += a
            ms = max(ms, s)
        return self.helper(k, ms, me, max_each, s) % (10 ** 9 + 7)

    def helper(self, k: int, ms: int, me: int, max_each: int, s: int) -> int:
        if k == 1:
            return max_each
        else:
            left: int = self.helper((k + 1) // 2, ms, me, max_each, s)
            right: int = self.helper(k // 2, ms, me, max_each, s)
            if s >= 0:
                max_cross = s * ((k + 1) // 2 - 1) + me + s * (k // 2 - 1) + ms
            else:
                max_cross = ms + me
            return max(left, right, max_cross)

    def __str__(self):
        return "Solution4"


class Solution5:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        max_each: int = 0  # max subarray sum for arr
        max_sub_end: int = 0  # max subarray sum ending in the last pos
        max_sub_start: int = 0  # max subarray sum starting at the first pos
        sum_array: int = 0
        for i, a in enumerate(arr):
            max_sub_end = max(a, a + max_sub_end)
            max_each = max(max_each, max_sub_end)
            sum_array += a
            max_sub_start = max(max_sub_start, sum_array)
        max_cross: int = max_sub_start + max_sub_end
        if k == 1:
            res = max_each
        elif k == 2:
            res = max(max_each, max_cross)
        else:
            res = (
                sum_array * (k - 2) + max_cross
                if sum_array > 0
                else max(max_each, max_cross)
            )
        return res % (10 ** 9 + 7)

    def __str__(self):
        return "Solution5"


def random_arr(LEN):
    return [randint(-10, 10) for _ in range(LEN)]


def random_test(Sa, Sb):
    sola = Sa()
    solb = Sb()
    T = 10
    for _ in range(T):
        k = 100
        arr = random_arr(1000)
        ra = sola.kConcatenationMaxSum(arr, k)
        rb = solb.kConcatenationMaxSum(arr, k)
        if ra != rb:
            print(f"{sola} = {ra}, {solb} = {rb}")
            print(arr)
            print(k)


def test_single():
    sol1 = Solution1()
    sol2 = Solution2()
    arr = [3, -3, 5]
    k = 100
    print(f"res1 = {sol1.kConcatenationMaxSum(arr, k)}")
    print(f"res2 = {sol2.kConcatenationMaxSum(arr, k)}")


def time_it(Sa, Sb):
    sola = Sa()
    solb = Sb()
    arr = random_arr(10000)
    k = 1000
    begin = time()
    print(sola.kConcatenationMaxSum(arr, k))
    print(f"{sola}: {time() - begin}")

    begin = time()
    print(solb.kConcatenationMaxSum(arr, k))
    print(f"{solb}: {time() - begin}")


# random_test(Solution3, Solution4)
# test_single()
# print(random_arr(10**5))
time_it(Solution4, Solution5)
