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
    public int missingNumber(int[] nums) {
        /*
        LeetCode 268
        
        Swap.
        
        O(N), 1 ms, faster than 47.27% 
        */
        int i = 0;
        while (i < nums.length) {
            if (nums[i] == nums.length) {
                nums[i] = -1;
            } else if (nums[i] == -1 || nums[i] == i) {
                i++;
            } else {
                int tmp = nums[i];
                nums[i] = nums[tmp];
                nums[tmp] = tmp;
            }
        }
        for (i = 0; i < nums.length; i++) {
            if (nums[i] < 0)
                return i;
        }
        return nums.length;
    }
}


class Solution2 {
    public int missingNumber(int[] nums) {
        /*
         * Use sum
         */
        int sum = 0;
        for (int n : nums) sum += n;
        return nums.length * (nums.length + 1) / 2 - sum;
    }
}


class Solution3 {
    public int missingNumber(int[] nums) {
        /*
         * Use XOR
         */
        int res = nums.length;
        for (int i = 0; i < nums.length; i++)
            res ^= (i ^ nums[i]);
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
