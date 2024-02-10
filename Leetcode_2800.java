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
    private String merge(String a, String b) {
        if (a.contains(b))
            return a;
        for (int i = Math.max(0, a.length() - b.length()); i < a.length(); i++) {
            String suba = a.substring(i);
            String subb = b.substring(0, a.length() - i);
            if (suba.equals(subb))
                return a + b.substring(a.length() - i);
        }
        return a + b;
    }

    public String minimumString(String a, String b, String c) {
        /*
         * We are brute forcing this problem.
         *
         * 40 ms, faster than 73.42%
         */
        String res = null;
        String[][] pat = new String[][]{{a,b,c},{b,a,c},{a,c,b},{c,a,b},{b,c,a},{c,b,a}};
        for (String[] p : pat) {
            String s = merge(merge(p[0], p[1]), p[2]);
            if (res == null || res.length() > s.length() || (res.length() == s.length() && s.compareTo(res) < 0))
                res = s;
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
