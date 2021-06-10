# from pudb import set_trace; set_trace()
from typing import List
import bisect


class MyCalendar:
    def __init__(self):
        self.bookings = []
        
    def book(self, start: int, end: int) -> bool:
        """LeetCode 729

        Naive O(N^2) solution. The trick is with how to detect overlap. But
        we didn't make any effort to improve on the data structure for storing
        the ranges.

        We can pass because there are only 1000 booking calls. So O(N^2) is
        still tolerable.

        1128 ms, 15% ranking.
        """
        for s, e in self.bookings:
            if s <= start < e or s < end < e or (start < s and end >= e):
                # the if condition can be simplied as `if start < e and end > s`
                return False
        self.bookings.append((start, end))
        return True


class MyCalendar:
    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        """Still O(N^2), but with time saving when a failed booking happens.

        We get 200 ms runtime, 90% ranking.

        Apparently, the test cases contain a lot of failed bookings. And this
        solution takes advantage of that fully. But I am still not happy with
        it, because in the worst case scenario, where the bookings are given
        in reverse order, then this solution runs in O(N^2).
        """
        if not self.bookings:
            self.bookings.append((start, end))
            return True
        idx = bisect.bisect_left(self.bookings, (start, end))
        if idx > 0 and self.bookings[idx - 1][1] > start:
            return False
        if idx < len(self.bookings) and self.bookings[idx][0] < end:
            return False
        self.bookings.insert(idx, (start, end))
        return True



class BSTNode:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

    def insert(self, node) -> bool:
        if node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        return False


class MyCalendar:
    def __init__(self):
        self.bookings = None

    def book(self, start: int, end: int) -> bool:
        """The official Binary Search Tree solution. I was thinking about a
        tree data structure to handle faster insertion while maintaining the
        sorted order. But the scheme I was cooking was too convoluted. This is
        the correct way to construct a tree for this purpose. Average run time
        is O(Nlog(N)), but worst case can still be O(N^2).

        264 ms.
        """
        if not self.bookings:
            self.bookings = BSTNode(start, end)
            return True
        return self.bookings.insert(BSTNode(start, end))


# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
