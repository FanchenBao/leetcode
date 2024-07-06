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
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        /*
         * LeetCode 2058
         *
         * Since I tried to do this with O(1) space, the logic is a bit
         * convoluted. One important thing to note is that preIdx is set when
         * a critical node is encountered. Yet preVal is set every single node
         * visit.
         *
         * O(N), 4 ms, faster than 100.00%
         */
        int idx = 1;
        int first = -1;
        int preVal = head.val;
        int preIdx = -1;
        ListNode node = head.next;
        int[] res = new int[]{-1, -1};
        while (node.next != null) {
            if ((node.val > preVal && node.val > node.next.val) || (node.val < preVal && node.val < node.next.val)) {
                if (first < 0)
                    first = idx;
                if (preIdx >= 0) {
                    int d = idx - preIdx;
                    res[0] = res[0] < 0 ? d : Math.min(res[0], d);
                }
                preIdx = idx;
            }
            preVal = node.val;
            node = node.next;
            idx++;
        }
        if (preIdx > first)
            res[1] = preIdx - first;
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
