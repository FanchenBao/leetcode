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
    private int helper(int[] nums, int length, int ed, int k) {
        int st = ed - length + 1;
        int i = st;
        int s = 0;
        int res = Integer.MAX_VALUE;
        for (int j = st; j <= ed; j++) {
            s += nums[j];
            while (s - nums[i] >= k)
                s -= nums[i++];
            if (s >= k)
                res = Math.min(res, j - i + 1);
        }
        return res;
    }
    
    public int shortestSubarray(int[] nums, int k) {
        /*
         * LeetCode 862 (FALLO)
         *
         * DOES NOT WORK
         */
        List<int[]> combined = new ArrayList<>();
        int s = nums[0];
        int c = 1;
        int res = Integer.MAX_VALUE;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] * nums[i - 1] >= 0) {
                s += nums[i];
                c++;
            } else {
                if (s >= k)
                    res = Math.max(res, helper(nums, c, i - 1, k));
                if (!combined.isEmpty() || s > 0) // ensure that the first sum in combined is always positive
                    combined.add(new int[]{s, c});
                s = nums[i];
                c = 1;
            }
        }
        if (s > 0) {
            if (s >= k)
                res = Math.max(res, helper(nums, c, nums.length - 1, k));
            else  // ensure that the last sum in combined is always positive
                combined.add(new int[]{s, c});
        }
        if (res < Integer.MAX_VALUE)
            return res;
        int i = 0;
        s = combined.get(0)[0];
        c = combined.get(0)[1];
        for (int j = 0; j + 2 < combined.size(); j += 2) {
            s += combined.get(j + 1)[0] + combined.get(j + 2)[0];
            c += combined.get(j + 1)[1] + combined.get(j + 2)[1];
            while (i + 2 < combined.size() && s - combined.get(i)[0] - combined.get(i + 1)[0] >= k) {
                s -= combined.get(i)[0] + combined.get(i + 1)[0];
                c -= combined.get(i)[1] + combined.get(i + 1)[1];
                i += 2;
            }
            if (s >= k)
                res = Math.min(res, c);
        }
        return res < Integer.MAX_VALUE ? res : -1;
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
