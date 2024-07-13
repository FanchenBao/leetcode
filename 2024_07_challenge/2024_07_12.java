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
    private int[] remove(String pat, char[] sArr, int sLen, int s) {
        int i = 1; // i points to the next write position
        int score = 0;
        for (int j = 1; j < sLen; j++) {
            // j points to the next read position
            if (i > 0 && sArr[i - 1] == pat.charAt(0) && sArr[j] == pat.charAt(1)) {
                score += s;
                i--;
            } else {
                sArr[i++] = sArr[j];
            }
        }
        return new int[]{score, i};
    }

    public int maximumGain(String s, int x, int y) {
        /*
         * LeetCode 1717 (Fail)
         *
         * Still not fully convinced of the greedy proof, but it is too late
         * now and I really cannot think straight. I'll let this pass.
         *
         * I am also implementing the second solution in the official solution
         * where we use O(1) extra space.
         *
         * O(N), 30 ms, faster than 84.85% 
         */
        int res = 0;
        String patX = "ab";
        String patY = "ba";
        if (x < y) {
            patX = "ba";
            patY = "ab";
        }
        char[] sArr = s.toCharArray();
        int[] removeX = remove(patX, sArr, s.length(), Math.max(x, y));
        res += removeX[0];
        int[] removeY = remove(patY, sArr, removeX[1], Math.min(x, y));
        return res + removeY[0];
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
