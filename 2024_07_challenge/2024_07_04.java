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
//
/**
 * Definition for singly-linked list.
 */
public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}


class Solution {
    public ListNode mergeNodes(ListNode head) {
        /*
         * LeetCode 2181
         *
         * Standard procedure of linkedlist
         *
         * O(N), 5 ms, faster than 84.77%
         */
        ListNode dummy = new ListNode();
        ListNode resNode = dummy;
        ListNode loopNode = head.next;
        int sum = 0;
        while (loopNode != null) {
            if (loopNode.val != 0) {
                sum += loopNode.val;
            } else {
                resNode.next = new ListNode(sum);
                resNode = resNode.next;
                sum = 0;
            }
            loopNode = loopNode.next;
        }
        return dummy.next;
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
