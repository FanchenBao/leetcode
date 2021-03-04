# from pudb import set_trace; set_trace()
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def reverse(self, head: ListNode) -> ListNode:
        """Reverse a linked-list with the given head"""
        left, right = None, head
        while right:
            temp = right.next
            right.next = left
            left = right
            right = temp
        return left

    def find_loop_begin(self, head: ListNode) -> ListNode:
        """Find the beginning node of a loop in a linked list with the
        given head. If no loop exists, return None"""
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                break
        else:
            return None  # no loop
        fast = head
        while fast is not slow:
            fast = fast.next
            slow = slow.next
        return fast

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """LeetCode 160

        This solution first reverses one of the linked list, obtain its new
        head, let's call it "tail", and then connect headA to headB. This way,
        we create a loop in the new linked structure with the head being "tail".
        Now the problem becomes to find the start node of the loop. We have
        solved this problem before. Finally, we undo the actions that create the
        loop.

        I would never have come up with this solution had I not solved the loop
        problem in the first place. So in a sense, this is a little bit unfair,
        because this solution asks a candidate to solve basically two problems
        in one. It's pretty hard.

        O(N) with O(1) space. 160 ms, 76% ranking.
        """
        if not headA or not headB:
            return None
        # create loop
        tail = self.reverse(headA)
        headA.next = headB
        target = self.find_loop_begin(tail)
        # undo loop
        headA.next = None
        self.reverse(tail)
        return target



class Solution2:
    def find_loop_begin(self, head: ListNode) -> ListNode:
        """Find the beginning node of a loop in a linked list with the
        given head. If no loop exists, return None"""
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                break
        else:
            return None  # no loop
        fast = head
        while fast is not slow:
            fast = fast.next
            slow = slow.next
        return fast

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """This is better than my original, because there is NO NEED to reverse
        anyone. We can create a loop by linking the tail of one list to the head
        of the other list. The rest is the same.
        """
        if not headA or not headB:
            return None
        tail = headA
        while tail.next:  # find the tail
            tail = tail.next
        tail.next = headB  # create loop
        target = self.find_loop_begin(headA)
        tail.next = None  # undo loop
        return target
        

class Solution3:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """This is the official O(N) time O(1) space solution. The intuition is
        actually quite simple. We have two lists. We know that the shared part
        must be of the same size on both lists. Therefore, we only need to find
        the start of both lists that guarantee that the remanining lists have
        the same length. For instance, given A: 1, 2 ,3, 4 and B: 5, 3, 4. We
        know A has length 4 and B has length 3. Then the shared part must exist
        in the last three nodes. So we move the starting node on A to the second
        node, and move the starting node on B to the head. Then we can just
        iterate one by one until we find the matching.

        The solution also offers a brilliant implementation of this solution,
        which I am going to code below.

        For detailed explanation, refer back to the solution:
        https://leetcode.com/problems/intersection-of-two-linked-lists/solution/
        """
        a, b = headA, headB
        while a is not b:
            a = headB if a is None else a.next
            b = headA if b is None else b.next
        return a



sol = Solution3()
tests = [
    ('abab', True),
    ('aba', False),
    ('abcabcabcabc', True),
    ('abcabcababcabcab', True),
    ('abcbac', False),
    ('aabaabaab', True),
    ('a', False),
    ('aaaaaaa', True),
    ('aaaaab', False),
]

for i, (s, ans) in enumerate(tests):
    res = sol.repeatedSubstringPattern(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
