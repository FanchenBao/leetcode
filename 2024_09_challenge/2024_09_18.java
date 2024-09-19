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
    public String largestNumber(int[] nums) {
        /*
         * LeetCode 179 Fail
         *
         * The key to the problem is to prove that if we sort the string version
         * of nums with the rule that A comes before B if AB > BA, where AB
         * and BA are concatenation of string and the comparison is string
         * comparison.
         *
         * To prove this, we must prove transitivity, i.e. if A > B and B > C,
         * then A > C. I will not repeat the proof here. One can refer to the
         * official solution, but suffice it to say that a little bit math
         * is needed to make the proof work.
         *
         * Once the transitivity is proven, we can easily use proof of
         * contradiction to show that the num strings sorted this way always
         * produce the largest number.
         *
         * 6 ms, faster than 54.52%
         */
        int N = nums.length;
        String[] numStrs = new String[N];
        for (int i = 0; i < N; i++)
            numStrs[i] = String.valueOf(nums[i]);
        Arrays.sort(numStrs, (a, b) -> -(a + b).compareTo(b + a));
        if (numStrs[0] == "0")
            return "0";
        StringBuilder res = new StringBuilder();
        for (String s : numStrs)
            res.append(s);
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
