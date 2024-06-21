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
    public int maxDistance(int[] position, int m) {
        /*
         * LeetCode 1552
         *
         * Binary search for min-max problem. We try a magnetic force, then
         * we distribute the m balls with the distance between every two balls
         * as close to the current magnetic force as possible. If the
         * distribution is possible, we can increase the magnetic force.
         * Otherwise, we decrease.
         *
         * O(NlogN), 43 ms, faster than 58.58%
         */
        Arrays.sort(position);
        long lo = 1;
        long hi = position[position.length - 1] - position[0] + 1;
        while (lo < hi) {
            long mid = (lo + hi) / 2;
            int pre = position[0]; // put the first ball at the first position
            int rem = m - 1;
            for (int i = 1; i < position.length; i++) {
                if (position[i] >= pre + mid) {
                    pre = position[i];
                    rem--;
                    if (rem == 0)
                        break;
                }
            }
            if (rem == 0)
                lo = mid + 1;
            else
                hi = mid;
        }
        return (int)lo - 1;
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
