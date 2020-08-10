#! /usr/bin/env python3
from typing import List
from random import randint

"""09/12/2019

Solution1:
First of all, I must admit this solution didn't come organically, as I used
trial and error with OJ to find the test case that my original solution failed.
That said, I am still quite happy with this solution. The main idea is the same
as Kadane's algorithm, where we keep the max continuing sum ending at each pos.
The difficult part is that now we are allowed to drop at most one element. To
handle that, I include a variable `deletion` to specifically record the element
that has been dropped. For each new element in the array, we consider how we can
arrive the max continuing sum ending at the new element, using the information
from the new element, the max continuing sum ending at the previous element, and
`deletion`.

If the new element is positive, the case is trivial, because we either choose
the new element as `drop_max` if it is negative, or add the
new element to `drop_max` if it is positive.

If the new element is negative, the case is more complicated. But still, there
are two easy cases. First, if the new element is less negative than `drop_max`,
we can safely use the new element as `drop_max`. Second, if the new element is
more negative than `drop_max` but currently we don't have a deletion yet, we can
assign deletion to the new element.

The last case where the new element is more negative than `drop_max`, and we
already have a deletion is the most complicated. We need to compare `deletion`
with the new element and choose the more negative one to drop. Then, and this is
from my trial and error with OJ, we have to compare with the result of a strict
Kadane's algorithm, and decide whether using a `non_drop_max` would yield even
larger sum.

After all these cases, we are done. This solution clocked in at 264 ms, 98%. I
am very happy.


UPDATE: 09/15/2019

Solution2:
After reading some discussion posts, I realized that this problem could be resolved
in the most canonical DP manner. For element arr[i], `max0` is the max subarray
sum ending at arr[i - 1] with no deletion; `max1` is the max subarray sum
ending at arr[i - 1] with at most one deletion; `res` is the overall max to be
returned at the end. For each arr[i], we consider a new `max1`. There are three
situations:
1. We use the previous `max1`. Since there must have been at most one element
deleted, arr[i] cannot be removed. So `max1 = max1 + arr[i]`
2. We need to remove arr[i]. Then the new `max1` must be the same as the previous
`max0`, i.e. `max1 = max0`
3. arr[i] is so big that it is better to start fresh, i.e. `max1 = arr[i]`
We pick the largest among the three situations to tbe the new `max1`. And keep
updating `max0` and overall max.

This solution clocked in at 292 ms, 88%.
"""


class Solution1:
    def maximumSum(self, arr: List[int]) -> int:
        total_max: int = arr[0]
        drop_max: int = arr[
            0
        ]  # max continuing sum ending at current pos allowing to drop one element
        non_drop_max: int = arr[
            0
        ]  # max continuing sum ending at current pos without drop
        deletion: int = 0  # record the value of the dropped element
        for a in arr[1:]:
            if a >= 0:
                if drop_max >= 0:
                    drop_max += a
                else:
                    drop_max = a
                    deletion = 0
            else:
                if a >= drop_max:  # e.g. drop_max = -5, a = -1
                    drop_max = a
                    deletion = 0
                else:
                    if deletion == 0:  # no deletion yet, we delete `a`
                        deletion = a
                    else:
                        if deletion > a:  # we drop `a` and include `deletion`
                            drop_max += deletion
                            deletion = a
                        else:
                            drop_max += a
                        # After processing drop_max, we need to check whether
                        # using non_drop_max can lead to better outcome
                        # The first part of the condition below is trivial, the
                        # second part means that if `non_drop_max` and `drop_max`
                        # are the same, we need to compare the value of the dropped
                        # item. For `non_drop_max`, the to-be-dropped element is
                        # a. We always want to keep the dropped element as large
                        # as possible, because that way if we encounter an even
                        # smaller
                        if non_drop_max > drop_max or (
                            non_drop_max == drop_max and a > deletion
                        ):
                            drop_max = non_drop_max
                            deletion = a
            non_drop_max = max(a, non_drop_max + a)
            total_max = max(total_max, drop_max)
        return total_max


class Solution2:
    def maximumSum(self, arr: List[int]) -> int:
        max1: int = arr[0]  # max subarray sum with at most one deletion
        max0: int = arr[0]  # max subarray sum with NO deletion
        res: int = arr[0]  # overall max to be returned
        for a in arr[1:]:
            max1 = max(
                max1 + a, max0, a
            )  # include a, not include a, or start with a
            max0 = max(max0 + a, a)  # update `max0`
            res = max(res, max1)  # update overall max
        return res


def test_cases():
    sol = Solution2()
    # test 1
    print("Test case 1: PASS") if sol.maximumSum(
        [1, -2, 0, 3]
    ) == 4 else print("Test case 1: fail")
    # test 2
    print("Test case 2: PASS") if sol.maximumSum(
        [1, -2, -2, 3]
    ) == 3 else print("Test case 2: fail")
    # test 3
    print("Test case 3: PASS") if sol.maximumSum(
        [-1, -1, -1, -1]
    ) == -1 else print("Test case 3: fail")
    # test 4
    print("Test case 4: PASS") if sol.maximumSum(
        [-2, -4, 2, 1, -4, 2, 4, 1, -3, -4, 1, 5, 1, -3, 0, 2, 0]
    ) == 11 else print("Test case 4: fail")
    # test 5
    print("Test case 5: PASS") if sol.maximumSum(
        [-3, -4, -5, -1, 1, 1, 3, 4, 4, 0, 0, 1, -4, -5, -2, 5, 5, -3, 4, -1]
    ) == 19 else print("Test case 5: fail")


def test_multiple():
    sol1: Solution1 = Solution1()
    sol2: Solution2 = Solution2()
    length: int = randint(1, 10 ** 5)
    arr: List[int] = [randint(-10 ** 4, 10 ** 4) for i in range(length)]
    T: int = 10
    for _ in range(T):
        res1: int = sol1.maximumSum(arr)
        res2: int = sol2.maximumSum(arr)
        if res1 != res2:
            print(f"res1 = {res1}")
            print(f"res2 = {res2}")
            print(arr)


test_multiple()
# test_cases()
