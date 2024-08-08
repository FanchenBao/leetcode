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
    String[] singleDigits = new String[] {"", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine "};
    String[] teens = new String[] {"Ten ", "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "};
    String[] tys = new String[] {"", "Ten ", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "};
    String[] triples = new String[] {"", "Thousand ", "Million ", "Billion "};

    private String handleThreeDigits(int num) {
        StringBuilder s = new StringBuilder();
        int i = num / 100;
        int j = num % 100;
        if (i > 0)
            s.append(singleDigits[i] + "Hundred ");
        if (j >= 10 && j <= 19) {
            s.append(teens[j % 10]);
        } else {
            i = j / 10;
            if (i > 0)
                s.append(tys[i]);
            j = j % 10;
            if (j > 0)
                s.append(singleDigits[j]);
        }
        return s.toString();
    }

    public String numberToWords(int num) {
        /*
         * LeetCode 273
         *
         * I think this is not a bad problem, because it is very realistc.
         * Plus, it requires one to think about how the algorithm should be
         * designed.
         *
         * 3 ms, faster than 69.21%
         */
        if (num == 0)
            return "Zero";
        StringBuilder res = new StringBuilder();
        int i = 0;
        while (num > 0) {
            String t = handleThreeDigits(num % 1000);
            if (!t.isEmpty())
                res.insert(0, t + triples[i]);
            i++;
            num /= 1000;
        }
        res.setLength(res.length() - 1);
        return res.toString();
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
