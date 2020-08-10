#! /usr/bin/env python3
from typing import List
from bisect import bisect_right

"""08/08/2019

SnapshotArray1:
Most naive implementation. Get memory limit exceeded error.

SnapshotArray2:
Use str instead of int array for storage, solved memory limit exceeded error,
but ran int to TLE.

SnapshotArray3:
Instead of tracking whole array, this method tracks only the number that is
changed. But it still timed out.

SnapshotArray4:
Same as SnapshotArray3, but use binary search for get() function. It passed OJ,
clocking at 632 ms, 11.7%.

SnapshotArray5:
Same method as SnapshotArray4, but with the ingenious insight from
https://leetcode.com/problems/snapshot-array/discuss/350562/JavaPython-Binary-Search
I am going to use bisect to do binary search. Use bisect, the solution clocked
at 548 ms, 40%.
"""


class SnapshotArray1:
    def __init__(self, length: int):
        self.array_versions: List[List[int]] = [[0] * length]
        self.snap_id = -1

    def set(self, index: int, val: int) -> None:
        self.array_versions[-1][index] = val

    def snap(self) -> int:
        self.snap_id += 1
        self.array_versions.append(self.array_versions[-1][:])
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        return self.array_versions[snap_id][index]


class SnapshotArray2:
    def __init__(self, length: int):
        self.array: List[str] = ["0"] * length
        self.snap_id = -1
        self.archives: List[str] = []

    def set(self, index: int, val: int) -> None:
        self.array[index] = str(val)

    def snap(self) -> int:
        self.snap_id += 1
        self.archives.append(",".join(self.array))
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        return int(self.archives[snap_id].split(",")[index])


class SnapshotArray3:
    def __init__(self, length: int):
        self.archive = [[[0, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if self.archive[index][-1][0] < self.snap_id:
            self.archive[index].append([self.snap_id, val])
        else:
            self.archive[index][-1][1] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        for i, v in enumerate(self.archive[index]):
            if v[0] == snap_id:
                return v[1]
            elif v[0] > snap_id:
                return self.archive[index][i - 1][1]
        return self.archive[index][-1][1]


class SnapshotArray4:
    def __init__(self, length: int):
        self.archive = [[[0, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if self.archive[index][-1][0] < self.snap_id:
            self.archive[index].append([self.snap_id, val])
        else:
            self.archive[index][-1][1] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        f, b = 0, len(self.archive[index]) - 1
        while f < b:
            m = (f + b) // 2
            if self.archive[index][m][0] < snap_id:
                f = m + 1
            elif self.archive[index][m][0] > snap_id:
                b = m - 1
            else:
                return self.archive[index][m][1]
        # note that this binary search exists when f == b, thus we cannot test
        # whether self.archive[index][f][0] == snap_id in the loop. Consequently,
        # we have to test that in the return statement.
        return (
            self.archive[index][f][1]
            if self.archive[index][f][0] <= snap_id
            else self.archive[index][f - 1][1]
        )


class SnapshotArray5:
    def __init__(self, length: int):
        self.archive = [[[0, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if self.archive[index][-1][0] < self.snap_id:
            self.archive[index].append([self.snap_id, val])
        else:
            self.archive[index][-1][1] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # note that we are comparing list in biset_right()
        # Two ways to approach locating where the snap_id is in the array
        # 1. Make sure when snap_id matches any existing snap_id, the [snap_id,
        # 10**9 + 1] is always bigger than the list in archive. Thus, the pos
        # returned will always need to minus 1 to find the correct value.
        return self.archive[index][
            bisect_right(self.archive[index], [snap_id, 10 ** 9 + 1]) - 1
        ][1]

        # 2. Use [snap_id + 1], as recommended by the discussion. It achieves
        # the same effect as method 1 and appears much neater
        # return self.archive[index][bisect_right(self.archive[index], [snap_id + 1]) - 1][1]
