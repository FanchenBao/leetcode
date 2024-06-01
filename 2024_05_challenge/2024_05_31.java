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
    public int[] singleNumber(int[] nums) {
        /*
         * LeetCode 260
         *
         * This is NOT according to the requirement because the runtime is
         * O(NlogN) 3 ms, faster than 45.25%
         */
        Arrays.sort(nums);
        int[] res = new int[2];
        int j = 0;
        for (int i = 0; i < nums.length; i++) {
            if ((i == 0 || nums[i - 1] != nums[i]) && (i == nums.length - 1 || nums[i + 1] != nums[i]))
                res[j++] = nums[i];
        }
        return res;
    }
}


class Solution2 {
    public int[] singleNumber(int[] nums) {
        /*
         * This solution is copied from my previous attempt, which itself was
         * inspired by a post in the discussion. Using just bit-manipulation,
         * we can XOR all the numbers to obtain a XOR b. Then right most set
         * bit of the XOR result is the first bit that differs between a and b
         * Then we just need to pick out all the numbers in nums with that bit
         * set, XOR all of them, and we will have one of the single numbers.
         * Then the other single number can be obtained very easily.
         *
         * O(N) time with O(1) space. 1 ms, faster than 100.00%
        */
        int xor = 0;
        for (int n : nums)
            xor ^= n;
        int mask = xor & (-xor);
        int a = 0;
        for (int n : nums) {
            if ((n & mask) > 0)
                a ^= n;
        }
        return new int[]{a, xor ^ a};
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
