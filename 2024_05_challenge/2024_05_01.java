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
    public String reversePrefix(String word, char ch) {
        /*
         * LeetCode 2000
         *
         *
         */
        char[] wordArr = word.toCharArray();
        int i = 0;
        int j = word.indexOf(ch);
        while (i < j) {
            char tmp = wordArr[j];
            wordArr[j--] = wordArr[i];
            wordArr[i++] = tmp;
        }
        return String.valueOf(wordArr);
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
