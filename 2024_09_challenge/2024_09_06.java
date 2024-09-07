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



// Definition for singly-linked list.
class ListNode {
  int val;
  ListNode next;
  ListNode() {}
  ListNode(int val) { this.val = val; }
  ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode modifiedList(int[] nums, ListNode head) {
        /*
         * LeetCode 3217
         *
         * Standard linked list
         * 21 ms, faster than 45.83%
         */
        Set<Integer> numSet = new HashSet<>();
        for (int n : nums)
            numSet.add(n);
        ListNode dummy = new ListNode(0, head);
        ListNode node = head;
        ListNode pre = dummy;
        while (node != null) {
            if (numSet.contains(node.val)) {
                pre.next = node.next;
            } else {
                pre = pre.next;
            }
            node = node.next;
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
