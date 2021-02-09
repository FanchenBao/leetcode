# from pudb import set_trace; set_trace()
from typing import List


# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator1:
    """This seems to be an easy question. We use an attribute self.top to record
    the current top value in the iterator. Each time peek is called, we simply
    return the top value. The top value changes when next is called. If the
    original iterator has been exhausted, we set the top value to None. Thus,
    we can use the top value to also return hasNext (i.e. check whether the
    top value is None).

    32 ms, 68% ranking.
    """

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.top = self.iter.next() if self.iter.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.top

    def next(self):
        """
        :rtype: int
        """
        ret = self.top
        self.top = self.iter.next() if self.iter.hasNext() else None
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.top is not None


class PeekingIterator2:
    """This is the more generic version. The version above cannot handle the
    situation where the iterator contains None.

    Reference:
    https://leetcode.com/problems/peeking-iterator/discuss/1055977/python-3-greedy-and-lazy-24ms

    28 ms, 88% ranking.
    """

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.has_peaked = False
        self.top = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.has_peaked:
            self.top = self.iter.next()
        return self.top

    def next(self):
        """
        :rtype: int
        """
        if self.has_peaked:
            self.has_peaked = False
            return self.top
        return self.iter.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.has_peaked or self.iter.hasNext()


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
