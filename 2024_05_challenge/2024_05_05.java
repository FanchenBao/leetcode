import java.util.*;
import java.util.stream.Stream;
import java.math.*;

/**
 * Definition for a binary tree node.
 */
//class TreeNode {
//    int val;
//    TreeNode left;
//    TreeNode right;
//    TreeNode() {}
//    TreeNode(int val) { this.val = val; }
//    TreeNode(int val, TreeNode left, TreeNode right) {
//        this.val = val;
//        this.left = left;
//        this.right = right;
//    }
//}

class Solution1 {
    public void deleteNode(ListNode node) {
        /*
         * LeetCode 237
         *
         * Since we are not given the head node, it is impossible to actually
         * remove the node. But what we can do is to shift the values left-
         * ward.
         *
         * O(N), 0 ms, faster than 100.00%
         */
        ListNode cur = node;
        while (cur != null && cur.next != null) {
            cur.val = cur.next.val;
            if (cur.next.next == null)
                cur.next = null;
            cur = cur.next;
        }
    }
}


class Solution2 {
    public void deleteNode(ListNode node) {
        /*
         * There is no need to even shift the values for everything. All we
         * need to do is to shift one of the values, and then delete the node
         * right next to the current node.
         *
         * This is from the official solution.
         * O(1)
         */
        node.val = node.next.val;
        node.next = node.next.next;
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
