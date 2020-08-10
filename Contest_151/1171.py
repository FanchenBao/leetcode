#! /usr/bin/env python3
from typing import List, Dict

# from collections import Counter
# from bisect import bisect_right
# from pprint import pprint as pp
from random import randint
from collections import OrderedDict

"""08/26/2019

Solution1:
Brute force. This might run into TLE.
Surprisingly, brute force (i.e. checking all sum of all consecutive nodes)
did not TLE. This solution clocked in at 140 ms, 34%

Solution2:
I read the discussion, specifically this one,

https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/discuss/366319/JavaC%2B%2BPython-Greedily-Skip-with-HashMap

and learned that using prefix sum, we can solve this problem in almost one pass.
I actually thought about prefix sum, but only focused on how to transform prefix
sum to suffix sum in order to fix a DP solution. In fact, there is no need for
suffix sum, because a sum of zero would appear naturally IF the same prefix sum
appears twice. This means the sum of consecutive values between the last time such
prefix sum occurs and the current time the same prefix sum appears must be zero.
We just need to remove those values in between.

A dict is perfect for this job. But pay attention to the use of OrderedDict,
because once the consecutive values are removed on the linked list, the
corresponding prefix sum key values in the OrderedDict must also be removed
as well. I used the dicsussion's solution for such removal, since it is neater
than my own.

This solution clocked in at 48 ms, 90%

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy: ListNode = ListNode(0)
        dummy.next = head
        pre: ListNode = dummy
        acc: int = 0
        while pre.next:
            curr_node: ListNode = pre.next
            while curr_node:
                acc += curr_node.val
                if acc == 0:
                    pre.next = curr_node.next
                    break
                curr_node = curr_node.next
            else:
                pre = pre.next
                acc = 0
        return dummy.next


class Solution2:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy: ListNode = ListNode(0)
        dummy.next = head
        seen: Dict[int, ListNode] = OrderedDict()
        seen[0] = dummy
        acc = 0
        while head:
            acc += head.val
            if acc not in seen:
                seen[acc] = head
            else:
                seen[acc].next = head.next
                temp_node = seen[acc]
                while acc in seen:
                    seen.popitem()
                seen[acc] = temp_node
            head = head.next
        return dummy.next


def gen_num(length: int) -> List[int]:
    return [randint(-1000, 1000) for _ in range(length)]


print(gen_num(1000))
