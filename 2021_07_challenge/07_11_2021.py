# from pudb import set_trace; set_trace()
from typing import List
from sortedcontainers import SortedList
import heapq


class MedianFinder1:

    def __init__(self):
        """
        LeetCode 295

        initialize your data structure here.

        Solved by Sorted Containers, which is more or less a cheat.

        296 ms, 27% ranking.
        """
        self.lst = SortedList()

    def addNum(self, num: int) -> None:
        self.lst.add(num)

    def findMedian(self) -> float:
        n = len(self.lst)
        if n % 2:
            return self.lst[n // 2]
        return (self.lst[n // 2] + self.lst[n // 2 - 1]) / 2


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    def add(self, val):
        self.root = self._add(self.root, val)
        self.count += 1

    def query(self, nth):
        return self._traverse(self.root, nth)[0]

    def _add(self, node, val):
        if not node:
            return TreeNode(val)
        if val <= node.val:
            node.left = self._add(node.left, val)
        else:
            node.right = self._add(node.right, val)
        return node

    def _traverse(self, node, remain):
        if not node:
            return None, remain
        val, cur_remain = self._traverse(node.left, remain)
        if cur_remain:
            if cur_remain == 1:
                return node.val, 0
            return self._traverse(node.right, cur_remain - 1)
        else:
            return val, cur_remain


class MedianFinder2:

    def __init__(self):
        """
        initialize your data structure here.

        """
        self.hp = []
        self.n = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.hp, -num)
        self.n += 1
        if len(self.hp) > self.n // 2 + 1:
            heapq.heappop(self.hp)

    def findMedian(self) -> float:
        first_max = -self.hp[0]
        if self.n % 2:
            return first_max
        heapq.heappop(self.hp)
        second_max = -self.hp[0]
        heapq.heappush(first_max)
        return (first_max + second_max) / 2


class MedianFinder3:

    def __init__(self):
        """
        initialize your data structure here.
        
        Got a hint from the question about using heap. This solution keeps two
        heaps, one max heap and one min heap. Both heap has size n // 2.
        The max heap helps to maintain the n // 2 smallest values in the stream.
        The min heap helps to maintain the n // 2 largest values in the stream.
        Thus, we can obtain the n // 2 th smallest value from self.max_hp[0],
        and the n // 2 th largest value from self.min_hp[0]. This set up allows
        for very simple median computation when n is even. We simply perform
        (self.min_hp[0] - self.max_hp[0]) / 2 (note that we need to use
        -self.max_hp[0] because heapq is a min heap).

        When n is odd, we need to find self.mid. This can be found by comparing
        the currently added num to the n // 2 th largest value. If num is larger
        or equal to the n // 2 th largest value, then self.mid must be the value
        popped by self.min_hp after num is added to it. Otherwise, self.mid is
        the value popped by self.max_hp after -num is added to it.

        Each addNum() runs in O(logN), and each findMedian() runs in O(1). This
        is the same runtime as the Sorted Container solution.

        200 ms, 60 % ranking.
        """
        self.min_hp = []
        self.max_hp = []
        self.mid = None
        self.n = 0

    def addNum(self, num: int) -> None:
        self.n += 1
        if self.n % 2:
            if self.min_hp and num >= self.min_hp[0]:
                self.mid = heapq.heappushpop(self.min_hp, num)
            else:
                self.mid = -heapq.heappushpop(self.max_hp, -num)
        else:
            if num >= self.mid:
                heapq.heappush(self.max_hp, -self.mid)
                heapq.heappush(self.min_hp, num)
            else:
                heapq.heappush(self.max_hp, -num)
                heapq.heappush(self.min_hp, self.mid)
            self.mid = None

    def findMedian(self) -> float:
        if self.n % 2:
            return self.mid
        return (self.min_hp[0] - self.max_hp[0]) / 2


class MedianFinder4:

    def __init__(self):
        """Same solution as the one above with two heaps, but with better
        implementation. Ref:

        https://leetcode.com/problems/find-median-from-data-stream/discuss/1330808/Python-2-heaps-solution-explained
        """
        self.small, self.big = [], []  # small is a max heap, big is a min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.big, -heapq.heappop(self.small))
        if len(self.small) < len(self.big):
            heapq.heappush(self.small, -heapq.heappop(self.big))

    def findMedian(self) -> float:
        if len(self.small) == len(self.big):
            return (self.big[0] - self.small[0]) / 2
        return -self.small[0]


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
