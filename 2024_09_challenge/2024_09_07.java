import java.util.*;
import java.util.stream.Stream;
import java.math.*;

/**
 * Definition for singly-linked list.
 */
class ListNode {
 int val;
 ListNode next;
 ListNode() {}
 ListNode(int val) { this.val = val; }
 ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
 
/**
 * Definition for a binary tree node.
 */
class TreeNode {
 int val;
 TreeNode left;
 TreeNode right;
 TreeNode() {}
 TreeNode(int val) { this.val = val; }
 TreeNode(int val, TreeNode left, TreeNode right) {
     this.val = val;
     this.left = left;
     this.right = right;
 }
}
 
class Solution1 {
    private boolean isSubArray(List<Integer> small, List<Integer> big) {
        if (small.size() > big.size())
            return false;
        for (int i = 0; i < big.size(); i++) {
            int j = 0;
            while (j < small.size() && i + j < big.size() && small.get(j) == big.get(i + j))
                j++;
            if (j == small.size())
                return true;
        }
        return false;
    }

    private boolean checkPath(TreeNode node, List<Integer> listVals, List<Integer> path) {
        if (node == null) {
            if (isSubArray(listVals, path))
                return true;
            return false;
        }
        path.add(node.val);
        if (checkPath(node.left, listVals, path) || checkPath(node.right, listVals, path))
            return true;
        path.remove(path.size() - 1);
        return false;
    }

    public boolean isSubPath(ListNode head, TreeNode root) {
        /*
         * LeetCode 1367
         *
         * First get the list of vals from linked list, then DFS root and check
         * whether the linked list vals is a subarray of a path in the tree.
         *
         * The implementation of subarray check is naive in this solution,
         * which takes O(MN) time. There is a better way called KMP that can
         * check subarray (KMP is usde for substring matching, but we can use
         * it here for checking subarray) in O(M + N). However, I am NOT going
         * to implement KMP. Too complicated.
         *
         * 66 ms, faster than 5.11%
         */
        List<Integer> listVals = new ArrayList<>();
        ListNode node = head;
        while (node != null) {
            listVals.add(node.val);
            node = node.next;
        }
        return checkPath(root, listVals, new ArrayList<>());
    }
}


class Solution2 {
    private boolean solve(ListNode lnode, TreeNode tnode, ListNode head) {
        if (lnode == null)
            return true;
        if (tnode == null)
            return false;
        if (lnode.val == tnode.val) {
            if (solve(lnode.next, tnode.left, head) || solve(lnode.next, tnode.right, head))
                return true;
        }
        if (head.val == tnode.val) {
            if (solve(head.next, tnode.left, head) || solve(head.next, tnode.right, head))
                return true;
        }
        return false;
    }

    public boolean isSubPath(ListNode head, TreeNode root) {
        /*
         * This approach uses a little bit inspiration from KMP, but it is NOT
         * exactly KMP. So I expect it to be faster than solution1, but in the
         * worst case, its complexity should still be O(MN)
         */
        return solve(head, root, head);
    }
}

class Main{
    public static void main(String[] args) {
        String s = "acbbaca";
        String t = "aba";
        Solution sol = new Solution();
        System.out.println(sol.minWindow(s, t));
    }
}
