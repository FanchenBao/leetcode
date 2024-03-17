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
    public int findMaxLength(int[] nums) {
        /*
        LeetCode 525
        
        Use prefix sum, for any index k, we want to find some index i such that
        2(Pk - Pi) = k - i => 2Pk - k = 2Pi -i
        
        Thus we keep track of the first index for each 2Pi - i. Then for each
        2Pk - k, we use the stored indices of the same value 2Pk - k to find
        the max length of subarray that satisfies the requiremment. We proceed
        to find the max of all lengths.
        
        O(N), 22 ms, faster than 82.95%
        */
        Map<Integer, Integer> m = new HashMap<>();
        m.put(1, -1); // this is for the initial condition where Pi = 0 and i = -1
        int res = 0;
        int psum = 0;
        for (int i = 0; i < nums.length; i++) {
            psum += nums[i];
            int cur = 2 * psum - i;
            if (!m.containsKey(cur))
                m.put(cur, i);
            else
                res = Math.max(res, i - m.get(cur));
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
