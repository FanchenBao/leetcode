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
 */
class ListNode {
     int val;
     ListNode next;
     ListNode() {}
     ListNode(int val) { this.val = val; }
     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }
 
class Solution {
    private int gcd(int a, int b) {
        if (b > 0)
            return gcd(b, a % b);
        return a;
    }

    public ListNode insertGreatestCommonDivisors(ListNode head) {
        /*
         * LeetCode 2807
         *
         * Just insert the GCD along the way.
         *
         * O(N), 2 ms, faster than 71.11%
         */
        ListNode dummy = new ListNode(0, head);
        ListNode p1 = head;
        ListNode p2 = head.next;
        while (p2 != null) {
            int g = gcd(p1.val, p2.val);
            p1.next = new ListNode(g);
            p1.next.next = p2;
            p1 = p2;
            p2 = p2.next;
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
