import java.util.*;
import java.util.stream.Stream;
import java.math.*;

/**
 * Definition for a binary tree node.
 */
class TreeNode {
   int val;
   TreeNode left;
   TreeNode right;
   TreeNode() {}
   TreeNode(int val) { this.val = val; }
   TreeNode(int val, TreeNode left, TreeNode right) {
       this.val = val;
       this.left = left;
       this.right = right;
   }
}


class Solution1 {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        /*
        LeetCode 19
        
        Technically this is O(N) time but we need O(N) space.
        */
        ListNode[] nodes = new ListNode[30];
        ListNode node = head;
        int i = 0;
        while (node != null) {
            nodes[i++] = node;
            node = node.next;
        }
        int j = i - n;
        if (j == 0)
            return head.next;
        nodes[j - 1].next = j < i - 1 ? nodes[j + 1] : null;
        return head;
    }
}


class Solution2 {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        /*
         * The standard solution is two pointers
        */
        ListNode right = head;
        for (int i = 0; i < n; i++)
            right = right.next;
        if (right == null)
            return head.next;
        ListNode left = head;
        while(right.next != null) {
            left = left.next;
            right = right.next;
        }
        left.next = left.next.next;
        return head;
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
