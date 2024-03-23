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
        while (head != null) {
            ListNode tmp = head.next;
            head.next = pre;
            pre = head;
            head = tmp;
        }
        return pre;
    }

    public boolean isPalindrome(ListNode head) {
        /*
        LeetCode 234
        
        Reverse the second half. It is O(N) time and O(1) space
        but at the cost of modifying the input linked list.

        4 ms, faster than 82.66%
        */
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        ListNode revHead = reverse(slow);
        ListNode node = head;
        while (revHead != null) {
            if (node.val != revHead.val)
                return false;
            node = node.next;
            revHead = revHead.next;
        }
        return true;
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
