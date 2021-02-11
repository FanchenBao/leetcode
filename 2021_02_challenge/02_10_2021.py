# from pudb import set_trace; set_trace()
from typing import List, Dict


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution1:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """A very straightforward solution, where we use a mapping to establish
        the connection between the original node and its copy. This way, when
        we need to create the random link in the copy nodes, we know exactly
        which copy node corresponds to the original node that is the target of
        the random link.

        O(N), 32 ms, 87% ranking.
        """
        ori_copy: Dict = {}
        dummy = Node(0)
        node, copy = head, dummy
        while node:  # copy the linked list, no worry about random link
            copy.next = Node(node.val)
            copy = copy.next
            ori_copy[id(node)] = copy
            node = node.next

        node, copy = head, dummy.next
        while node:  # traverse the linked list, fill in the random link
            rand_node = node.random
            if rand_node is not None:
                copy.random = ori_copy[id(rand_node)]
            node = node.next
            copy = copy.next

        return dummy.next


class Solution2:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """One pass"""
        ori_copy: Dict = {id(None): None}
        dummy = Node(0)
        node, copy = head, dummy
        while node:
            # copy the next node
            copy.next = ori_copy.get(id(node), Node(node.val))
            copy = copy.next
            ori_copy[id(node)] = copy
            # copy the random node
            copy.random = ori_copy.get(
                id(node.random),
                Node(node.random.val) if node.random else None,
            )
            ori_copy[id(node.random)] = copy.random
            node = node.next
        return dummy.next


class Solution3:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """O(1) space, very very smart
        Reference: https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)
        """
        if not head:
            return None
        # Create copy nodes that are right next to the original nodes
        node = head
        while node:
            nn = node.next
            node.next = Node(node.val)
            node.next.next = nn
            node = nn
        # Copy random links
        node = head
        while node:
            rn = node.random
            if rn:
                node.next.random = rn.next
            node = node.next.next
        # Split origin and copy
        copy_head = head.next
        node, copy = head, copy_head
        while node:
            node.next = copy.next
            node = node.next
            copy.next = node.next if node else None
            copy = copy.next
        return copy_head


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
