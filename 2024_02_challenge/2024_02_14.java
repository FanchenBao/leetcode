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
    public int[] rearrangeArray(int[] nums) {
        /*
        LeetCode 2149
        
        I was not inclined to use this O(N) space method, but I couldn't
        figure out a smart way to swap the values. Hence, O(N) space it is.
        
        O(N) time and O(N) space. 5 ms, faster than 39.72%
        */
        int[] pos = new int[nums.length / 2];
        int[] neg = new int[nums.length / 2];
        int ni = 0; int pi = 0;
        for (int n : nums) {
            if (n > 0)
                pos[pi++] = n;
            else
                neg[ni++] = n;
        }
        int[] res = new int[nums.length];
        ni = 0; pi = 0;
        for (int i = 0; i < res.length; i++) {
            if (pi == ni)
                res[i] = pos[pi++];
            else
                res[i] = neg[ni++];
        }
        return res;
    }
}


class Solution3 {
    public int[] rearrangeArray(int[] nums) {
        /*
        This is a much easier implementation. Quite a shame that I didn't
        come up with this earlier.
        
        O(N) time and O(N) space. 7 ms, faster than 24.48%
        */
        int ni = 0; int pi = 0;
        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i += 2) {
            while (ni < nums.length && nums[ni] > 0)
                ni++;
            while (pi < nums.length && nums[pi] < 0)
                pi++;
            res[i] = nums[pi++];
            res[i + 1] = nums[ni++];
        }
        return res;
    }
}


class Solution {
    public int[] rearrangeArray(int[] nums) {
        /*
         * This is the from the official solution. I have to say, it is the
         * best.
         
         3 ms, faster than 100.00%
         */
        int ni = 1; int pi = 0;
        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                res[pi] = nums[i];
                pi += 2;
            } else {
                res[ni] = nums[i];
                ni += 2;
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
