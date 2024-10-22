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
    int res = 0;
    Set<String> seen = new HashSet<>();

    private void helper(String s, int idx) {
        if (idx == s.length()) {
            res = Math.max(res, this.seen.size());
        } else {
            for (int i = idx; i < s.length(); i++) {
                if (this.seen.size() + s.length() - i <= this.res)
                    break;
                String cur = s.substring(idx, i + 1);
                if (!this.seen.contains(cur)) {
                    this.seen.add(cur);
                    helper(s, i + 1);
                    this.seen.remove(cur); // backtrack
                }
            }
        }
    }

    public int maxUniqueSplit(String s) {
        /*
         * LeetCode 1593
         *
         * Backtrack with O(N * 2^N). Basically we try all combinations of
         * splitting the string and return the max count of substrings among
         * them.
         *
         * 2 ms, faster than 99.35%
         */
        helper(s, 0);
        return this.res;
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
