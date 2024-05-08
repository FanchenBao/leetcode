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


class Solution1 {
    private ListNode[] helper(ListNode node) {
        ListNode[] next;
        if (node.next != null) 
            next = helper(node.next);
        else
            next = new ListNode[]{null, new ListNode(0)};
        int d = node.val * 2 + next[1].val;
        return new ListNode[]{new ListNode(d % 10, next[0]), new ListNode(d / 10)};
    }

    public ListNode doubleIt(ListNode head) {
        /*
         * LeetCode 2816
         *
         * I opt for a recursion solution. It can of course also be solved by
         * reverse the linked list and then reverse it back.
         *
         * O(N), 11 ms, faster than 22.34%
         */
        ListNode[] next = helper(head);
        if (next[1].val > 0)
            return new ListNode(next[1].val, next[0]);
        return next[0];
    }
}


class Solution2 {
    public ListNode doubleIt(ListNode head) {
        /*
         * This is the solution 5 from the official solution. It uses one
         * pointer to go left to right on the linked list. It just so happens
         * that if a digit is smaller or equal to 4, no matter how we double
         * the number, this digit will not create a carry. So, for each position
         * we check the value to its right to decide whether a carry will be
         * produced. If so, we add one (because the only possible carry is one)
         * otherwise, we don't add anything and just double the digit.
         *
         * The essence of this method is to change the value in-place. Thus,
         * although I don't like to change in place, we will do it here.
         *
         * O(N), 2 ms, faster than 100.00%
         */
        ListNode cur = head;
        ListNode res = head;
        if (cur.val * 2 >= 10)
            res = new ListNode(1, head);
        while (cur != null) {
            int d = cur.val * 2;
            if (cur.next != null && cur.next.val * 2 >= 10)
                d += 1;
            cur.val = d % 10;
            cur = cur.next;
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
