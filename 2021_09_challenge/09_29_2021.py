# from pudb import set_trace; set_trace()
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        """LeetCode 725

        I don't think this is too difficult, but there are quite a few mind
        twists that one needs to go through.

        First of all, we use slow and past pointers to obtain the larger number
        of nodes in the partition and the number of large partitions. This is
        achieved by letting the fast node to go k steps at a time. Essentially
        when the fast node reaches the end, we can compute N % k by counting
        the number of steps the fast node moves in its last attempt. N % k is
        the number of large partitions. Meanwhile, we also keep track of the
        steps the slow node makes, and that is the lenght of the large partition.

        Once we have these two pieces of information, we can put the large
        partitions in the result. After the large parititions are done, we
        reduce the large partition size by one to obtain the small partition
        size, and we add the small partitions or empty node until total number
        of partitions reach k.

        O(N), where N is the number of nodes in the linked list.
        32 ms, 
        """
        if not head:
            return [head for _ in range(k)]
        dummy = ListNode(next=head)
        slow, fast = dummy, dummy
        slow_steps, fast_steps = 0, 0
        while True:
            for _ in range(k):
                if fast.next:
                    fast = fast.next
                    fast_steps += 1
                else:
                    break
            slow = slow.next
            slow_steps += 1
            if not fast.next:
                break
            fast_steps = 0
        res = [head]
        # number of partitions with slow_steps number of elements
        for _ in range(fast_steps - 1):
            dummy = slow
            for _ in range(slow_steps):
                slow = slow.next
            res.append(dummy.next)
            dummy.next = None
        # number of partitions with slow_steps - 1 number of elements
        for _ in range(k - fast_steps):
            dummy = slow
            for _ in range(slow_steps - 1):
                slow = slow.next
            res.append(dummy.next)
            dummy.next = None
        return res


class Solution2:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        """Official solution. It directly computes the small size partition and
        number of large parititons by counting the number of elements in the
        linked list. I don't know why I never thought about doing it this way.
        It's way simpler than the two pointer method.
        """
        N = 0
        node = head
        while node:
            node = node.next
            N += 1
        width, remain = divmod(N, k)

        res = []
        cur = head
        for i in range(k):
            front = cur
            for _ in range(width + int(i < remain) - 1):
                if cur:
                    cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            res.append(front)
        return res


sol = Solution2()
tests = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]),
    ([1, 2, 3], 5, [[1], [2], [3], [], []]),
    ([], 3, [[], [], []]),
    ([1], 3, [[1], [], []]),
]

for i, (ll, k, ans) in enumerate(tests):
    dummy = ListNode()
    node = dummy
    for val in ll:
        node.next = ListNode(val=val)
        node = node.next
    res = sol.splitListToParts(dummy.next, k)
    rlst = []
    for r in res:
        temp = []
        node = r
        while node:
            temp.append(node.val)
            node = node.next
        rlst.append(temp)
    if rlst == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {rlst}')
