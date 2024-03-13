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


 public class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }
 

class Solution1 {
    public ListNode removeZeroSumSublists(ListNode head) {
        /*
         * LeetCode 1171
         *
         * Use stack.
         *
         * O(N), 6 ms, faster than 10.28%
         */
        Stack<ListNode> stack = new Stack<>();
        Set<Integer> seen = new HashSet<>();
        Stack<Integer> presum = new Stack<>();
        ListNode dummy = new ListNode(0, head);
        stack.add(dummy);
        seen.add(0);
        presum.add(0);
        // prefix sum
        ListNode node = head;
        while (node != null) {
            int curSum = presum.peek() + node.val;
            if (seen.contains(curSum)) {
                while (presum.peek() != curSum) {
                    seen.remove(presum.pop());
                    stack.pop();
                }
                stack.peek().next = node.next;
            } else {
                seen.add(curSum);
                presum.add(curSum);
                stack.add(node);
            }
            node = node.next;
        }
        return dummy.next;
    }
}


class Solution2 {
    public ListNode removeZeroSumSublists(ListNode head) {
        /*
         * Create a new array from scratch
         *
         */
        int[][] presum = new int[1001][2];
        int i = 1;
        while (head != null) {
            int cur = head.val + presum[i - 1][0];
            boolean hasSeen = false;
            for (int j = i - 1; j >= 0; j--) {
                if (presum[j][0] == cur) {
                    i = j + 1;
                    hasSeen = true;
                    break;
                }
            }
            if (!hasSeen) {
                presum[i][0] = cur;
                presum[i][1] = head.val;
                i++;
            }
            head = head.next;
        }
        if (i == 1)
            return null;
        ListNode newHead = new ListNode(presum[1][1]);
        ListNode node = newHead;
        for (int j = 2; j < i; j++) {
            node.next = new ListNode(presum[j][1]);
            node = node.next;
        }
        return newHead;
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
