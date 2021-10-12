# from pudb import set_trace; set_trace()
from typing import List
import heapq
from collections import deque, defaultdict
from random import randint
from copy import deepcopy


class Solution1:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        """LeetCode 1943

        TLE
        """
        heapq.heapify(segments)
        mixed = heapq.heappop(segments)
        res = []
        while segments:
            paint = heapq.heappop(segments)
            if mixed[0] <= paint[0] < mixed[1]:
                if mixed[0] < paint[0]:
                    res.append([mixed[0], paint[0], mixed[2]])
                mixed[0] = paint[0]
                if mixed[1] < paint[1]:
                    heapq.heappush(segments, [mixed[1], paint[1], paint[2]])
                elif mixed[1] > paint[1]:
                    heapq.heappush(segments, [paint[1], mixed[1], mixed[2]])
                    mixed[1] = paint[1]
                mixed[2] += paint[2]
            elif paint[0] >= mixed[1]:
                res.append(mixed)
                mixed = paint
        return res + [mixed]


class Solution2:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        """TLE"""
        segments.sort(key=lambda ele: (ele[0], ele[1]))
        queue, res = [], []
        for paint in segments:
            if not queue:
                queue.append(paint)
            else:
                temp = []
                for mixed in queue:
                    if paint[0] >= paint[1]:
                        temp.append(mixed)
                        continue
                    if mixed[1] <= paint[0]:
                        res.append(mixed)
                    else:
                        if mixed[0] < paint[0]:
                            res.append([mixed[0], paint[0], mixed[2]])
                        if mixed[1] <= paint[1]:
                            temp.append([paint[0], mixed[1], mixed[2] + paint[2]])
                            paint[0] = mixed[1]
                        else:
                            temp.append([paint[0], paint[1], mixed[2] + paint[2]])
                            temp.append([paint[1], mixed[1], mixed[2]])
                            paint[0] = paint[1]
                if paint[0] < paint[1]:
                    temp.append(paint)
                queue = temp
        return res + queue


class Solution3:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        """I was not able to solve this. So I checked lee215, and here is his
        solution:

        https://leetcode.com/problems/describe-the-painting/discuss/1359815/JavaC%2B%2BPython-Sweep-Line

        This feels like a reversed? prefix sum. Basically, we find the delta
        for each position in segments and put that in a dictionary d. d[i] means
        the delta value from i towards infinity. Thus, to find the sum of
        segment [i, j), we need to sum up d[1], d[2], ..., d[i]. That is the
        algo.
        """
        d = defaultdict(int)
        for i, j, c in segments:
            d[i] += c  # delta from the start of a segment is always to add
            # delta from the end of a segment needs to cancel delta from the
            # start such that the only segment that has value c is [i, j), and
            # all the other segments towards infinity has value c as 0
            d[j] -= c
        res = []
        i = 0
        # since all colors are unique, we can report all segments
        for j in sorted(d):
            if d[i]:  # if d[i] == 0, that means there is no color in [i, j)
                res.append([i, j, d[i]])
            # need to compute the actual value from j to its next position
            d[j] += d[i]  # d[i] = d[1] + d[2] + d[3] + ... + d[i]
            i = j  # acquire the start position of a new segment
        return res


sol1 = Solution1()
sol = Solution3()
# tests = [
#     ([[1, 4, 5], [4, 7, 7], [1, 7, 9]], [[1, 4, 14], [4, 7, 16]]),
#     ([[1, 7, 9], [6, 8, 15], [8, 10, 7]], [[1, 6, 9], [6, 7, 24], [7, 8, 15], [8, 10, 7]]),
#     ([[1, 4, 5], [1, 4, 7], [4, 7, 1], [4, 7, 11]], [[1, 4, 12], [4, 7, 12]]),
# ]
num_test = 10
seg_len = 10
tests = []
for _ in range(num_test):
    test = []
    for _ in range(seg_len):
        while True:
            paint = [randint(1, 100), randint(1, 100), randint(1, 100)]
            if paint[1] > paint[0]:
                break
        test.append(paint)
    tests.append(test)

for i, segments in enumerate(tests):
    res = sol.splitPainting(deepcopy(segments))
    ans = sol1.splitPainting(deepcopy(segments))

    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}, Test: {segments}')
