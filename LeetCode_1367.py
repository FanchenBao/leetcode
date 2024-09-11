# from pudb import set_trace; set_trace()
from typing import List, Optional
import math


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def get_lps(self, arr: List[int]) -> List[int]:
        """
        Produce the longest prefix suffix array for the given arr.
        lps[i] = max length of the prefix that matches the suffix ending at
        arr[i]
        """
        N = len(arr)
        lps = [0] * N
        cur_len = 0  # current max length of matching prefix
        i = 1
        while i < N:
            if arr[i] == arr[cur_len]:
                cur_len += 1
                lps[i] = cur_len
                i += 1
            elif cur_len > 0:
                cur_len = lps[cur_len - 1]
            else:  # cur_len is zero, impossible to match anything
                i += 1
        return lps

    def kmp_match(self, src: List[int], pat: List[int]) -> bool:
        """
        This is the implementation of KMP with list instead of string
        """
        M, N = len(src), len(pat)
        if M < N:
            return False
        lps = self.get_lps(pat)
        i = j = 0
        while (
            M - i >= N - j
        ):  # the condition is to check whether there is enough src to match pat
            if src[i] == pat[j]:
                i += 1
                j += 1
                if j == N:
                    return True
            elif j > 0:
                j = lps[j - 1]  # the next ele in pat to match src[i]
            else:
                i += 1  # j is zero and there is no match.
        return False

    def dfs(self, node: TreeNode, path: List[int], linkedlist: List[int]) -> bool:
        res = False
        path.append(node.val)
        if not node.left and not node.right:
            res = self.kmp_match(path, linkedlist)
        if node.left:
            res |= self.dfs(node.left, path, linkedlist)
        if node.right:
            res |= self.dfs(node.right, path, linkedlist)
        path.pop()
        return res

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        """
        In this solution, we will use KMP substring matching algorithm to
        more quickly determine whether the linked list pattern is a subarray
        of any path in the tree.

        This is most likely not the final version of KMP, but it is an faster
        way of matching subarray.

        184 ms, faster than 5.01%
        """
        linkedlist = []
        listnode = head
        while listnode:
            linkedlist.append(listnode.val)
            listnode = listnode.next
        if not root:
            return False
        return self.dfs(root, [], linkedlist)


class Solution2:
    def get_lps(self, arr: List[int]) -> List[int]:
        """
        Produce the longest prefix suffix array for the given arr.
        lps[i] = max length of the prefix that matches the suffix ending at
        arr[i]
        """
        N = len(arr)
        lps = [0] * N
        cur_len = 0  # current max length of matching prefix
        i = 1
        while i < N:
            if arr[i] == arr[cur_len]:
                cur_len += 1
                lps[i] = cur_len
                i += 1
            elif cur_len > 0:
                cur_len = lps[cur_len - 1]
            else:  # cur_len is zero, impossible to match anything
                i += 1
        return lps

    def dfs(
        self, node: Optional[TreeNode], linkedlist: List[int], idx: int, lps: List[int]
    ) -> bool:
        if idx == len(linkedlist):
            return True
        if not node:
            return False
        if node.val == linkedlist[idx]:
            return self.dfs(node.left, linkedlist, idx + 1, lps) or self.dfs(
                node.right, linkedlist, idx + 1, lps
            )
        if idx > 0:
            return self.dfs(node, linkedlist, lps[idx - 1], lps)
        return self.dfs(node.left, linkedlist, idx, lps) or self.dfs(
            node.right, linkedlist, idx, lps
        )

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        """
        Second version of KMP where we perform the match as we go through the
        DFS. In fact, this makes a lot of sense, because the matching algorithm
        always goes through the source array one by one, the same as DFS. The
        benefit of this is that we don't have to go through the path a second
        time for the matching.

        60 ms, faster than 85.29%
        """
        if not root:
            return False
        linkedlist = []
        listnode = head
        while listnode:
            linkedlist.append(listnode.val)
            listnode = listnode.next
        lps = self.get_lps(linkedlist)
        return self.dfs(root, linkedlist, 0, lps)


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
