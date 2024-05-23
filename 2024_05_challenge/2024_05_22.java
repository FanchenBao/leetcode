import java.util.*;
import java.util.stream.Stream;
import java.math.*;
import java.sql.Array;

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
    Map<Integer, List<List<String>>> memo = new HashMap<>();

    private boolean isPalindrome(int lo, int hi, String s) {
        int i = lo;
        int j = hi;
        while (i < j) {
            if (s.charAt(i++) != s.charAt(j--))
                return false;
        }
        return true;
    }

    private List<List<String>> dp(int idx, String s) {
        if (idx == s.length()) {
            List<List<String>> res = new ArrayList<>();
            res.add(new ArrayList<>());
            return res;
        }
        if (memo.containsKey(idx))
            return memo.get(idx);
        memo.put(idx, new ArrayList<>());
        for (int i = idx; i < s.length(); i++) {
            if (isPalindrome(idx, i, s)) {
                for (List<String> nex : dp(i + 1, s)) {
                    List<String> cur = new ArrayList<>();
                    cur.add(s.substring(idx, i + 1));
                    cur.addAll(nex);
                    memo.get(idx).add(cur);
                }
            }
        }
        return memo.get(idx);
    }
    public List<List<String>> partition(String s) {
        /*
         * DP solution where dp(i) return a list of palindromic partitions
         * in substring s[i:]
         *
         * O(N^2 * (N + K)), 10 ms, faster than 25.47% 
         */
        return dp(0, s);
    }
}


class Solution2 {
    List<List<String>> res = new ArrayList<>();

    private boolean isPalindrome(int lo, int hi, String s) {
        int i = lo;
        int j = hi;
        while (i < j) {
            if (s.charAt(i++) != s.charAt(j--))
                return false;
        }
        return true;
    }

    private void backtrack(int idx, String s, List<String> cur) {
        if (idx == s.length()) {
            res.add(new ArrayList<>(cur));
        } else {
            for (int i = idx; i < s.length(); i++) {
                if (isPalindrome(idx, i, s)) {
                    cur.add(s.substring(idx, i + 1));
                    backtrack(i + 1, s, cur);
                    cur.remove(cur.size() - 1);
                }
            }
        }
    }
    public List<List<String>> partition(String s) {
        /*
         * Backtracking, 7 ms, faster than 96.51%
         */
        backtrack(0, s, new ArrayList<>());
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
