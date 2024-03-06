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
public class Solution {
    public boolean hasCycle(ListNode head) {
        /*
        LeetCode 141
        
        0 ms, faster than 100.00% 
        */
        if (head == null)
            return false;
        ListNode slow = head;
        ListNode fast = head.next;
        while (fast != null && fast.next != null && slow != fast) {
            fast = fast.next.next;
            slow = slow.next;
        }
        return slow == fast;
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
