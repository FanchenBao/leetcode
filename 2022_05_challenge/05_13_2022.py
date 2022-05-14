# from pudb import set_trace; set_trace()
from typing import List



# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution1:
    def connect(self, root: 'Node') -> 'Node':
        """LeetCode 117

        This is the naive way to do this. BFS. We can establish the link of
        the next pointers by building up the queue for the next layer.

        O(N), 63 ms, faster than 55.92%
        """
        if not root:
            return root
        queue = [root]
        while queue:
            temp = []
            for node in queue:
                if node.left:
                    if temp:
                        temp[-1].next = node.left
                    temp.append(node.left)
                if node.right:
                    if temp:
                        temp[-1].next = node.right
                    temp.append(node.right)
            queue = temp
        return root


class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        """O(1) space. We work always on two adjacent layers. top and bot. We
        keep the tail node for the top and bot layer, and we walk them both to
        the right.
        """
        if not root:
            return root
        top = root
        bot_head = bot = None
        while top:
            while top:
                l, r = top.left, top.right
                if l:
                    l.next = r
                if bot:
                    bot.next = l or r
                else:
                    bot_head = bot = l or r
                while bot and bot.next:
                    bot = bot.next
                top = top.next
            top = bot_head
            bot = None
        return root


        

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
