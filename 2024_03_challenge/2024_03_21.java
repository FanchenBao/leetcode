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

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution1 {
    public ListNode reverseList(ListNode head) {
        /*
         * LeetCode 206
         *
         * Iterative approach
         */
        ListNode pre = null;
        ListNode cur = head;
        while (cur != null) {
            ListNode tmp = cur.next;
            cur.next = pre;
            pre = cur;
            cur = tmp;
        }
        return pre;
    }
}


class Solution {
    ListNode revHead;

    private ListNode helper(ListNode node) {
        if (node.next == null) {
            revHead = node; // last node
            return node;
        }
        ListNode tail = helper(node.next);
        tail.next = node;
        node.next = null;
        return node;
    }

    public ListNode reverseList(ListNode head) {
        /*
         * LeetCode 206
         *
         * Recursive approach
         */
        if (head == null)
            return head;
        helper(head);
        return revHead;
    }
}


class Solution3 {
    public ListNode reverseList(ListNode head) {
        /*
         * LeetCode 206
         *
         * Better recursion
         */
        if (head == null || head.next == null)
            return head;
        ListNode tail = head.next;
        ListNode revHead = reverseList(head.next);
        tail.next = head;
        head.next = null;
        return revHead;
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
