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

class Solution {
    private ListNode reverse(ListNode node) {
        ListNode pre = null;
        while (node != null) {
            ListNode tmp = node.next;
            node.next = pre;
            pre = node;
            node = tmp;
        }
        return pre;
    }

    public void reorderList(ListNode head) {
        /*
         * LeetCode 143
         *
         * Slow and fast nodes to find the mid-point, reverse the second half
         * and then interweave the second half into the first half.
         *
         * O(N), 2 ms, faster than 88.69%
         */
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        ListNode node2 = reverse(slow.next);
        slow.next = null;
        ListNode node1 = head;
        while (node2 != null) {
            ListNode tmp1 = node1.next;
            ListNode tmp2 = node2.next;
            node1.next = node2;
            node2.next = tmp1;
            node1 = tmp1;
            node2 = tmp2;
        }
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
