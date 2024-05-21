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
    public int subsetXORSum(int[] nums) {
        /*
         * LeetCode 1863
         *
         * Essentially finding all the combinations within array nums.
         * We use the method of bitmask to obtain each combination without
         * going through recursion.
         *
         * O(2^N), 5 ms, faster than 35.74%
         */
        int N = nums.length;
        int res = 0;
        for (int i = 0; i <= (1 << N) - 1; i++) {
            int s = 0;
            for (int j = 0; j < N; j++) {
                if ((i & (1 << j)) > 0)
                    s ^= nums[j];
            }
            res += s;
        }
        return res;
    }
}


class Solution2 {
    public int subsetXORSum(int[] nums) {
        /*
         * This is the O(N) solution. Its proof is provided by
         * https://leetcode.com/problems/sum-of-all-subset-xor-totals/discuss/1211182/One-liner-+-Bitmask/1002314
         *
         * The gist is to count the number of times a specific bit among all
         * elements of nums contribute to the final sum.
         *
         * If we take that bit out, we will have N of them either 1s or 0s.
         * The subset XOR sum of this bit array is exactly 2^(N - 1). For a
         * robust proof, refer to the link above and my comment.
         *
         * The answer to this problem is finding the contributing bit from all
         * the elements via OR and multiply the result by 2^(N - 1)
         */
        int N = nums.length;
        int res = 0;
        for (int n : nums)
            res |= n;
        return res << (N - 1);
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
