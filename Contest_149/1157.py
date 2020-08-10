#! /usr/bin/env python3
from typing import List, Tuple, Dict
from collections import Counter

# from random import randint
from math import log
from collections import defaultdict
from bisect import bisect_left, bisect_right

"""08/20/2019

Solution1:
I predict, without even writing Solution1, it will time out.
And my prediction is correct. Solution1 is the most naive. Due to a ton of
repetitive computation, it is not surprising that it timed out.


Solution2:
I used segment tree for this solution, with each node being a dict recording
the frequency of each number and a tuple recording the max frequency number and
its corresponding frequency. This segment tree implementation does speed up
the solution, but it still timed out.


Solution3:
I gave up after the unsuccessful attempt with Solution2, even though I did
believe segment tree was a viable solution. After reading the discussion, I
saw that segment tree was indeed one of the standard solution to this problem.
The difference between a successful implementation of segment tree and my
previous segment tree is the merge step both during segment tree initialization
and querying. The key factors are:

1. Only the majority number in a child node has the possibility of becoming
majority in the parent node. So when merging two child nodes, we only need to
examine the majority number in each child. If majority does not exist in a
child node, we don't even have to examine it.

2. Examination can be done in O(log(n)) time. The way I examined majority in
the previous method was via dictionary, and it was O(n) time with probably quite
some overhead with dictionary processes. A very good way of examination is to
use binary search on a list of positions of the target number against a querying
range's start and end. Once proper positions on the list for querying range's
start and end, we can easily read how many of such target number exist within
this range. This takes O(log(n)) time with little overhead.

Once the merge function is optimized via the two factors above, the solution
shall pass OJ. I cannot do it today since I don't have internet at home. I will
run it tomorrow.

Update 08/21/2019
Solution3 clocked in at 1076 ms, 55%

P.S. The random pick method is definitely brilliant. It is similar to the method
in one of the CodeJam problem. Here, since we are looking for the majority
number, it is natural that if such number exists, we shall be able to randomly
pick it out more than 50% of the time. Error happens if none of the number we
pick is the majority while the majority actually exists. The probably of doing
this is less than 1/2 for each pick. Thus, the more picks we do, the less likely
that all of them are non-majority number. The concensus on the discussion was
to pick 20 times, in which the probability all of them are wrong picks is as
small as (1/2)**20, which furthr amounts to 0.01 times of error in 10000 queries.
For each random pick, we do the same binary search method to check whether it
is the real majority or not.
"""


class MajorityChecker1:
    def __init__(self, arr: List[int]):
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        count = Counter(self.arr[left : right + 1])
        for k, v in count.items():
            if v >= threshold:
                return k
        return -1


class MajorityChecker2:
    def __init__(self, arr: List[int]) -> None:
        self.arr = arr
        # https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/
        size = 2 * (2 ** int(log(len(self.arr), 2) + 1)) - 1
        self.seg_tree: List[Tuple[Dict[int, int], Tuple[int, int]]] = [
            (defaultdict(int), (0, 0)) for _ in range(size)
        ]
        self.init_seg_tree(0, 0, len(self.arr) - 1)

    def query(self, left: int, right: int, threshold: int) -> int:
        count_dict, majority_tuple = self.query_seg_tree(
            left, right, 0, len(self.arr) - 1, 0
        )
        return -1 if majority_tuple[1] < threshold else majority_tuple[0]

    def merge(
        self,
        item1: Tuple[Dict[int, int], Tuple[int, int]],
        item2: Tuple[Dict[int, int], Tuple[int, int]],
    ) -> Tuple[Dict[int, int], Tuple[int, int]]:
        res_dict: Dict[int, int] = defaultdict(int)
        res_majority: Tuple[int, int] = item1[1]
        res_dict.update(item1[0])
        for k, v in item2[0].items():
            res_dict[k] += v
            if res_dict[k] > res_majority[1]:
                res_majority = (k, res_dict[k])

        return res_dict, res_majority

    def init_seg_tree(self, root: int, ss: int, se: int) -> None:
        if ss == se:
            self.seg_tree[root] = ({self.arr[ss]: 1}, (self.arr[ss], 1))
        else:
            mid = ss + (se - ss) // 2
            self.init_seg_tree(2 * root + 1, ss, mid)
            self.init_seg_tree(2 * root + 2, mid + 1, se)
            self.seg_tree[root] = self.merge(
                self.seg_tree[2 * root + 1], self.seg_tree[2 * root + 2]
            )

    def query_seg_tree(
        self, qs: int, qe: int, ss: int, se: int, root: int
    ) -> Tuple[Dict[int, int], Tuple[int, int]]:
        if qs == ss and qe == se:
            return self.seg_tree[root]
        mid = ss + (se - ss) // 2
        if qs > mid:
            return self.query_seg_tree(qs, qe, mid + 1, se, root * 2 + 2)
        elif qe <= mid:
            return self.query_seg_tree(qs, qe, ss, mid, root * 2 + 1)
        else:
            return self.merge(
                self.query_seg_tree(qs, mid, ss, mid, root * 2 + 1),
                self.query_seg_tree(mid + 1, qe, mid + 1, se, root * 2 + 2),
            )


class MajorityChecker3:
    def __init__(self, arr: List[int]) -> None:
        self.arr = arr

        # provision record for all positions of each number
        self.pos_dict: Dict[int, List[int]] = defaultdict(list)
        for i, a in enumerate(self.arr):
            self.pos_dict[a].append(i)

        # https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/
        size = 2 * (2 ** int(log(len(self.arr), 2) + 1)) - 1
        # provision segment tree
        self.seg_tree: List[int] = [-1] * size
        self.init_seg_tree(0, 0, len(self.arr) - 1)

    def query(self, left: int, right: int, threshold: int) -> int:
        maj = self.query_seg_tree(left, right, 0, len(self.arr) - 1, 0)
        return maj if self.frequency(maj, left, right) >= threshold else -1

    def merge(self, maj1: int, maj2: int, start: int, end: int) -> int:
        # NOTE: if a child node has no majority, none of its members can be
        # majority in the parent node. When a child has a majority number, it
        # may or may not be the majority in the parent node. Further examination
        # is needed.
        if (
            maj1 != -1
            and self.frequency(maj1, start, end) * 2 > end - start + 1
        ):
            return maj1
        if (
            maj2 != -1
            and self.frequency(maj2, start, end) * 2 > end - start + 1
        ):
            return maj2
        return (
            -1
        )  # when neither child node has majority, parent node has no majority

    def frequency(self, target: int, start: int, end: int) -> int:
        # use binary search to find how many target number resides within the
        # given range [start, end]
        return bisect_right(self.pos_dict[target], end) - bisect_left(
            self.pos_dict[target], start
        )

    def init_seg_tree(self, root: int, ss: int, se: int) -> None:
        if ss == se:
            self.seg_tree[root] = self.arr[ss]
        else:
            mid = ss + (se - ss) // 2
            self.init_seg_tree(2 * root + 1, ss, mid)
            self.init_seg_tree(2 * root + 2, mid + 1, se)
            self.seg_tree[root] = self.merge(
                self.seg_tree[2 * root + 1],
                self.seg_tree[2 * root + 2],
                ss,
                se,
            )

    def query_seg_tree(
        self, qs: int, qe: int, ss: int, se: int, root: int
    ) -> int:
        if qs == ss and qe == se:
            return self.seg_tree[root]
        mid = ss + (se - ss) // 2
        if qs > mid:
            return self.query_seg_tree(qs, qe, mid + 1, se, root * 2 + 2)
        elif qe <= mid:
            return self.query_seg_tree(qs, qe, ss, mid, root * 2 + 1)
        else:
            return self.merge(
                self.query_seg_tree(qs, mid, ss, mid, root * 2 + 1),
                self.query_seg_tree(mid + 1, qe, mid + 1, se, root * 2 + 2),
                qs,
                qe,
            )


test_case_first: List[int] = [2, 2, 1, 2, 1, 2, 2, 1, 1, 2]
test_case: List[List[int]] = [
    [2, 5, 4],
    [0, 5, 6],
    [0, 1, 2],
    [2, 3, 2],
    [6, 6, 1],
    [0, 3, 3],
    [4, 9, 6],
    [4, 8, 4],
    [5, 9, 5],
    [0, 1, 2],
]
mc = MajorityChecker1(test_case_first)
for t in test_case:
    print(mc.query(t[0], t[1], t[2]))
