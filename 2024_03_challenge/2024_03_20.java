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
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        /*
        LeetCode 1669
        
        Simple linked list maneuver.
        
        O(N), 2 ms, faster than 40.65%
        */
        ListNode node = list1;
        int idx = 0;
        ListNode l1prea = new ListNode();
        ListNode l1b = new ListNode();
        while (node != null) {
            if (idx == a - 1)
                l1prea = node;
            if (idx == b + 1) {
                l1b = node;
                break;
            }
            node = node.next;
            idx++;
        }
        l1prea.next = list2;
        node = list2;
        while (node.next != null)
            node = node.next;
        node.next = l1b;
        return list1;
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
