# from pudb import set_trace; set_trace()
from typing import List



# Definition for a Node.
class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution1:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """LeetCode 138

        I didn't realize that the values in the nodes are not unique. Thus, we
        need to use the original node's address as keys to a hashmap. In addi-
        tion, we use a dummy node to simplify the procedure.

        O(N), 51 ms, 54% ranking.
        """
        dummy = Node(-1, next=head)
        node = dummy
        hashmap = {id(dummy): Node(-1)}
        while node:
            if node.next:
                k1 = id(node.next)
                if k1 not in hashmap:
                    hashmap[k1] = Node(node.next.val)
                hashmap[id(node)].next = hashmap[k1]
            if node.random:
                k2 = id(node.random)
                if k2 not in hashmap:
                    hashmap[k2] = Node(k2)
                hashmap[id(node)].random = hashmap[k2]
            node = node.next
        return hashmap[id(dummy)].next


class Solution2:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """This is the solution from some discussio that I copied when I did
        this problem a year ago. The key insight is that instead of using a
        hashmap to create the connection between the original node and the
        copied node, we can simply place the copied node right next to the
        original node. This way, we create a natural connection between the
        two.

        O(N) time and O(1) space. 40 ms, 81% ranking.
        """
        # copy the list only considering the next pointer
        node = head
        while node:
            temp = node.next
            node.next = Node(node.val)
            node.next.next = temp
            node = temp
        # copy the random pointer
        node = head
        while node:
            if node.random:
                rn = node.random
                node.next.random = rn.next
            node = node.next.next
        # split the two
        dummy = Node(-1)
        copy = dummy
        node = head
        while node:
            copy.next = node.next
            node.next = node.next.next
            node = node.next
            copy = copy.next
        return dummy.next



        

# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
