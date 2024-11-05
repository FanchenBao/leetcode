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
    public String compressedString(String word) {
        /*
         * LeetCode 3163
         *
         * Just count the frequency of each letter in word from left to right
         * and compress them into the result. Seems very simple.
         *
         * O(N), 22 ms, faster than 46.61%
         */
        StringBuilder res = new StringBuilder();
        int cnt = 1;
        for (int i = 1; i < word.length(); i++) {
            if (word.charAt(i) == word.charAt(i - 1) && cnt < 9) {
                cnt++;
            } else {
                res.append(cnt).append(word.charAt(i - 1));
                cnt = 1;
            }
        }
        return res.append(cnt).append(word.charAt(word.length() - 1)).toString();
    }
}


class Solution2 {
    public String compressedString(String word) {
        /*
         * Try making it faster
         *
         * 14 ms, faster than 98.31%
         */
        int N = word.length();
        char[] res = new char[2 * N];
        int cnt = 1;
        int j = 0;
        for (int i = 1; i < word.length(); i++) {
            if (word.charAt(i) == word.charAt(i - 1) && cnt < 9) {
                cnt++;
            } else {
                res[j++] = (char)('0' + cnt);
                res[j++] = word.charAt(i - 1);
                cnt = 1;
            }
        }
        res[j++] = (char)('0' + cnt);
        res[j++] = word.charAt(N - 1);
        return new String(res, 0, j);
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
