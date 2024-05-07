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
    private ListNode reverse(ListNode head) {
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

    public ListNode removeNodes(ListNode head) {
        /*
         * LeetCode 2487
         *
         * Reverse the linked list, run monotonic increasing stack, then reverse
         * the linked list back.
         *
         * O(N) 7 ms, faster than 80.63%
         */
        ListNode newHead = reverse(head);
        ListNode cur = newHead;
        while (cur != null && cur.next != null) {
            if (cur.val > cur.next.val)
                cur.next = cur.next.next;
            else
                cur = cur.next;
        }
        return reverse(newHead);
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
