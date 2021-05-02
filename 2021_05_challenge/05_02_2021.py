# from pudb import set_trace; set_trace()
from typing import List
import heapq


class Solution1:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """LeetCode 630

        This solution is based on hint, although I have basically the same
        idea as the hint. Yet, I was not sure to pursue the idea illustrated in
        the hint.

        The first task is to sort courses. We sort based on last day. It can be
        proven that having large last day after small last day is a better
        strategy than the other way around. This is because, if cur_time + dur
        fits in both the small and large last day, then their order doesn't
        matter. Similarly, if cur_time + dur does not fit in either the small or
        large last day, their order doesn't matter. It only matters, if one
        of the last day fits. Apparently, it can only be the large last day that
        fits, and the small last day doesn't fit. In this scenario, if we do
        the large last day first, then we are guaranteed to only fit one course.
        However, if we do the small last day first, then it is guaranteed that
        we can fit both courses. Therefore, it is always better to sort the
        courses based on their last day.

        If the last day is the same, we want to have the smaller duration first,
        because that can produce larger gaps between the end of the class and
        the last day, which provides higher chance of fitting another class.

        The key idea from the hint is to iterate through the sorted courses, and
        when a course cannot fit, we check whether it is a good deal to drop
        the course with the largest duration so far. The check is based on
        whether the drop can fit the new last day and whether the drop leads to
        bigger gap between the end of the current course and the last day. If
        both conditions are satisfied, we do the drop.

        To obtain the largest duration so far, we use a heapq.

        O(Nlog(N)) 732 ms, 31% ranking.
        """
        courses.sort(key=lambda tup: (tup[1], tup[0]))
        heap = []
        cur_time = 0
        for dur, last in courses:
            if cur_time + dur <= last:
                heapq.heappush(heap, -dur)
                cur_time += dur
            else:
                if heap:
                    max_dur = -heapq.heappop(heap)
                    if cur_time + dur - max_dur <= last and cur_time + dur - max_dur < cur_time:
                        cur_time = cur_time - max_dur + dur
                        heapq.heappush(heap, -dur)
                    else:
                        heapq.heappush(heap, -max_dur)
        return len(heap)


class Solution2:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """This is according to the solution. The key idea is to pop the max
        duration encountered so far if and only if it is larger than the current
        duration. This is because if the max duration is larger than the current
        duration, we can guarantee that the swap results in larger gap between
        the current time and the last day. In other words, we don't have to
        check for it separately.
        """
        courses.sort(key=lambda tup: (tup[1], tup[0]))
        heap = []
        cur_time = 0
        for dur, last in courses:
            if cur_time + dur <= last:
                heapq.heappush(heap, -dur)
                cur_time += dur
            elif heap and -heap[0] > dur:
                cur_time = cur_time + dur + heapq.heappop(heap)
                heapq.heappush(heap, -dur)
        return len(heap)


sol = Solution2()
tests = [
    ([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]], 3),
    ([[1, 2]], 1),
    ([[3, 2], [4, 3]], 0),
    ([[5, 5], [4, 6], [2, 6]], 2),
]
for i, (courses, ans) in enumerate(tests):
    res = sol.scheduleCourse(courses)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
