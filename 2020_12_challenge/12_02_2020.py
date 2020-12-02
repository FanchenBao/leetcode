# from pudb import set_trace; set_trace()
from typing import List
import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    """Easy question if we do not consider memory limit. 84% ranking."""

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.lst = []
        node = head
        while node:
            self.lst.append(node.val)
            node = node.next
        self.length = len(self.lst)

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return self.lst[random.randint(0, self.length - 1)]
        

class Solution2:
    """Naive way of O(1) extra space. 67% ranking"""

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.length = 0
        self.head = head
        node = head
        while node:
            self.length += 1
            node = node.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        steps = random.randint(1, self.length)
        node = self.node
        while steps:
            node = node.next
            steps -= 1
        return node.val


class Solution3:
    """Standard reservoir sampling
    
    This solution does not pass OJ, but I think it is the correct one for
    hanlding infinite stream of number. This solution guarantees that the value
    in reservoir is 1 / k + i chance to be selected.

    However, this solution fails if the stream is finite, because it simply
    cannot loop around and still guarantee equal chance of hitting all the
    numbers.
    """

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.k = 1  # reservoir size
        self.reservoir = self.head.val
        self.node = self.head.next
        self.i = 1  # additional element after the initial reservior size

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        For use in infinite stream only because there if end has reached, this
        algorithm cannot produce random value anymore.
        """
        if random.randint(1, self.i + self.k) <= self.k:
            self.reservoir = self.node.val
        self.node = self.node.next
        self.i += 1
        return self.reservoir


class Solution4:
    """Standard reservoir sampling
    
    This solution is suitable for finite linked list. Finished with 26% ranking.
    """

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        For use in infinite stream only because there if end has reached, this
        algorithm cannot produce random value anymore.
        """
        reservoir = self.head.val
        node = self.head
        i, k = 1, 1
        while node:
            if random.randint(1, i + k) <= k:
                reservoir = node.val
            node = node.next
            i += 1
        return reservoir

        



sol = Solution3()
tests = [
    # ([1, 2, 3, 1], 3, 0, True),
    # ([1, 0, 1, 1], 1, 2, True),
    ([1, 5, 9, 1, 5, 9], 2, 3, False),
    # ([1, 4, 9, 1, 4, 9], 1, 3, True),
    # ([-1, -1], 1, -1, False),
    # ([1, 3, 6, 2], 1, 2, True),
]

for i, (nums, k, t, ans) in enumerate(tests):
    res = sol.containsNearbyAlmostDuplicate(nums, k, t)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
