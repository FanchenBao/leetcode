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
    public ListNode[] splitListToParts(ListNode head, int k) {
        /*
         * LeetCode 725
         *
         * The base length of each split linked list is N / k. If N / k has
         * remainder, they will be evenly split among the first few split
         * linked lists
         *
         * O(N), 0 ms, faster than 100.00%
         */
        int N = 0;
        ListNode node = head;
        while (node != null) {
            N++;
            node = node.next;
        }
        int each = N / k;
        int rem = N % k;
        ListNode[] res = new ListNode[k];
        node = head;
        for (int i = 0; i < k; i++) {
            res[i] = node;
            int cnt = each + (rem > 0 ? 1 : 0);
            while (cnt > 1 && node != null) {
                node = node.next;
                cnt--;
            }
            if (node != null) {
                ListNode tmp = node.next;
                node.next = null;
                node = tmp;
            }
            rem--;
        }
        return res;
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
