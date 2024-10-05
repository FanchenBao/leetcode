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
    public long dividePlayers(int[] skill) {
        /*
         * LeetCode 2491
         *
         * Find the target skill for the sum of two people. Create a counter
         * for all the skills. Then go through each skill and examine if a
         * match can be found. Pay attention to the scenario where the two
         * skills are the same.
         *
         * O(N), 4 ms, faster than 94.96%
         */
        int[] counter = new int[1001];
        int total = 0;
        int maxSkill = 0;
        for (int s : skill) {
            counter[s]++;
            total += s;
            maxSkill = Math.max(maxSkill, s);
        }
        if (total % (skill.length / 2) != 0)
            return -1;
        int tgt = total / (skill.length / 2);
        long res = 0;
        for (int s = 1; s <= maxSkill; s++) {
            if (counter[s] > 0) {
                int m = tgt - s;
                if (counter[m] != counter[s] || (m == s && counter[s] % 2 != 0))
                    return -1;
                res += (long)s * (long)m * (m == s ? (long)counter[s] / 2 : (long)counter[s]);
                counter[s] = 0;
                counter[m] = 0;
            }
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
